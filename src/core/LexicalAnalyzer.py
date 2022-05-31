from .LexicalAnalyzerState import LexicalAnalyzerState

class LexicalAnalyzer:
    def __init__(self, input, lexemes):
        self._input         = input
        self._lexemes       = lexemes
        self._found_lexemes = list()

    def analyze(self):
        
        queue          = list()
        current_lexeme = self._lexemes["function"]
        self._found_lexemes.append(current_lexeme)
        current_state  = current_lexeme.initial_state()
        
        for index in range(len(self._input)):
            char = self._input[index]
            if current_state.has_production_with_char(char):
                next_state    = current_state.next_state(char)
                current_state = current_lexeme.get_state(next_state)
            else:

                if not current_state.is_final():
                    lexical_state    = LexicalAnalyzerState(current_lexeme, current_state)
                    queue.append(lexical_state)
                    possible_lexemes = current_state.get_productions_that_leads_to_another_lexeme()
                    bfs              = list(possible_lexemes)
                    current_lexeme   = self.find_next_lexeme(char, bfs)
                    current_state    = current_lexeme.initial_state()
                    next_state       = current_state.next_state(char)
                    current_state    = current_lexeme.get_state(next_state)
                else:
                    this_state       = queue.pop()
                    current_lexeme   = this_state.lexeme()
                    current_state    = this_state.state()
                    next_state       = current_state.next_state(char)
                    current_state    = current_lexeme.get_state(next_state)
    
    def find_next_lexeme(self, char, bfs):
        if len(bfs) == 0:
            raise RuntimeError("there are some errors in this language.")
        possible_lexeme = bfs.pop(0)
        possible_lexeme = possible_lexeme[1 : : ]
        possible_lexeme = possible_lexeme[ : -1 : ]
        lexeme          = self._lexemes[possible_lexeme]
        if lexeme.initial_state().has_production_with_char(char):
            bfs.append(lexeme)
            self._found_lexemes.append(lexeme)
            return lexeme
        
        possible_lexeme = self._lexemes[possible_lexeme]
        lexemes = possible_lexeme.initial_state().get_productions_that_leads_to_another_lexeme()
        for lexeme in lexemes:
            possible_lexeme.generated_by(possible_lexeme)
            bfs.append(lexeme)
        
        return self.find_next_lexeme(char, bfs)
           


                
                
    