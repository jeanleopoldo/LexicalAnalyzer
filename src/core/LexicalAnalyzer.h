#ifndef LEXICAL_ANALIZER_H
#define LEXICAL_ANALIZER_H

#include <list>
#include "../model/Lexeme.h"


class LexicalAnalyzer
{
    private:
        const std::string                   _input;
        const std::map<std::string, Lexeme> _lexemes;
              std::list<Lexeme>             _recognized_lexemes;
        LexicalAnalyzer(const std::string &input, const std::map<std::string, Lexeme> &lexemes);
    public:
        void find_lexemes();

};

#endif