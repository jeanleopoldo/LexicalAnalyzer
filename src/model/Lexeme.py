
from .Abstraction import Abstraction
class Lexeme(Abstraction):
    def __init__(self, json):
        super().__init__(json)
    
    def set_generated_by(self, lexeme):
        self._generated_by = lexeme

    def get_generated_by(self):
        return self._generated_by


    

    

    
