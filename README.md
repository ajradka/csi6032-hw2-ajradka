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

Run the built-in tests from the repository root:

```powershell
python -m unittest discover -s tests
```