from funq.client import FunqClient
import pyautogui
from modules.settings import metods
import time

def run():
    try:
        funq = FunqClient("127.0.0.1", 9999)
        pyautogui.doubleClick("./modules/case_4/settings/images/new_device.png")
        funq.widget(path=str("FrameworkWidget::FrameworkToolBar::WidgetActionContainer-19::QWidget::ToolBarActionWidget")).click()
        time.sleep(1)
        metods.moveToScreen("./modules/case_4/settings/images/window.png")
        pyautogui.dragTo(500, 0, 4, button='left')
        time.sleep(3)
        pyautogui.click("./modules/case_4/settings/images/section_pattern.png")
        time.sleep(1)
        metods.moveToScreen("./modules/case_4/settings/images/channel.png")
        time.sleep(1)
        pyautogui.dragTo(600, 300, 4, button='left')
        time.sleep(1)
        pyautogui.click("./modules/case_4/settings/images/saveBtn.png")
        funq.widget(path="FrameworkWidget::DockAreaWidget::DeviceEditorWidget::qt_dockwidget_closebutton").click()
        funq.widget(path=str('FrameworkWidget::FrameworkToolBar::WidgetActionContainer-34::QWidget::ToolBarActionWidget::QLabel')).click()
        return True
    except:
        print("case4: error")
        return False
    