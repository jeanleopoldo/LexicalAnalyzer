class LexicalAnalyzer:
    def __init__(self, input, lexemes):
        self._input         = input
        self._lexemes       = lexemes
        self._found_lexemes = list()
        self._queue         = list()

    def analyze(self):
        
        
        current_lexeme = self._lexemes["function"]
        self._found_lexemes.append(current_lexeme)
        current_state  = current_lexeme.initial_state()
        
        for index in range(len(self._input)):
            char = self._input[index]
            if current_state.has_production_with_char(char):
                next_state    = current_state.next_state(char)
                current_state = current_lexeme.get_state(next_state)
                current_lexeme.set_current_state(current_state)
            else:
                if not current_state.is_final():
                    self._queue.append(current_lexeme)
                    possible_lexemes = current_state.get_productions_that_leads_to_another_lexeme()
                    self.root(possible_lexemes, current_lexeme)
                    current_lexeme = self.find_next_lexeme(char, possible_lexemes)

                    current_state  = current_lexeme.get_current_state()
                    next_state     = current_state.next_state(char)
                    current_state  = current_lexeme.get_state(next_state)
                    current_lexeme.set_current_state(current_state)
                else:
                    current_lexeme = self.get_previous_lexeme(current_lexeme)
                    current_state  = current_lexeme.get_current_state()
                    next_state     = current_state.next_state(char)
                    current_state  = current_lexeme.get_state(next_state)
                    current_lexeme.set_current_state(current_state)

    def root(self, possible_lexemes, current_lexeme):
        for lexeme_str in possible_lexemes:
            lexeme = self.format(lexeme_str)
            lexeme = self._lexemes[lexeme]
            lexeme.set_generated_by(current_lexeme)

    def find_next_lexeme(self, char, bfs): #TODO fix dis
        if len(bfs) == 0:
            raise RuntimeError("there are some errors in this language.")
        raw             = bfs.pop(0)
        possible_lexeme = self.format(raw)
        lexeme          = self._lexemes[possible_lexeme]
        if lexeme.initial_state().has_production_with_char(char):
            bfs.append(lexeme)
            self._found_lexemes.append(lexeme)
            if not lexeme.get_generated_by() is None:
                self._queue.append(lexeme)
            return lexeme
        
        possible_lexeme = self._lexemes[possible_lexeme]
        lexemes         = possible_lexeme.initial_state().get_productions_that_leads_to_another_lexeme()
        for lexeme_str in lexemes:
            bfs.append(lexeme_str)
            lexeme = self.format(lexeme_str)
            lexeme = self._lexemes[lexeme]
            lexeme.set_generated_by(possible_lexeme)
            
        
        return self.find_next_lexeme(char, bfs)
           
    def get_previous_lexeme(self, lexeme):

        root = lexeme
        while root.get_generated_by() is not None:
            root     = root.get_generated_by()
            if not root.get_current_state().is_final():
                return root
        return root

    def format(self, string):
        string = string[1 : : ]
        string = string[ : -1 : ]
        return string
                
    