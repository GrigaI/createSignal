from funq.client import FunqClient
import pyautogui
from modules.settings import metods
import time

def run():
    try:
        funq = FunqClient("127.0.0.1", 9999)
        pyautogui.doubleClick("./modules/case_5/settings/images/help.png")
        pyautogui.rightClick("./modules/case_5/settings/images/technologies_classes.png")
        metods.moveToScreen("./modules/case_5/settings/images/add.png")
        time.sleep(1)
        pyautogui.click("./modules/case_5/settings/images/class.png")
        time.sleep(1)
        pyautogui.rightClick("./modules/case_5/settings/images/section_class.png")
        time.sleep(2)
        pyautogui.click("./modules/case_5/settings/images/rename.png")
        pyautogui.hotkey('alt','shift')
        pyautogui.write("Nt[Rkfcc_Yjdjuj ecnhjqcndf")
        pyautogui.press('enter')
        metods.moveToScreen("./modules/case_5/settings/images/data.png")
        pyautogui.scroll(-10)
        pyautogui.doubleClick("./modules/case_5/settings/images/tech.png")
        time.sleep(1)
        pyautogui.click("./modules/case_5/settings/images/section_slots.png")
        pyautogui.doubleClick("./modules/case_5/settings/images/add_slot.png")
        for i in range (15):
            pyautogui.press('backspace')
        pyautogui.write("NB_1")
        pyautogui.click("./modules/case_5/settings/images/combo_box.png")
        pyautogui.click("/home/user/autotests/test_createSignals/modules/case_5/settings/images/analog.png")
        pyautogui.click("/home/user/autotests/test_createSignals/modules/case_5/settings/images/saveSlot.png")
        funq.widget(path="FrameworkWidget::DockAreaWidget::TechClassEditorWidget::qt_dockwidget_closebutton").click()
        funq.widget(path=str('FrameworkWidget::FrameworkToolBar::WidgetActionContainer-34::QWidget::ToolBarActionWidget::QLabel')).click()
        return True
    except:
        print("case5: error")
        return False