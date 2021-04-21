from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from main import CalcGridLayout


def find_widgets(root, _type):
    """search through a widget tree to find all instances of <type>"""
    to_search = [root]
    found = []
    while to_search:
        widget = to_search.pop()
        if isinstance(widget, _type):
            found.append(widget)
        to_search.extend(widget.children)
    return found


def press_sequence(input_string):
    """press a sequence of buttons, collect output, and clear the text field.
    
    input_string: string of space-separated button texts (Ex: '1 + 2 =')
    """
    for btn in input_string.split():
        buttons[btn].trigger_action()
    output = textfield.text
    buttons['AC'].trigger_action()
    return output


# create the root widget, and load the kv file to get buttons and stuff defined there
Builder.load_file('calculator.kv')
root = CalcGridLayout()

# collect references to buttons and textfield
buttons = {button.text: button for button in find_widgets(root, Button)}
textfield = find_widgets(root, TextInput)[0]
