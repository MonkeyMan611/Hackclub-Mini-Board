# You import all the IOs of your board
import board
import neopixel
import random

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.GP1, board.GP2, board.GP4, board.GP3]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

NUM_LEDS = 4
pixels = neopixel.NeoPixel(board.GP6, NUM_LEDS, brightness=0.4, auto_write=True)

def random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )

def light_random():
    color = random_color()
    for i in range(NUM_LEDS):
        pixels[i] = color

def clear_leds():
    for i in range(NUM_LEDS):
        pixels[i] = (0, 0, 0)

# Here you define the buttons corresponding to the pins
keyboard.keymap = [
    [
        KC.A,
        KC.DELETE,
        KC.MACRO("Hello world!"),
        KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),
    ]
]

def process_key(keyboard, key, is_pressed, intkey):
    if is_pressed:
        light_random()
    else:
        clear_leds()
    return True

keyboard.process_key = process_key

# Start kmk!
if __name__ == '__main__':
    
