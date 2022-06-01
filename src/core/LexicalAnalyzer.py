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
        if word == " ":
            return
        found = False
        for token in self._tokens:
            array = self._tokens[token]
            if word in array:
                found = True
                self._found_tokens[token].append(word)
        
        if not found:
            self._found_tokens["id"] = word