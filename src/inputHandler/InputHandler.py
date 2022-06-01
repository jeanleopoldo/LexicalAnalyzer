
class InputHandler:
    def __init__(self, path):
        self._path = path

    def read_list(self, path):
        file = open(path, "r")
        data = file.readlines()
        elements = list()
        for index in range(len(data)):
            line = data[index].replace("\n", "")
            elements.append(line)
        return elements
    
    def read_file(self, path):
        file = open(path, "r")
        data = file.readlines()
        input = ""
        for index in range(len(data)):
            input = input + data[index]
        return input