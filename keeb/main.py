import decimal
from time import sleep
from pathlib import Path
import random
import pkg_resources

import click
import playsound
from pynput import keyboard


class Keeb:
    def __init__(self, sound_profile, sound_delay_multiplier):
        self.sound_profile = sound_profile
        self.sound_delay_multiplier = sound_delay_multiplier

    def play_key(self, key):
        key_map = {
            'a': ['a'], 'b': ['b'], 'c': ['c'], 'd': ['d'], 'e': ['e'], 'f': ['f'], 'g': ['g'], 'h': ['h'], 'i': ['i'],
            'j': ['j'], 'k': ['k'], 'l': ['l'], 'm': ['m'], 'n': ['n'], 'o': ['o'], 'p': ['p'], 'q': ['q'], 'r': ['r'],
            's': ['s'], 't': ['t'], 'u': ['u'], 'v': ['v'], 'w': ['w'], 'x': ['x'], 'y': ['y'], 'z': ['z'],
            ' ': ['SPACE'],
            'A': ['LSHIFT', 'a'], 'B': ['LSHIFT', 'b'], 'C': ['LSHIFT', 'c'], 'D': ['LSHIFT', 'd'],
            'E': ['LSHIFT', 'e'],
            'F': ['LSHIFT', 'f'], 'G': ['LSHIFT', 'g'], 'H': ['LSHIFT', 'h'], 'I': ['LSHIFT', 'i'],
            'J': ['LSHIFT', 'j'],
            'K': ['LSHIFT', 'k'], 'L': ['LSHIFT', 'l'], 'M': ['LSHIFT', 'm'], 'N': ['LSHIFT', 'n'],
            'O': ['LSHIFT', 'o'],
            'P': ['LSHIFT', 'p'], 'Q': ['LSHIFT', 'q'], 'R': ['LSHIFT', 'r'], 'S': ['LSHIFT', 's'],
            'T': ['LSHIFT', 't'],
            'U': ['LSHIFT', 'u'], 'V': ['LSHIFT', 'v'], 'W': ['LSHIFT', 'w'], 'X': ['LSHIFT', 'x'],
            'Y': ['LSHIFT', 'y'],
            'Z': ['LSHIFT', 'z'], '-': ['-'], '=': ['='], '[': ['['], ']': [']'], '\\': ['\\'], ';': [';'], "'": ["'"],
            ',': [','], '.': ['.'], '/': ['SLASH'], '0': ['0'], '1': ['1'], '2': ['2'], '3': ['3'], '4': ['4'],
            '5': ['5'],
            '6': ['6'], '7': ['7'], '8': ['8'], '9': ['9'], '!': ['LSHIFT', '1'], '@': ['LSHIFT', '2'],
            '#': ['LSHIFT', '3'],
            '$': ['LSHIFT', '4'], '%': ['LSHIFT', '5'], '^': ['LSHIFT', '6'], '&': ['LSHIFT', '7'],
            '*': ['LSHIFT', '8'],
            '(': ['LSHIFT', '9'], ')': ['LSHIFT', '0'], '_': ['LSHIFT', '-'], '+': ['LSHIFT', '='],
            '<': ['LSHIFT', ','],
            '>': ['LSHIFT', '.'], '?': ['LSHIFT', 'SLASH'], ':': ['LSHIFT', ';'], '"': ['LSHIFT', '\''],
            '{': ['LSHIFT', '['],
            '}': ['LSHIFT', ']'], '|': ['LSHIFT', '\\'], '`': ['CAPS', 'ESC'], '~': ['LSHIFT', 'CAPS', 'ESC'],
            '\n': ['ENTER'],
            'enter': ['ENTER'], 'space': ['SPACE'], 'backspace': ['BACKSPACE'], 'ctrl_l': ['LCTRL']
        }
        for key_file in key_map.get(key, ["a"]):
            playsound.playsound(str(Path(pkg_resources.resource_filename('keeb', f'sounds/{self.sound_profile}'), f'{key_file}.mp3')), block=False)

    def _artificial_pause(self, key):
        if key in ['.', ';']:
            sleep(.3)
        else:
            sleep(self.sound_delay_multiplier * float(decimal.Decimal(random.randrange(10)) / 100))

    def play_string(self, user_string):
        for key in user_string:
            self.play_key(key)
            self._artificial_pause(key)

    def _on_press(self, key):
        if key == keyboard.Key.esc:
            return False
        try:
            k = key.char
        except AttributeError:
            k = key.name
        self.play_key(k)

    def hook_keyboard(self):
        listener = keyboard.Listener(on_press=self._on_press)
        listener.start()
        listener.join()


@click.command()
@click.option('--hook', is_flag=True, help='This hooks into your keyboard and plays a sound when you type')
@click.option('--switches', default='gateron-red',
              help='Provide the sound profile, by default it\'s set to gateron-red')
@click.option('--delay', default=1.5,
              help='Sound delay multiplier for playing keyboard sound from a string')
@click.option('--string', required=False,
              help='Pass some arbitrary string to play a keyboard typing sound typing said string')
def main(hook, switches, string, delay):
    k = Keeb(switches, delay)
    if hook:
        k.hook_keyboard()
    elif string:
        k.play_string(string)
    else:
        raise Exception(
            'Please use one of the options, use --help for more details')  # TODO change this to another form of exception


if __name__ == '__main__':
    main()
