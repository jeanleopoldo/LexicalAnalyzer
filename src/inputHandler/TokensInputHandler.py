from ast import operator
from .InputHandler import InputHandler
class TokensInputHandler(InputHandler):
    def __init__(self, tokens_path):
        super().__init__(tokens_path)
        self._identifiers = self._path + "identifiers.txt"
        self._keywords    = self._path + "keywords.txt"
        self._delimiters  = self._path + "delimiters.txt"
        self._operators   = self._path + "operators.txt"
        self._comments    = self._path + "comments.txt"
        self._literals    = self._path + "literals.txt"

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

        return tokens



    
    