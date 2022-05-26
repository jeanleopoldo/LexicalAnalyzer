#ifndef STATE_H
#define STATE_H

#include <string>
#include <map>

class State
{
    private:
        const bool _is_final;
        const bool _is_initial;
        std::map<std::string, State> _productions;
    
    public:
        State(const bool &is_initial, const bool &is_final, const std::map<std::string, State> &productions);
        bool is_initial();
        bool is_final();
        std::map<std::string, State> productions();

};

#endif