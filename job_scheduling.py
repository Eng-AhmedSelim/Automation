# cors 10 video
# virtualenv - create and active
# step One run Code pip install schedule
# ------------------
import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
