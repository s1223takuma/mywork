import pyautogui as auto
import subprocess
import time
import schedule
print("スタレンプログラムをセットしました。")
subprocess.run('open -a LINE', shell=True)
print(auto.position())
time.sleep(3)
auto.click(1650, 1028)
for i in range(10):
    time.sleep(0.1)
    auto.click(133,233)