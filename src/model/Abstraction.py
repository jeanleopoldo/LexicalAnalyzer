import json
from .State import State

class Abstraction:
    def __init__(self, json):
        if json["name"] == "hashtag":
            self._name = "#"
        else:
            json["name"]
        self._json          = json
        self._generated_by  = None
        self._states        = {}
        self.create_states()
        self._current_state = self._states["q0"]
    
    def create_states(self):
        
        for name in self._json["states"]:
            json               = self._json["states"][name]
            state              = State(name, json)
            self._states[name] = state
    
    def name(self):
        return self._name

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
    
    def toJSON(self):
        return json.dumps(self)
    
    