from ..model.exceptions.ProductionNotFoundException import ProductionNotFoundException


class State:
    def __init__(self, name, json):
        self.name  = name
        self._json = json
        
        
    def productions(self):
        return self._json["productions"]
    
    def next_state(self, char):
        try:
            return self._json["productions"][char]
        except KeyError:
            raise ProductionNotFoundException
    
    def is_final(self):
        return self._json["final"]