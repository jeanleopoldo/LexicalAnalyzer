#ifndef LEXEME_H
#define LEXEME_H

#include <string>
#include "State.h"

class Lexeme
{
    private:
        std::string _name;
        State       _initial_state;

    public:
        Lexeme(const std::string &name, State &initial_state);

};

#endif