
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
            line = data[index]
            is_comment = False
            for char in line:
                if not char == " " and char == "#":
                    is_comment = True
                if is_comment:
                    break
            if is_comment:
                continue
            input = input + data[index]
        return input