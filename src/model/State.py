from ..model.exceptions.ProductionNotFoundException import ProductionNotFoundException


class State:
    def __init__(self, name, json):
        self._name  = name
        self._json = json
    
    def name(self):
        return self._name
    
    def productions(self):
        return self._json["productions"]
    
    def next_state(self, char):
        try:
            return self._json["productions"][char]
        except KeyError:
            raise ProductionNotFoundException
    
    def is_final(self):
        return self._json["final"]
    
    def has_production_with_char(self, char):
        return char in self._json["productions"]
    
    def get_productions_that_leads_to_another_lexeme(self):
        lexemes = [x for x in self._json["productions"] if x[0]=="<" and x[len(x)-1] == ">"]
        return lexemes