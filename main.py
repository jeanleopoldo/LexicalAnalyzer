
import os

from src.inputHandler.TokensInputHandler  import TokensInputHandler
from src.inputHandler.LexemesInputHandler import LexemesInputHandler
from src.inputHandler.UserInputHandler    import UserInputHandler
from src.core.LexicalAnalyzer             import LexicalAnalyzer

_dirname = os.path.dirname(__file__)+"/"

AVAILABLE_LEXEMES_AUTOMATA = _dirname+"syntaticAnalysis/automatons/lexemes.txt"
LEXEMES_AUTOMATA_PATH      = _dirname+"syntaticAnalysis/automatons/json/"
INPUT_PATH                 = _dirname+"expr/input.txt"
TOKEN_PATH                 = _dirname+"lexicalAnalysis/tokens/"
AVAILABLE_TOKENS_AUTOMATA  = _dirname+"lexicalAnalysis/automatons/tokens.txt"
TOKENS_AUTOMATA_PATH       = _dirname+"lexicalAnalysis/automatons/json/"

if __name__ == "__main__":
    
    lexemes_input_handler = LexemesInputHandler(LEXEMES_AUTOMATA_PATH, AVAILABLE_LEXEMES_AUTOMATA)
    lexemes               = lexemes_input_handler.get_lexemes()

    user_input_handler    = UserInputHandler(INPUT_PATH)
    input                 = user_input_handler.get_input()

    tokens_input_handler  = TokensInputHandler(TOKEN_PATH,AVAILABLE_TOKENS_AUTOMATA, TOKENS_AUTOMATA_PATH)
    tokens                = tokens_input_handler.get_tokens()
    tokens_automatons     = tokens_input_handler.get_tokens_automatons()

    analyzer              = LexicalAnalyzer(input, tokens)
    analyzer.tokenize()
