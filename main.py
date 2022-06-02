
import os

from src.inputHandler.TokensInputHandler  import TokensInputHandler
from src.inputHandler.LexemesInputHandler import LexemesInputHandler
from src.inputHandler.UserInputHandler    import UserInputHandler
from src.core.LexicalAnalyzer             import LexicalAnalyzer

_dirname = os.path.dirname(__file__)+"/"

if __name__ == "__main__":
    
    available_automatons  = _dirname+"syntaticAnalysis/automatons/lexemes.txt"
    automatons_path       = _dirname+"syntaticAnalysis/automatons/json/"
    input_path            = _dirname+"expr/input.txt"
    tokens_path           = _dirname+"tokens/"
    
    lexemes_input_handler = LexemesInputHandler(automatons_path, available_automatons)
    lexemes               = lexemes_input_handler.get_lexemes()

    user_input_handler    = UserInputHandler(input_path)
    input                 = user_input_handler.get_input()

    tokens_input_handler  = TokensInputHandler(tokens_path)
    tokens                = tokens_input_handler.get_tokens()

    analyzer              = LexicalAnalyzer(input, tokens)
    analyzer.tokenize()
