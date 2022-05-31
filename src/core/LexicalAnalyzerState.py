class LexicalAnalyzerState:
    def __init__(self, lexeme, state):
        self._lexeme = lexeme
        self._state  = state
    
    def lexeme(self):
        return self._lexeme
    
    def state(self):
        return self._state