import json

class OutputHandler:
    def __init__(self, path, automaton, token_table):
        self._path        = path
        self._automaton   = automaton
        self._token_table = token_table
    

    def generate_automaton_output(self):
        path = self._path + "automaton.json"
        states = [x.toJSON() for x in self._automaton]
        self.write_file(states, path)
    

    def generate_token_table_output(self):
        path = self._path + "token_table.json"
        
        self.write_file(self._token_table, path)

    
    def write_file(self, to_file, path):
        file_into_json = json.dumps(to_file)
        file           = open(path, "w")
        file.write(file_into_json)