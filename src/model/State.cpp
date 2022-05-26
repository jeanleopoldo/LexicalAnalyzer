#include "State.h"

State::State(const bool &is_initial, const bool &is_final, const std::map<std::string, State> &productions) : 
    _is_initial(is_initial),
    _is_final(is_initial),
    _productions(productions) {}

bool State::is_initial()
{
    return _is_initial;
}

bool State::is_final()
{
    return _is_final;
}

std::map<std::string, State> State::productions()
{
    return _productions;
}