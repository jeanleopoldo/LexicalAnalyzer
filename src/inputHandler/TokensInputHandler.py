import json
from .InputHandler import InputHandler
from ..model.Token import Token
class TokensInputHandler(InputHandler):
    def __init__(self, tokens_path, available_automatons, tokens_automatons_path):
        super().__init__(tokens_path)
        self._identifiers            = self._path + "identifiers.txt"
        self._keywords               = self._path + "keywords.txt"
        self._delimiters             = self._path + "delimiters.txt"
        self._operators              = self._path + "operators.txt"
        self._comments               = self._path + "comments.txt"
        self._literals               = self._path + "literals.txt"
        self._numbers                = self._path + "numbers.txt"
        self._available_automatons   = available_automatons
        self._tokens_automatons_path = tokens_automatons_path

    def get_tokens(self):

        tokens        = {}

        identifiers   = self.read_list(self._identifiers)
        tokens["id"]  = identifiers

        keywords      = self.read_list(self._keywords)
        tokens["kw"]  = keywords

        delimiters    = self.read_list(self._delimiters)
        tokens["del"] = delimiters

        operators     = self.read_list(self._operators)
        tokens["op"]  = operators

        comments      = self.read_list(self._comments)
        tokens["cmm"] = comments

        literals      = self.read_list(self._literals)
        tokens["lit"] = literals

        numbers       = self.read_list(self._numbers)
        tokens["num"] = numbers

        return tokens

    def get_tokens_automatons(self):
        tokens     = {}
        automatons = self.read_list(self._available_automatons)
        
        
        for index in range(len(automatons)):
            if automatons[index] == "#":
                print()
            path                       = self._tokens_automatons_path+automatons[index]+".json"
            str                        = self.read_file(path),
            token_json                 = json.loads(str[0])
            token                      = Token(token_json)
            tokens[token_json["name"]] = token
        return tokens