 _   _ _____ _     _      ___    __        __ ___  ____  _     ____  
| | | | ____| |   | |    / _ \   \ \      / // _ \|  _ \| |   |  _ \ 
| |_| |  _| | |   | |   | | | |   \ \ /\ / /| | | | |_) | |   | | | |
|  _  | |___| |___| |___| |_| |    \ V  V / | |_| |  _ <| |___| |_| |
|_| |_|_____|_____|_____|\___/      \_/\_/   \___/|_| \_|_____|____/ 

# Figlet Converter

This project converts text into a styled format using a custom `convert` function inspired by the `figlet` tool. The project includes two main files: `figlet.py` for the conversion logic and `main.py` for executing the conversion via command-line input.

## Files

- **figlet.py**: Contains the `convert` function that processes text into a styled format.
- **main.py**: A command-line interface for the `convert` function, allowing users to input text and receive styled output.
- **chars.txt**: A text file containing the character mapping used by `convert` to style the text.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the project files.
2. Ensure that `figlet.py`, `main.py`, and `chars.txt` are in the same directory.

## Usage

To convert text using the command line:

```bash
python3 main.py "Your Text Here"
```

### Example

```bash
python3 main.py "Hello World"
```

This command will output the styled version of "Hello World" in your terminal.

## Customization

- **chars.txt**: Customize the `chars.txt` file to define how each character should be styled.
- **convert function**: Modify the `convert` function in `figlet.py` to change how text is processed and styled.
