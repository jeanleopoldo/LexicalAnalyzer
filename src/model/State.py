from ..model.exceptions.ProductionNotFoundException import ProductionNotFoundException


class State:
    def __init__(self, name, json):
        self._name    = name
        self._initial = json["initial"]
        self._final   = json["final"]
        self._json    = json
        self.create_productions()
    
    def name(self):
        return self._name
    
    def create_productions(self):
        self._productions = {}
        for head in self._json["productions"]:
            tail = self._json["productions"][head]
            self._productions[head] = tail

    def productions(self):
        return self._productions
    
    def next_state_by_char(self, char):
        try:
            return self._productions[char]
        except KeyError:
            raise ProductionNotFoundException
    def next_state_by_lexeme(self, lexeme):
        try:
            return self._productions[lexeme]
        except KeyError:
            raise ProductionNotFoundException
    
    def is_final(self):
        return self._final
    
    def has_production_with_char(self, char):
        return char in self._productions
    
    def get_productions_that_leads_to_another_lexeme(self):
        lexemes = [x for x in self._productions if x[0]=="<" and x[len(x)-1] == ">"]
        return lexemes

    def update_final_state(self, head, tail):
        self._productions[head] = tail
        self._final             = False
    
    def update_initial_state(self):
        self._initial = False

    def set_this_as_final_state(self):
        self._final = True

    def toJSON(self):
        JSONObject = {
            "initial"     : self._initial,
            "final"       : self._final,
            "productions" : self._productions
        }

        return JSONObject

