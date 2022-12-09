import pyautogui as auto
import subprocess
import time
import schedule
print("スタレンプログラムをセットしました。")
def alarm():
    subprocess.run('open -a LINE', shell=True)
    print(auto.position())
    time.sleep(5)
    auto.click(294,175)
    auto.click(762,594)
    for i in range(5):
        time.sleep(0.1)
        auto.click(864,235)
schedule.every().day.at("06:30").do(alarm)
while True:
    schedule.run_pending()
    time.sleep(60)
