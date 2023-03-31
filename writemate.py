import random
import string
import time
import pyautogui


class WriteMate:
    def __init__(self, speed=0.5, inverse_speed=None, typo_rate=0.05, pause_rate=0.05, text=None, load_from_file=False, verbose=False):
        self.speed = speed
        self.typo_rate = typo_rate
        self.pause_rate = pause_rate
        if inverse_speed is not None:
            self.speed = 1 / inverse_speed
        self.original_text = ''
        self.words = []
        self.verbose = verbose
        if text is not None:
            self.load_text(text)
        elif load_from_file:
            self.load_from_file()

    def load_from_file(self, filename='text'):
        with open(filename, 'r') as f:
            text = f.read()
        self.load_text(text)

    def load_text(self, text: str):
        self.original_text = text
        self.words = text.split(sep=" ")

    def log(self, message):
        if self.verbose:
            print(f'[+] {message}')

    def type_word(self, word: str):
        for letter in word:
            if letter not in string.ascii_letters + string.digits + ' .,;!?()$@[]\{\}':
                num = hex(ord(letter))
                pyautogui.hotkey('ctrl', 'shift', 'u')
                for n in num:
                    pyautogui.typewrite(n)
                pyautogui.typewrite(' ')
            else:
                pyautogui.typewrite(letter)
            time.sleep(self.speed + ((self.speed/5) * random.random()))

    def insert_typo(self, word: str) -> str:
        # Select a random index to insert the typo
        typo_index = random.randint(0, len(word))

        # Generate a random typo to insert
        typo = random.choice(['a', 'e', 'i', 'o', 'u'])

        # Insert the typo into the word
        new_word = word[:typo_index] + typo + word[typo_index:]

        return new_word

    def type_next_word(self):
        # This is the end of a sentence, so we are going to give more delay to simulate the writer taking a breath to
        # start a new sentence.
        word = self.words.pop(0)
        if word.endswith(".") or word.endswith("!") or word.endswith("?") or word.endswith(","):
            self.log('End of sentence, taking a breath')
            self.type_word(word)

            time.sleep(self.speed*10 + (self.speed*20 * random.random()))
            pyautogui.typewrite(" ")
            return

        # This is a random event that will cause the writer to stop typing for a few seconds
        if random.random() < self.pause_rate:
            self.log('Pausing to think')
            time.sleep(self.speed*20 * random.random())

        # This is a random event that will cause the writer to make a typo
        elif random.random() < self.typo_rate:
            misspelled_word = self.insert_typo(word)
            self.log(f'Making a typo on word "{word}" -> "{misspelled_word}"')
            self.type_word(misspelled_word)

            time.sleep(self.speed + (self.speed/5 * random.random()))
            pyautogui.hotkey('ctrl', 'backspace')

        # This is a normal word, so we are going to type it out and give a small delay to simulate the writer typing
        self.log(f'Typing word "{word}"')
        self.type_word(word)

        # Insert a space after the word
        pyautogui.typewrite(" ")

    def type_text(self):
        self.log(f'Typing text with {len(self.words)} words')
        while len(self.words) > 0:
            self.type_next_word()
        self.log('Done typing text!')


if __name__ == '__main__':
    # Example usage:
    text = 'This is a test.'
    write_mate = WriteMate(speed=0.3, text=text, verbose=True)
    write_mate.type_text()
