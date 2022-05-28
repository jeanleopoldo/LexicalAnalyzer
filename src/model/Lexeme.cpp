#include "Lexeme.h"

Lexeme::Lexeme(const std::string &name, State &initial_state):
    _name(name),
    _initial_state(initial_state) {}