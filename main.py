import time

from funq.client import FunqClient
from modules.settings import launch
from modules.autorization import autorization
from modules.isProccesing import processing
from modules.case_1 import case1 
from modules.case_2 import case2
from modules.case_3 import case3
from modules.case_4 import case4
from modules.case_5 import case5
from modules.case_6 import case6
from modules.case_7 import case7
from modules.case_8 import case8
from testReports import createReport


createReport.title()
                                                        
createReport.curAction(launch.launch(),"Запуск HMI")                                                                        #запуск HMI
time.sleep(3)                                                                         
createReport.curAction(autorization.autorization(),"Авторизация HMI")                                                       #авторизация HMI
createReport.curAction(processing.proccessing(), "Проверка процессинга")
                      
createReport.curCase(case1.run(),"Создание нового устройства с пользовательским именем")                               #выполнение кейсов              
createReport.curCase(case2.run(),"Добавление аналогового сигнала в устройство")                                                            
createReport.curCase(case3.run(),"Создание протокола с пользовательским именем")                                                                
createReport.curCase(case4.run(),"Добавление протокола в устройство")                                                      
createReport.curCase(case5.run(),"Создание технологического класса с пользовательским именем, добавление слотов состояния") 
createReport.curCase(case6.run(),"Создание объекта с пользовательским именем, привязка сигнала к объекту")
createReport.curCase(case7.run(),"Создание мнемосхемы с пользовательским именем. Расположение графических элементов на мнемосхеме. Привязка объекта к графическому элементу ") 
createReport.curCase(case8.run(),"Настройка параметров протокола и эмуляция поступления значений аналогового сигнала")

createReport.downTitle()
createReport.saveReport("./testReports/reports/")