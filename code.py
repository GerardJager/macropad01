from adafruit_macropad import MacroPad
from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
import time

macropad = MacroPad()
text_lines = macropad.display_text(title="MacroPad Info")

while True:
    key_event = macropad.keys.events.get()
    if key_event and key_event.pressed:
        text_lines[0].text = "Key {} pressed!".format(key_event.key_number)
        macropad.pixels[key_event.key_number] = (255, 0, 0)
        macropad.keyboard.send(Keycode.COMMAND, Keycode.SHIFT, Keycode.Y)
        
    if key_event and key_event.released:
        text_lines[0].text = "Key {} released!".format(key_event.key_number)
        macropad.pixels[key_event.key_number] = (0, 255, 0)
    
    text_lines[1].text = "Rotary encoder {}".format(macropad.encoder)
    text_lines[2].text = "Encoder switch: {}".format(macropad.encoder_switch)
    text_lines.show()
    

# Docs
# https://docs.circuitpython.org/projects/macropad/en/latest/index.html