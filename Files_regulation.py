import time
import schedule
import os
import shutil
from win10toast import ToastNotifier

toaster = ToastNotifier()
current_dir = os.path.dirname(os.path.realpath(__file__))


def photo():
    if not os.path.exists("Photo_file"):
        os.mkdir("Photo_file")
    shutil.copy(file, "Photo_file")
    os.remove(file)


def doc():
    if not os.path.exists("Doc_file"):
        os.mkdir("Doc_file")
    shutil.copy(file, "Doc_file")
    os.remove(file)


def archive():
    if not os.path.exists("Archive"):
        os.mkdir("Archive")
    shutil.copy(file, "Archive")
    os.remove(file)


def app():
    if not os.path.exists("App_File"):
        os.mkdir("App_File")
    shutil.copy(file, "App_File")
    os.remove(file)


def web_file():
    if not os.path.exists("Web_File"):
        os.mkdir("Web_File")
    shutil.copy(file, "Web_File")
    os.remove(file)


def video():
    if not os.path.exists("Video_File"):
        os.mkdir("Video_File")
    shutil.copy(file, "Video_File")
    os.remove(file)


def check():
    global file
    for file in os.listdir(current_dir):
        if file.endswith(('.mp4', '.m4v', '.m4v', '.mkv')):
            video()
        elif file.endswith(('.html', '.htm')):
            web_file()
        elif file.endswith(('.exe', '.iso')):
            app()
        elif file.endswith(('.zip', '.rar')):
            archive()
        elif file.endswith(('.docx', '.pdf', '.xlsx', 'xls', 'doc')):
            doc()

        elif file.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            photo()
    toaster.show_toast("Hello Name", "files have been arranged", duration=5)


schedule.every(10).seconds.do(check)
while True:
    schedule.run_pending()
    time.sleep(1)

