import os
from src.inputHandler.InputHandler import InputHandler
from src.core.LexicalAnalyzer      import LexicalAnalyzer

dirname = os.path.dirname(__file__)+"/"

if __name__ == "__main__":
    
    available_automatons = "automatons/lexemes.txt"
    automatons_path      = "automatons/json/"
    input_path           = "expr/input.txt"
    
    input_handler = InputHandler(available_automatons, input_path, automatons_path)
    input         = input_handler.get_input()
    lexemes       = input_handler.get_lexemes()

    analyzer      = LexicalAnalyzer(input, lexemes)
    analyzer.analyze()
