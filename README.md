# BookBot 📚

BookBot is a command-line Python program that analyzes text files and generates a statistical report of word and character usage.

The goal of this project is to practice writing clean, modular Python code and building a real CLI-style tool that accepts user input via command-line arguments.

---

## Features

- Accepts a text file path as a command-line argument
- Counts the total number of words in the file
- Counts the frequency of each alphabetical character (case-insensitive)
- Sorts characters by frequency (highest to lowest)
- Skips non-alphabetical characters
- Produces clean, deterministic terminal output
- Gracefully handles incorrect CLI usage

---

## Usage

Run the program from the project root:

```bash
python3 main.py <path_to_book>

