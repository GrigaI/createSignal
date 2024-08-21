from funq.client import FunqClient
import pyautogui
from modules.settings import metods
import time

def run():
    try:
        funq = FunqClient("127.0.0.1", 9999)
        funq.widget(path='FrameworkWidget::FrameworkToolBar::WidgetActionContainer-21::QWidget::ToolBarActionWidget::QLabel').click()
        time.sleep(0.5)
        pyautogui.rightClick("./modules/case_7/settings/images/treeView_rightClick.png")
        metods.moveToScreen("./modules/case_7/settings/images/add.png")
        time.sleep(1)
        pyautogui.click("./modules/case_7/settings/images/add_mnemoshem.png")
        pyautogui.rightClick("./modules/case_7/settings/images/new_mnemoshem.png")
        time.sleep(0.5)
        pyautogui.click("./modules/case_7/settings/images/rename.png")
        #pyautogui.hotkey('alt','shift')
        pyautogui.write("Dsdjl fyfkjujdjuj cbuyfkf")
        pyautogui.press('enter')
        metods.allSave()
        time.sleep(1)
        pyautogui.doubleClick("./modules/case_7/settings/images/dcklick_mnemoshem.png")
        funq.widget(path="FrameworkWidget::FrameworkToolBar::WidgetActionContainer-23::QWidget::ToolBarActionWidget::sr:_:widgets:_:ElidedLabel").click()
        funq.widget(path="FrameworkWidget::DockAreaWidget::DockAreaLayout::QSplitter::QSplitter"\
                        "::QScrollArea::qt_scrollarea_viewport::sr:_:widgets:_:DockAreaItemLayout::DockAreaSplitterWidget"\
                        "::QWidget::GraphicElementPaletteWidget::sr:_:graphicpalette:_:GraphicElementPaletteView::ToolBox"\
                        "::qt_scrollarea_viewport::ToolBoxContainer::QSplitter::ToolBoxWidget-2::ToolBoxHeaderWidget::QLabel-1").click()
        time.sleep(2)
        metods.moveToScreen("./modules/case_7/settings/images/channel_image.png")
        pyautogui.dragTo(980, 440, 3, button='left')
        metods.moveToScreen("./modules/case_7/settings/images/text_image.png")
        pyautogui.dragTo(980, 480, 3, button='left')
        pyautogui.rightClick(x=980,y=480)
        pyautogui.click("./modules/case_7/settings/images/propertyes.png")
        time.sleep(1)
        pyautogui.click("./modules/case_7/settings/images/propertyes_rename.png")
        pyautogui.press('backspace')
        pyautogui.write("NB")
        pyautogui.press('enter')
        metods.allSave()
        funq.widget(path="FrameworkWidget::FrameworkToolBar::WidgetActionContainer-18::QWidget::ToolBarActionWidget::sr:_:widgets:_:ElidedLabel").click()
        time.sleep(1)
        metods.moveToScreen("./modules/case_7/settings/images/object.png")
        pyautogui.dragTo(980, 350, 3, button='left')
        pyautogui.click("./modules/case_7/settings/images/change_slot.png")
        pyautogui.click("./modules/case_7/settings/images/TU1.png")
        pyautogui.doubleClick("./modules/case_7/settings/images/section_position.png")
        time.sleep(1)
        pyautogui.click("./modules/case_7/settings/images/position_value.png")
        for i in range (5):
            pyautogui.press('backspace')
        pyautogui.write("60")
        pyautogui.press('enter')   
        metods.allSave()
        return True
    except:
        print("case7: error")
        return False