
from funq.client import FunqClient
import pyautogui
from modules.settings import metods
import time

def run():
    try:
        funq = FunqClient("127.0.0.1", 9999)
        pyautogui.rightClick("./modules/case_3/settings/images/channel.png")
        metods.moveToScreen("./modules/case_3/settings/images/add.png")
        time.sleep(1)
        metods.moveToScreen("./modules/case_3/settings/images/patternProtokol.png")
        time.sleep(1)
        pyautogui.click("./modules/case_3/settings/images/masterPattern.png")
        pyautogui.rightClick("./modules/case_3/settings/images/pattern.png")
        pyautogui.click("./modules/case_3/settings/images/rename.png")
        #pyautogui.keyDown('shif')
        pyautogui.write("V\"R-104_")
        pyautogui.hotkey('alt','shift')
        pyautogui.write("Master")
        pyautogui.press('enter')
        return True
    except:
        print("case3: error")
        return False