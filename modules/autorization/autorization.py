import time
from funq.client import FunqClient

def autorization():
    try:
        funq = FunqClient("127.0.0.1", 9999)

        login = "Инженер"
        password = "1234567890"
        funq.widget(path=str("UserAuthorizationDialog::TextEditWidget")).set_properties(text=login)
        funq.widget(path=str("UserAuthorizationDialog::TextEditWidget-1")).set_properties(text=(password))
            
        funq.widget(path=str("UserAuthorizationDialog::QDialogButtonBox::QPushButton")).click()
        return True
    except:
        print("autorization: error")
        return False