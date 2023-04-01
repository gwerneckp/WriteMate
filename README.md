# WriteMate

WriteMate is a Python script that simulates human typing speed by pasting text into any application with a delay between keystrokes. It can also introduce random typos and pauses to make the typing more human-like.

## Prerequisites

WriteMate requires Python 3 and the following Python libraries:

- PyAutoGUI
- argparse

You can install them using pip:

```
pip install pyautogui argparse
```

## CLI

To run the CLI, use the following command:

```
python typewriter.py [options]
```

Where the arguments are:

- `--text`, `-t`: The text to be typed out.
- `--speed`, `-s`: The typing speed in seconds (default: 0.5).
- `--inverse-speed`, `-i`: The typing speed as the inverse of characters per second (overrides --speed).
- `--pause-rate`, `-pr`: The rate at which pauses occur as a float (default: 0.05).
- `-d/--delay`: Delay in seconds before typing starts (default: 5)
- `--load-from-file`, `--file`, `-f`: Load the text to be typed out from a file.
- `--verbose`, `-v`: Enable verbose logging (default: False).

For example:

```
python typewriter.py -s 0.3 -f my_text.txt
```

This will type the contents of the `my_text.txt` file at a speed of 0.3 seconds per character, with a delay of 5 seconds before typing starts.

## Random Typos and Pauses

WriteMate can introduce random typos and pauses to simulate human typing. By default, it introduces a typo in 5% of the words, and a pause in typing for 5% of the words.

If a typo is introduced, a random vowel is inserted into the word at a random position. If a pause is introduced, the script stops typing for a random duration between 0 and 1 second.

## GUI

WriteMate also comes with a graphical user interface (GUI) that allows you to interactively type out text with realistic typos and pauses. To use the GUI, run the writemate_gui.py script:

```
python writemate_gui.py
```

## License

WriteMate is released under the MIT License. See the [LICENSE](LICENSE) file for more details.
