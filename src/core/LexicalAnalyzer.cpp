#include "LexicalAnalyzer.h"

LexicalAnalyzer::LexicalAnalyzer(const std::string &input, const std::map<std::string, Lexeme> &lexemes) :
    _input(input),
    _lexemes(lexemes){}

void LexicalAnalyzer::find_lexemes()
{
    std::string recognized_lexeme = "";
    for(int index = 0; index < _input.length(); index++)
    {
        auto letter = _input[index];
        if(letter == ' ')
        {
            try
            {
                auto it     = _lexemes.find(recognized_lexeme);
                auto lexeme = it->second;
                _recognized_lexemes.push_back(lexeme);

            }
            catch(const std::exception& e)
            {
                throw "an error was found whilst recognizing a lexeme.";
            }
        }
    }
}
    