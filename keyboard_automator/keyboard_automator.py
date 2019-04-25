import json
import os
import sys
import time

import pyautogui


DIR_PATH = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE = 'configs.json'
CONFIG_FILE_PATH = os.path.join(DIR_PATH, CONFIG_FILE)


DEFAULT_COLLECTION = 'startUp'


def autoKeyboard(collection=DEFAULT_COLLECTION):
    with open(CONFIG_FILE_PATH, 'r') as input_file:
        json_data = json.load(input_file)
        cmds = json_data[collection].get('cmds')
        for cmd in cmds:
            if cmd['type'] == 'hotkey':
                pyautogui.hotkey(*cmd['args'].split(','))
            elif cmd['type'] == 'press':
                pyautogui.press(cmd['args'])
            elif cmd['type'] == 'typewrite':
                pyautogui.typewrite(cmd['args'])
            elif cmd['type'] == 'wait':
                time.sleep(cmd['args'])


if __name__ == '__main__':
    if (len(sys.argv) == 2):
        autoKeyboard(sys.argv[1])
    else:
        autoKeyboard()