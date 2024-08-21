from datetime import datetime
import pdfkit 
#PATH_WKHTMLTOPDF = '/opt/bin/wkhtmltopdf'
#PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf=PATH_WKHTMLTOPDF)


n=1
htmlStr =""

def curTime():
    return datetime.now().strftime("%Y-%m-%d %H-%M-%S")

def title():
    global htmlStr
    htmlStr += "<meta http-equiv='Content-type' content='text/html; charset=utf-8' />"
    htmlStr +="<h1 align='center'>Тест: Заведения сигналов.</h1>"
    htmlStr += "<h2 align='center'>Количество кейсов: 5</h2>"
    htmlStr += "<h2 align='center'>Дата и время начала теста: "+ str(curTime()) +"</h2>"
    htmlStr += "<h2 align='center'>===================================================================</h2>"
    

def curAction(isSuccess, caseName):
    global htmlStr, n
    success = "<span style='color: #008000;'> [Успешно]</span>"
    unsuccess = "<span style='color: #800000;'> [Ошибка]</span>"
    
    if isSuccess:
        htmlStr += "<h3>" +str(n) + ". " + str(caseName) + str(success) + "</h3>"
    else:
        htmlStr += "<h3>" +str(n) + ". " + str(caseName) + str(unsuccess) + "</h3>"
        
    n += 1
    
def curCase(isSuccess, caseName):
    global htmlStr, n
    success = "<span style='color: #008000;'> [Успешно]</span>"
    unsuccess = "<span style='color: #800000;'> [Ошибка]</span>"
    
    if isSuccess:
        htmlStr += "<h3>" +str(n) + ". Кейс: " + str(caseName) + str(success) + "</h3>"
    else:
        htmlStr += "<h3>" +str(n) + ". Кейс: " + str(caseName) + str(unsuccess) + "</h3>"
        
    n += 1

    
def downTitle():
    global htmlStr
    htmlStr += "<h2 align='center'>===================================================================</h2>"
    htmlStr +="<h2 align='center'>Дата и время завершения теста: "+ str(curTime())+ "</h2>"
    

    
def saveReport(pathF):
    
    pdfkit.from_string(htmlStr,str(pathF)+"report_"+curTime()+".pdf",verbose=True)
    
    
