# cors 10 video
# virtualenv - create and active
# ------------------
import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)