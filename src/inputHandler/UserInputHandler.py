from .InputHandler import InputHandler
class UserInputHandler(InputHandler):
    def __init__(self, user_input_path):
        super().__init__(user_input_path)
    
    def get_input(self):
        input = self.read_file(self._path)
        input = input.replace("\n", " ")
        return input