DEL = "del"
OP  = "op"
LIT = "lit"
ID  = "id"
CMM = "cmm"


class LexicalAnalyzer:
    def __init__(self, input, tokens):
        self._input          = input
        self._tokens         = tokens
        self._ordered_tokens = list()


    def tokenize(self):
        self._found_tokens  =  {"kw":[], "id":[], "del":[], "op":[], "cmm":[], "lit":[]}
        word = ""
        cmm = False
        for index in range(len(self._input)):
            char = self._input[index]
            if char == ";":
                print()
            ## dealing with comments
            if cmm:
                if char == '\\':
                    cmm = False
                    self._ordered_tokens.append({CMM : word})
                    word = ""
                else:
                    word += char
                continue
            
            if char in self._tokens[CMM]:
                
                cmm = True
                word += char
                continue

            if char in self._tokens[DEL] or char in self._tokens[OP] or char == " ":
                token = self.find_token(word)
                if token is not None:
                    self._ordered_tokens.append({token : word})
                token = self.find_token(char)
                if token is not None:
                    self._ordered_tokens.append({token : char})
                word = ""
            else:
                word +=char
            
    def find_token(self, word):
        if word == " " or word =="":
            return
        
        #dealing with strings
        if word[0] == '"' and word[len(word)-1] == '"':
            return LIT

        # dealing with operators, delimites and keywords
        for token in self._tokens:
            array = self._tokens[token]
            if word in array:
                self._found_tokens[token].append(word)
                return token
        
        #dealing with identifiers
        if word[0] is not type(word[0]) != int and word[0] is not type(word[0]) != float: # prevents id starting with numbers: var 3id = ""
            self._found_tokens[ID].append(word)
            return ID