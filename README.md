# csi6032-hw2-ajradka
Course: Machine Learning CSI6032
HW 2
Repository URL: https://github.com/ajradka/csi6032-hw2-ajradka.git
Windows 11
This assignment is to practice building and interacting with AI agents. This repository contains the checkpoint setup for HW2, including the starter notebook, a sample text file, adn the initial commit before running an AI agent on the codebase. 

## Text statistics

Run the command-line program with one UTF-8 text file:

```powershell
python src\text_stats.py sample.txt
```

It prints JSON with the number of `lines`, `words`, and `characters`, for example:

```json
{"characters": 136, "lines": 5, "words": 32}
```

To include the most frequent words, pass an optional `--top N` argument:

```powershell
python src\text_stats.py sample.txt --top 3
```

The JSON output then includes a `top` array of up to `N` objects. Words are
counted case-insensitively and ties are ordered alphabetically:

```json
"top": [{"word": "example", "count": 4}, {"word": "text", "count": 3}]
```

Run the built-in tests from the repository root:

```powershell
python -m unittest discover -s tests
```