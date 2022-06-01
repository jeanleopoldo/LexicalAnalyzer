DEL = "del"
OP  = "op"


class LexicalAnalyzer:
    def __init__(self, input, tokens):
        self._input         = input
        self._tokens        = tokens


    def tokenize(self):
        self._found_tokens  =  {"kw":[], "id":[], "del":[], "op":[], "cmm":[], "lit":[]}
        word = ""
        for index in range(len(self._input)):
            char = self._input[index]

            if char in self._tokens[DEL] or char in self._tokens[DEL]:
                self.find_token(word)
                word = ""
            
            if char == " ":
                self.find_token(word)
                word = ""
            else:
                word +=char
        
        print("")
    
    def find_token(self, word):
        if word == " " or word =="":
            return
        found = False
        for token in self._tokens:
            array = self._tokens[token]
            if word in array:
                found = True
                self._found_tokens[token].append(word)
        
        if not found and word[0] is not type(word[0])!=int and word[0] is not type(word[0])!=float: # prevents id starting with numbers: var 3id = ""
            self._found_tokens["id"].append(word)
        
        # TODO
        # 1. + is being set as id instead of op
        # 2 num is is being set as id instead of literal
        # 3 needs to find string as literal