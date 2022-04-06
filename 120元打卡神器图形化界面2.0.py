import tkinter as tk
import threading
import pyautogui
import time,datetime
import schedule
import os

    
    
 

    
def run_am():
    l.config(text = '模式： ' + var.get()) #config()给Label进行属性设置，这里获取当前选项的value进行绑定
    def am():
        print("签到开始啦")
        os.system('"C:\Program Files\Google\Chrome\Application\chrome.exe" https://www.baidu.com/')
        time.sleep(5)
        pyautogui.click(x=282, y=321)
        time.sleep(3)
        pyautogui.click(x=1152, y=723)
        time.sleep(1)
        print("你守住了你的120")
        quit()
    schedule.every().day.at("02:27:50").do(am)

def run_pm():
    l.config(text = '模式： ' + var.get()) #config()给Label进行属性设置，这里获取当前选项的value进行绑定
    def pm():
        print("签出开始啦")
        os.system('"C:\Program Files\Google\Chrome\Application\chrome.exe" https://www.baidu.com/')
        time.sleep(5)
        pyautogui.click(x=319, y=350)
        time.sleep(3)
        pyautogui.click(x=1129, y=699)
        time.sleep(1)
        print("你守住了你的120")
        quit()
    schedule.every().day.at("01:22:51").do(pm) 

    

window = tk.Tk()
window.title('打卡神器')
window.geometry('400x400')

var = tk.StringVar()
l = tk.Label(window, text = '请选择你想要的模式', bg = '#1E6FFF', font = ('Arial', 12), width = 25, height = 5)
l.pack()


    

# RadioButton中variable将所选中的value值绑定到var变量中，方便在点击后，给label进行绑定
r1 = tk.Radiobutton(window, text = '签到', variable = var, value = '签到\n打卡程序已运行，请关闭窗口吧~', command =run_am)
r1.pack()


r2 = tk.Radiobutton(window, text = '签出', variable = var, value = '签出\n打卡程序已运行，请关闭窗口~', command = run_pm)
r2.pack()



window.mainloop()

while True:
    schedule.run_pending()
    time.sleep(1)
# if you want run this, type "python3 Mouse_click.py"