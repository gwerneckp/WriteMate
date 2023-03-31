import argparse
from writemate import WriteMate
from time import sleep
import sys
import subprocess
import os


def get_default_editor():
    if sys.platform.startswith('win'):
        try:
            import winreg

            with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, '.txt') as key:
                value, _ = winreg.QueryValueEx(key, 'Content Type')
            with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, value) as key:
                value, _ = winreg.QueryValueEx(key, 'PerceivedType')
            with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, f'{value}file\\shell\\open\\command') as key:
                value, _ = winreg.QueryValueEx(key, None)
            return value.split()[0]
        except:
            # fallback to a default editor if any of the registry keys are missing
            return 'notepad.exe'
    else:
        return os.environ.get('EDITOR', 'vi')


def get_text_from_editor():
    filename = 'text.temp'
    editor = get_default_editor()
    subprocess.run([editor, filename])
    with open(filename, 'r') as f:
        text = f.read()
    os.remove(filename)
    return text


def countdown(seconds: int):
    # Delay for a few seconds to give time to switch to the target window
    print_size = len(str(seconds))
    for i in range(seconds, 0, -1):
        remaining = ' ' * (print_size - len(str(i)))
        print(str(i) + remaining + '', end='\r', flush=True)
        sleep(1)

    print('...', end='\r', flush=True)


parser = argparse.ArgumentParser(
    description='Type out text with typos and pauses')
parser.add_argument('--text', '-t', type=str, default=None,
                    help='the text to be typed out')
parser.add_argument('--speed', '-s', type=float, default=0.5,
                    help='the typing speed (default: 0.5)')
parser.add_argument('--inverse-speed', '-i', type=float, default=None,
                    help='the inverse of the typing speed (overrides --speed)')
parser.add_argument('--typo-rate', '-tr', type=float, default=0.05,
                    help='the rate at which typos occur (default: 0.05)')
parser.add_argument('--pause-rate', '-pr', type=float, default=0.05,
                    help='the rate at which pauses occur (default: 0.05)')
parser.add_argument('--load-from-file', '--file' '-f', type=str, default=None,
                    help='load the text to be typed out from a file')
parser.add_argument('--verbose', '-v', action='store_true',
                    help='enable verbose logging (default: False)')

args = parser.parse_args()

if args.inverse_speed is not None and args.speed != 0.5:
    print('Warning: Both --speed and --inverse-speed were specified. Ignoring --speed.')


if not args.text and not args.load_from_file:
    print('Warning: No text was specified, getting text from editor.')
    args.text = get_text_from_editor()

if args.load_from_file and args.text:
    print('Warning: Both text and --load-from-file were specified. Ignoring --text.')

if __name__ == '__main__':
    wm = WriteMate(text=args.text, speed=args.speed, inverse_speed=args.inverse_speed,
                   typo_rate=args.typo_rate, pause_rate=args.pause_rate, verbose=args.verbose, load_from_file=args.load_from_file)

    wm.type_text()
