from funq.client import FunqClient
from funq.models import TabBar, TableView
import pyautogui
from modules.settings import metods
import time

def run():
    try:
        funq = FunqClient("127.0.0.1", 9999)
        funq.widget(path="FrameworkWidget::FrameworkToolBar::WidgetActionContainer-19::QWidget::ToolBarActionWidget::QLabel").click()
        time.sleep(0.5)
        pyautogui.doubleClick("./modules/case_8/settings/images/data.png")
        time.sleep(0.5)
        pyautogui.doubleClick("./modules/case_8/settings/images/channels.png")
        time.sleep(0.5)
        pyautogui.doubleClick("./modules/case_8/settings/images/mak.png")
        time.sleep(0.5)
        pyautogui.doubleClick("./modules/case_8/settings/images/port.png")
        pyautogui.press('backspace')
        pyautogui.write("2507")
        pyautogui.press('enter')
        funq.widget(path="FrameworkWidget::DockAreaWidget::ProtocolEditorWidget::ProtocolEditorView::sr:_:widgets:_:ControlElementWidget::QPushButton").click()
        metods.allSave()
        TabBar = funq.widget(path="FrameworkWidget::DockAreaWidget::ProtocolEditorWidget::ProtocolEditorView::EditorPlacement::QTabWidget::qt_tabwidget_tabbar")
        TabBar.set_current_tab(1)
        pyautogui.click("./modules/case_8/settings/images/adres_IOA.png")
        pyautogui.write("1000")
        pyautogui.press('enter')
        funq.widget(path="FrameworkWidget::DockAreaWidget::ProtocolEditorWidget::ProtocolEditorView::sr:_:widgets:_:ControlElementWidget::QPushButton").click()
        metods.allSave()
        funq.widget(path="FrameworkWidget::DockAreaWidget::ProtocolEditorWidget::qt_dockwidget_closebutton").click()
        pyautogui.hotkey('alt','shift')
        pyautogui.hotkey('alt','t')
        time.sleep(1)
        pyautogui.write("cd ./iectest-2507/ && sudo ./iectest-2507.sh")
        pyautogui.press('enter')
        pyautogui.write("12345678")
        pyautogui.press('enter')
        pyautogui.click("./modules/case_8/settings/images/scadar.png")
        time.sleep(1)
        funq.widget(path="FrameworkWidget::DockAreaWidget::DockAreaLayout::QSplitter::QSplitter::QSplitter::QScrollArea::qt_scrollarea_viewport::sr:_:widgets:_:DockAreaItemLayout::DockAreaSplitterWidget::QWidget::SceneEditorWidget::sr:_:sceneeditor:_:EditorView::SceneEditorToolBar::QToolButton").click()
        pyautogui.moveTo(980,540)
        pyautogui.keyDown('ctrl')
        pyautogui.scroll(-6)
        pyautogui.keyUp('ctrl')
        return True
    except:
        print("case8: error")
        return False