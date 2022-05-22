#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

std::string read_input()
{
    std::string   line;
    std::ifstream file ("./expr/file.txt");
    std::string   input;
    if (file.is_open())
    {
        while ( getline (file, line) )
        {
            input += line;
        }
        file.close();
    }

    return input;
}

void remove_white_spaces(std::string& input)
{
    input.erase(std::remove(input.begin(), input.end(), ' '), input.end());
}

std::string get_input()
{
    std::string input = read_input();
    remove_white_spaces(input);
    return input;
}

int main()
{
    std::string input = get_input();
    std::cout << input<<std::endl;
    return 0;
}