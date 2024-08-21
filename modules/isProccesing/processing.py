from funq.client import FunqClient
import time

def proccessing():
    time.sleep(5)
    funq = FunqClient("127.0.0.1", 9999)
    try:
        print(funq.widget(path="FrameworkWidget::FrameworkToolBar::WidgetActionContainer-32::QWidget::DateTimeWidget::NormalIlluminatedTimeLabel").properties())
        return True
    except:
        print("error")
        return False

