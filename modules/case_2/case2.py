from funq.client import FunqClient
import pyautogui
from modules.settings import metods
import time

def checkEditorOpen():
    try:
        prReady = pyautogui.locateOnScreen("./modules/case_2/settings/images/analog_editor.png")
        return True
    except pyautogui.ImageNotFoundException:
        print("no image")
        return False

def run():
    try:    
        funq = FunqClient("127.0.0.1", 9999)
        pyautogui.rightClick("./modules/case_2/settings/images/new_device.png")
        metods.moveToScreen("./modules/case_2/settings/images/section_add.png")
        time.sleep(2)
        metods.moveToScreen("./modules/case_2/settings/images/new_signal.png")
        time.sleep(2)
        pyautogui.click("./modules/case_2/settings/images/analog.png")
        time.sleep(2)
        pyautogui.doubleClick("./modules/case_2/settings/images/open_editor.png")
        if checkEditorOpen == False:
            return False
    
        funq.widget(path=str("FrameworkWidget::DockAreaWidget::DeviceEditorWidget::DeviceEditorView::EditorPlacement::QTabWidget::qt_tabwidget_stackedwidget::AnalogEndpointEditor::AnalogEndpointEditorWidget::AnalogEndpointEditorView::sr:_:widgets:_:ExtendableTableView::qt_scrollarea_viewport::TableCellWidget-1::CheckBoxCellWidget")).click()

        time.sleep(0.25)
        pyautogui.doubleClick("./modules/case_2/settings/images/archive_value.png")
        pyautogui.write("1")
        pyautogui.doubleClick("./modules/case_2/settings/images/delta_value.png")
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.write("0")

        pyautogui.click("./modules/case_2/settings/images/apply.png")

        time.sleep(1)
        funq.widget(path=str('FrameworkWidget::DockAreaWidget::DeviceEditorWidget::qt_dockwidget_closebutton')).click()
        funq.widget(path=str('FrameworkWidget::FrameworkToolBar::WidgetActionContainer-34::QWidget::ToolBarActionWidget::QLabel')).click()
        return True
    except:
        print("case2: error")
        return False
    