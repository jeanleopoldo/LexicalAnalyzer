# LexicalAnalyzer
This is an implementation of a lexical analyzer in Python

## Requirements
[python 3.9.12](https://www.python.org/downloads/release/python-3912/)

## How to run
- one shall insert a regular grammar in ./expr/file.txt
- one shall run ./scripts/run.sh
    - the script is meant for linux
    - alternatively, one shall run `python3 main.py` once in project's root folder
- the **token table** and the **generated automaton** are in `./output/token_table.json` and `./output/automatons.json` respectively
    - for a better view, one may put the desired file into a json formatter, such as [JSON formatter](https://jsonformatter.org/).
## Documentation
[tokens](https://docs.google.com/document/d/1lHORtHnWSRQFe5K1vXkKPAZxZMa5mhE2Ebdm48LD0Ls/edit?usp=sharing)

## Contribuition
### Commits
This project adheres [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

## Further informations

- lines that start with `#` are not to be considered as they are, by the language definition, comments