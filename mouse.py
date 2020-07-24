import pyautogui
from time import sleep

# move the mouse to a corner to stop
pyautogui.FAILSAFE = True

try:
    # move to location
    pyautogui.moveTo(383, 651)

    # click forever
    while True:
        pyautogui.doubleClick()
        # sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
