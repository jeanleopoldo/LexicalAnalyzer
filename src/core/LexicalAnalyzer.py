from ..model.exceptions.ProductionNotFoundException import ProductionNotFoundException

class LexicalAnalyzer:
    def __init__(self, input, lexemes):
        self._input   = input
        self._lexemes = lexemes

    def analyze(self):
        found_lexemes  = list()
        char           = self._input[0]
        start_lexeme   = self._lexemes["function"]
        found_lexemes.append(start_lexeme)
        initial_state  = start_lexeme.initial_state()
        next_state     = initial_state.next_state(char)
        current_state  = start_lexeme.get_state(next_state)
        current_lexeme = start_lexeme
        
        index = 1
        previous_lexeme = None
        for index in range(len(self._input)-1):
            try:
                index        += 1
                char          = self._input[index]
                current_state = current_lexeme.get_state(next_state)
                next_state    = current_state.next_state(char)
            except ProductionNotFoundException:

                if current_state.is_final():
                    next_state      = previous_state.next_state(char)
                    current_lexeme  = previous_lexeme 
                else:
                    previous_lexeme = current_lexeme
                    previous_state  = current_state
                    current_lexeme  = self.find_next_lexeme(current_state, char)
                    found_lexemes.append(current_lexeme)
                    next_state      = current_lexeme.initial_state()
                    next_state      = next_state.next_state(char)
                  
                
    
    def find_next_lexeme(self, state, char):
        raise Exception("not implemented yet")
                
                
    