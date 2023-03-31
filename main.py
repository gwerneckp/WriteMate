import random
import string
import time

import pyautogui
import argparse

parser = argparse.ArgumentParser(description='Typing Simulator')
parser.add_argument('-s', '--speed', type=float, default=0.5,
                    help='Typing speed in seconds')
parser.add_argument('-i', '--inverse', '--inverse-speed',
                    type=float, default=None)
parser.add_argument('-f', '--file', type=str,
                    default='text', help='File to type')
parser.add_argument('-d', '--delay', type=int, default=5,
                    help='Delay in seconds before typing starts')
args = parser.parse_args()

if args.inverse is not None:
    SPEED = 1 / args.inverse
else:
    SPEED = args.speed

DELAY = args.delay
FILE = args.file

paragraph = """"""
# get paragraph from file
with open(FILE, "r") as f:
    paragraph = f.read()


def random_letter() -> str:
    return random.choice("abcdefghijklmnopqrstuvwxyz")


def type_word(word: str):
    for letter in word:
        if letter not in string.ascii_letters + string.digits + ' .,;!?()$@[]\{\}':
            num = hex(ord(letter))
            pyautogui.hotkey('ctrl', 'shift', 'u')
            for n in num:
                pyautogui.typewrite(n)
            pyautogui.typewrite(' ')
        else:
            pyautogui.typewrite(letter)
        time.sleep(SPEED + ((SPEED/5) * random.random()))

# def type_word(word: str):
#     for letter in word:
#         if letter == '\n':
#             pyautogui.typewrite('enter')
#         elif letter in string.printable and letter not in [' ', '\t']:
#             pyautogui.press(letter)
#         else:
#             pyautogui.typewrite(letter)
#         time.sleep(SPEED + ((SPEED/5) * random.random()))


def insert_typo(word: str) -> str:
    # Select a random index to insert the typo
    typo_index = random.randint(0, len(word))

    # Generate a random typo to insert
    typo = random.choice(['a', 'e', 'i', 'o', 'u'])

    # Insert the typo into the word
    new_word = word[:typo_index] + typo + word[typo_index:]

    return new_word


# Delay for a few seconds to give time to switch to the target window
print_size = len(str(DELAY))
for i in range(DELAY, 0, -1):
    remaining = ' ' * (print_size - len(str(i)))
    print(str(i) + remaining, end='\r', flush=True)
    time.sleep(1)
print('...', end='\r', flush=True)

# Splitting the paragraph into a list of words
words = paragraph.split(sep=" ")

# Looping through the words
for word in words:
    # This is the end of a sentence, so we are going to give more delay to simulate the writer taking a breath to
    # start a new sentence.
    if word.endswith(".") or word.endswith("!") or word.endswith("?") or word.endswith(","):
        type_word(word)

        time.sleep(SPEED*10 + (SPEED*20 * random.random()))
        pyautogui.typewrite(" ")
        continue

    # This is a random event that will cause the writer to stop typing for a few seconds
    elif random.random() < 0.05:
        time.sleep(SPEED*20 * random.random())

    # This is a random event that will cause the writer to make a typo
    elif random.random() < 0.05:
        type_word(insert_typo(word))

        time.sleep(SPEED + (SPEED/5 * random.random()))
        pyautogui.hotkey('ctrl', 'backspace')

    # This is a normal word, so we are going to type it out and give a small delay to simulate the writer typing
    type_word(word)

    # Insert a space after the word
    pyautogui.typewrite(" ")

print('Done!', end='\r', flush=True)
print('', end='\r', flush=True)
