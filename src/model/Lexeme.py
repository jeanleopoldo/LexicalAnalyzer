from .State import State

class Lexeme:
    def __init__(self, json):
        self._json = json
        self.create_states()

    def create_states(self):
        self._states = {}
        for name in self._json["states"]:
            json = self._json["states"][name]
            state = State(name, json)
            self._states[name] = state
        
        print("")
    
    def generated_by(self, lexeme):
        self._generated_by = lexeme
    
    def name(self):
        return self._json["name"]
    
    def states(self):
        return self._states
    
    def get_state(self, state):
        return self._states[state]
    
    def initial_state(self):
        return self._states["q0"]
    
