import pyautogui
import time

terminalString = "cd "
terminalString += "&& cd /home/user/funq/server/funq_server/ "
terminalString += "&& export LD_LIBRARY_PATH=/usr/lib/scada-r/hmi-engineer "
terminalString += "&& python3 runner.py --host 0.0.0.0 --port 9999 /usr/lib/scada-r/hmi-engineer/hmi-engineer"

def launch():
    try:
        pyautogui.hotkey('alt','t')
        time.sleep(1)
        pyautogui.write(terminalString)
        pyautogui.press('enter')
        return True
    except:
        print("launch: error")
        return False