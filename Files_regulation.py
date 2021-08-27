import time
import schedule
import os
import shutil

user_pc = os.getlogin()
path_publice = input('inter path: ')
os.chdir(path_publice)
path_pdf_doc = f'C:/Users/{user_pc}/Downloads/1-office'
path_Pictures = f'C:/Users/{user_pc}/Downloads/2-Pictures'
path_compressed = f'C:/Users/{user_pc}/Downloads/3-compressed'
path_video = f'C:/Users/{user_pc}/Downloads/4-video'
path_program = f'C:/Users/{user_pc}/Downloads/5-programs'


def job():  # function File regulation
    for file in os.listdir():
        name_file, file_ext = os.path.splitext(file)  # Divide the file name into two parts, name and extension
        # condition
        if any([file_ext == '.png', file_ext == '.jpg', file_ext == '.jpeg']):
            chek1 = os.path.exists(path_Pictures)  # Confirm the existence of the path
            if chek1:
                shutil.move(file, path_Pictures)  # Move the file to the path
                print('done')
            else:
                os.mkdir('2-Pictures')
                shutil.move(file, path_Pictures)
                print('done')
        # condition files word
        elif any([file_ext == '.docx', file_ext == '.pdf', file_ext == '.xlsx']):
            chek2 = os.path.exists(path_pdf_doc)
            if chek2:
                shutil.move(file, path_pdf_doc)
                print('done')
            else:
                os.mkdir('1-office')
                shutil.move(file, path_pdf_doc)
                print('done')

        elif any([file_ext == '.zip', file_ext == '.rar']):
            chek3 = os.path.exists(path_compressed)
            if chek3:
                shutil.move(file, path_compressed)
                print('done')
            else:
                os.mkdir('3-compressed')
                shutil.move(file, path_compressed)
                print('done')

        elif any([file_ext == '.mp4', file_ext == '.m4v', file_ext == '.m4v', file_ext == '.mkv']):
            chek4 = os.path.exists(path_video)
            if chek4:
                shutil.move(file, path_video)
                print('done')
            else:
                os.mkdir('4-video')
                shutil.move(file, path_video)
                print('done')

        elif any([file_ext == '.exe', file_ext == '.iso']):
            chek5 = os.path.exists(path_program)
            if chek5:
                shutil.move(file, path_program)
                print('done')
            else:
                os.mkdir('5-programs')
                shutil.move(file, path_program)
                print('done')
        else:
            continue


schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

# C:/Users/Ahmed/Downloads
