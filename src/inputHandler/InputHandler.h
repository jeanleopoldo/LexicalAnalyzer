#ifndef INPUT_HANDLER_H
#define INPUT_HANDLER_H

#include <string>
#include <map>
#include "../model/Lexeme.h"

class InputHandler
{
    private:
        const std::string _input;
        const std::string _file_path = "../../expr/file.txt";
        const std::map<std::string, Lexeme> _lexemes;

    
    public:
        InputHandler();
        std::map<std::string, Lexeme> generate_lexemes_table();
        

};

#endif