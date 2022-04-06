# V_2.0 此版本升级了图形化界面  
-通过此工具可自动进行签到打卡。
**需要满足条件：**  
1.电脑处于解锁界面  
2.python环境  
3.安装库  
import tkinter as tk  
import threading  
import pyautogui  
import time,datetime  
import schedule  
import os  
**使用方法： ** 
1.设置好打卡网站  
<img width="289" alt="image" src="https://user-images.githubusercontent.com/59388781/161877828-84d2e00c-dfbd-4368-a7c2-6ddc18dd959e.png">。  
2.设置好坐标<img width="1024" alt="image" src="https://user-images.githubusercontent.com/59388781/161877953-f274b07e-47b5-418d-a31e-1eaf6b45ae57.png">
3.设置打卡时间。<img width="987" alt="image" src="https://user-images.githubusercontent.com/59388781/161878033-d9e7bf66-01b3-4e29-9e42-0da36a744aa7.png">  
4.运行程序，将会弹出窗口。    
5.点击签到或签出。<img width="400" alt="image" src="https://user-images.githubusercontent.com/59388781/161878432-1c18b5ef-2201-4290-b3f3-e54412be5b60.png">  
6.选择后关闭窗口<img width="400" alt="image" src="https://user-images.githubusercontent.com/59388781/161878524-59fcbf2f-3222-4bc1-a00c-9f1619c12641.png">
 *非关闭程序    
软件将会在后台运行，执行完打卡后自动关闭
