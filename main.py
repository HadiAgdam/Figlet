import sys
from figlet import convert


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the text as a command-line argument.")
        sys.exit(1)

    text = " ".join(sys.argv[1:])  # Join all arguments after the script name as the text input
    print(convert(text))