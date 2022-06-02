import json

from .InputHandler  import InputHandler
from ..model.Lexeme import Lexeme

class LexemesInputHandler(InputHandler):
    def __init__(self, lexemes_path, available_automatons):
        super().__init__(lexemes_path)
        self._available_automatons = available_automatons
    
    def get_lexemes(self):
        available = self.read_list(self._available_automatons)
        lexemes   = {}
        for index in range(len(available)):
            str                          = self.read_file(self._path + available[index]+".json")
            lexeme_json                  = json.loads(str)
            lexeme                       = Lexeme(lexeme_json)            
            lexemes[lexeme_json["name"]] = lexeme 
        return lexemes