from .State import State

class Lexeme:
    def __init__(self, json):
        self._json         = json
        self._generated_by = None
        self.create_states()
        self._current_state = self._states["q0"]

    def create_states(self):
        self._states = {}
        for name in self._json["states"]:
            json               = self._json["states"][name]
            state              = State(name, json)
            self._states[name] = state
    
    def set_generated_by(self, lexeme):
        self._generated_by = lexeme

    def get_generated_by(self):
        return self._generated_by

    def name(self):
        return self._json["name"]
    
    def set_current_state(self, state):
        self._current_state = state

    def get_current_state(self):
        return self._current_state    
    def states(self):
        return self._states
    
    def get_state(self, state):
        return self._states[state]
    
    def initial_state(self):
        return self._states["q0"]
    

    
