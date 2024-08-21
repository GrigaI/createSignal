from funq.client import FunqClient
import pyautogui
from modules.settings import metods
import time

def run():
    try:
        funq = FunqClient("127.0.0.1", 9999)
        funq.widget(path='FrameworkWidget::FrameworkToolBar::WidgetActionContainer-18::QWidget::ToolBarActionWidget::QLabel').click()
        funq.widget(path='FrameworkWidget::DockAreaWidget::DockAreaLayout::QSplitter::QSplitter::QScrollArea-1::qt_scrollarea_viewport::sr:_:widgets:_:DockAreaItemLayout::DockAreaSplitterWidget::QWidget::ObjectTreeToolWidget::sr:_:objecttree:_:ObjectTreeView::ObjectTreeToolBar::QToolButton').click()

        funq.widget(path='sr:_:objecttree:_:ObjectTreeAddItemWidget::ComboBoxWidget::QComboBox').set_current_text(text='ТехКласс_Нового устройства')
        funq.widget(path='sr:_:objecttree:_:ObjectTreeAddItemWidget::ComboBoxWidget-1::QComboBox::QLineEdit').set_properties(text='Объект_Нового устройства')
        funq.widget(path='sr:_:objecttree:_:ObjectTreeAddItemWidget::QDialogButtonBox::QPushButton').click()
        metods.allSave()
        time.sleep(2)
        pyautogui.doubleClick("./modules/case_6/settings/images/dcObject.png")
        metods.moveToScreen("./modules/case_6/settings/images/scroll_tree.png")
        pyautogui.scroll(15)
        location = pyautogui.locateCenterOnScreen("./modules/case_6/settings/images/source.png")
        print(location)
        x = location[0]
        y = location[1]
        print(x,y)
        metods.moveToScreen("./modules/case_6/settings/images/analog_channel.png")
        pyautogui.dragTo(x, y, 3, button='left')
        metods.allSave()
        funq.widget(path='FrameworkWidget::DockAreaWidget::ObjectSlotEditorWidget::qt_dockwidget_closebutton').click()
        funq.widget(path="FrameworkWidget::DockAreaWidget::DockAreaLayout::QSplitter::QSplitter::QScrollArea-1::qt_scrollarea_viewport::sr:_:widgets:_:DockAreaItemLayout::DockAreaSplitterWidget::QWidget::ObjectTreeToolWidget::qt_dockwidget_closebutton").click()
        funq.widget(path="FrameworkWidget::DockAreaWidget::DockAreaLayout::QSplitter::QSplitter::QScrollArea-1::qt_scrollarea_viewport::sr:_:widgets:_:DockAreaItemLayout::DockAreaSplitterWidget::QWidget::SystemTreeWidget::qt_dockwidget_closebutton").click()
        return True
    except:
        print("case6: error")
        return False


