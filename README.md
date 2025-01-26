# Password Generator

This project generates memorable and random passwords. The memorable passwords are generated using a list of common English nouns, while the random passwords are generated using a mix of letters, digits, and punctuation.

## Features

- Generates memorable passwords using common English nouns and digits.
- Generates random passwords using a mix of letters, digits, and punctuation.
- Saves generated passwords to separate files in different directories (`Memorable` and `Random`).
- Creates directories if they do not exist.

## Requirements

- Python 3.x

## Usage

1. Ensure you have a file named `top_english_nouns_lower_100000.txt` in the same directory as the script. This file should contain a list of common English nouns, one per line.
2. Run the script:

    ```sh
    python assignment1.py
    ```

3. Follow the prompts to generate either a memorable or random password.
