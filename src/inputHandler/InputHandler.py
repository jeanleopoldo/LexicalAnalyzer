import json
from ..model.Lexeme import Lexeme
class InputHandler:
    def __init__(self, available_automatons, input_path, automatons_path):
        self.available_automatons = available_automatons
        self.input_path           = input_path
        self.automatons_path      = automatons_path

    
    def read_file(self, path):
        file = open(path, "r")
        data = file.readlines()
        input = ""
        for index in range(len(data)):
            input = input + data[index]
        return input

    def get_input(self):
        input = self.read_file(self.input_path)
        input = input.replace(" ", "")
        input = input.replace("\n", "")

        return input
    
    def read_lexemes(self, path):
        file = open(path, "r")
        data = file.readlines()
        lexemes = list()
        for index in range(len(data)):
            lexeme = data[index].replace("\n", "")
            lexemes.append(lexeme)
        return lexemes
    
    def get_lexemes(self):
        available = self.read_lexemes(self.available_automatons)
        lexemes = {}
        for index in range(len(available)):
            str = self.read_file(self.automatons_path+available[index]+".json")
            lexeme_json = json.loads(str)
            lexeme = Lexeme(lexeme_json)
            
            lexemes[lexeme_json["name"]] = lexeme 

        return lexemes