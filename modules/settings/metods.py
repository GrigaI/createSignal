import pyautogui
from datetime import datetime, timedelta
from funq.client import FunqClient

def moveToScreen(pathS):
    buttonLocation = pyautogui.locateOnScreen(pathS)

    buttonPoint = pyautogui.center(buttonLocation)
    print(buttonPoint)
    pyautogui.moveTo(buttonPoint)

def waitOpenOfIMG(imgName):
    now = datetime.now() 
    finish_time = now + timedelta(seconds=60)
    finish_time = finish_time.strftime("%H:%M:%S")
    while True:
        curTime = datetime.now().strftime("%H:%M:%S")
        if finish_time < curTime:
            return False
        else:
            try:
                prReady = pyautogui.locateOnScreen(imgName)
                return True
            except pyautogui.ImageNotFoundException:
                print("no image")
                continue
            
def allSave():
    funq = FunqClient("127.0.0.1", 9999) 
    funq.widget(path=str('FrameworkWidget::FrameworkToolBar::WidgetActionContainer-34::QWidget::ToolBarActionWidget::QLabel')).click()