import pyautogui as auto
import subprocess
import datetime
import time
import schedule
def alarm():
    subprocess.run('open -a LINE', shell=True)
    print(auto.position())
    time.sleep(5)
    auto.click(262,168)
    auto.click(716,653)
    for i in range(10):
        time.sleep(0.5)
        auto.click(808,222)
schedule.every().day.at("03:29").do(alarm)
while True:
    schedule.run_pending()
    time.sleep(60)