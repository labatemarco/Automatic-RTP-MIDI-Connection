import pyautogui
from time import sleep


screen_width = pyautogui.size()[0]
screen_height = pyautogui.size()[1]
with pyautogui.hold('command'):
    pyautogui.press('space')
pyautogui.typewrite('audio midi setup')
pyautogui.press('enter')           # Open Audio Midi Setup
sleep(1.5)
with pyautogui.hold('command'):    # Open Midi Studio
    pyautogui.press('2')
sleep(1)
pyautogui.click(0.215*screen_width, 0)
sleep(1)
pyautogui.click(0.215*screen_width, 0.289*screen_height)
sleep(1)
ref_image = pyautogui.locateOnScreen('honing_in_pic.png')
x, y = pyautogui.center(ref_image)  # Divide by factor of 2
x, y = x/2, y/2                     # due to retina display bug


pyautogui.click(x+(0.069*screen_width), (y+0.039*screen_height))
pyautogui.click(x+(0.069*screen_width), (y+0.211*screen_height))
pyautogui.click(x+(0.153*screen_width), y+(0.361*screen_height))
sleep(5)    # Waiting for midi to connect
# Closing Midi Network and Studio Windows
pyautogui.click(x-(0.029*screen_width), y-(0.028*screen_height))
sleep(1)
with pyautogui.hold('command'):
    pyautogui.press('2')
# Minimize Audio MIDI Setup
sleep(1)
with pyautogui.hold('command'):
    pyautogui.press('m')
