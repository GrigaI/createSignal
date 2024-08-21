from funq.client import FunqClient
import pyautogui
from modules.settings import metods
import time


def run():
    try:
        metods.waitOpenOfIMG("./modules/case_1/settings/images/screenReady.png")
        funq = FunqClient("127.0.0.1", 9999)
        funq.widget(path=str("FrameworkWidget::FrameworkToolBar::WidgetActionContainer-19::QWidget::ToolBarActionWidget")).click()
        time.sleep(1.2)
        pyautogui.doubleClick("./modules/case_1/settings/images/section_data.png")

        pyautogui.rightClick("./modules/case_1/settings/images/section_device.png")
        #time.sleep(5.0)
        metods.moveToScreen("./modules/case_1/settings/images/section_add.png")
        time.sleep(1)
        pyautogui.click("./modules/case_1/settings/images/device.png")
        #time.sleep(2)
        pyautogui.rightClick("./modules/case_1/settings/images/device2.png")
        #time.sleep(2)
        pyautogui.hotkey('shift','alt')
        pyautogui.click("./modules/case_1/settings/images/rename.png")
        
        #time.sleep(2)
        #pyautogui.write("Новое устройство")
        pyautogui.write("Yjdjt ecnhjqcndj") #Новое устровйство 
        #time.sleep(2)
        pyautogui.press('enter')
        return True
    except:
        print("case1: error")
        return False