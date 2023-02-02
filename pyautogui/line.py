import pyautogui as auto
import subprocess
import time
import schedule
print("スタレンプログラムをセットしました。")
subprocess.run('open -a LINE', shell=True)
print(auto.position())
time.sleep(10)
auto.click(294,175)
auto.click(762,594)
for i in range(10):
    time.sleep(0.1)
    auto.click(864,235)