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

## Usage

To use WriteMate, run the `typewriter.py` script with the following arguments:

- `-s/--speed`: Typing speed in seconds (default: 0.5)
- `-i/--inverse/--inverse-speed`: Typing speed as the inverse of characters per second (overrides `-s/--speed`)
- `-f/--file`: File containing the text to type (default: text)
- `-d/--delay`: Delay in seconds before typing starts (default: 5)
- `--typo-rate`: Typo rate as a float (default: 0.05)
- `--pause-rate`: Pause rate as a float (default: 0.05)

For example:

```
python typewriter.py -s 0.3 -f my_text.txt
```

This will type the contents of the `my_text.txt` file at a speed of 0.3 seconds per character, with a delay of 5 seconds before typing starts.

## Random Typos and Pauses

WriteMate can introduce random typos and pauses to simulate human typing. By default, it introduces a typo in 5% of the words, and a pause in typing for 5% of the words.

If a typo is introduced, a random vowel is inserted into the word at a random position. If a pause is introduced, the script stops typing for a random duration between 0 and 1 second.

## License

WriteMate is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

WriteMate uses the PyAutoGUI library to automate keyboard and mouse actions.
