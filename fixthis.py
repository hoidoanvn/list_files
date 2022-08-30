import os
import glob
import shutil

Dowload = r"C:\Users\Admin\Downloads"
#Dowload = "folder"

pdf_folder = "pdf folder"
app_folder = "app folder"
rar_folder = "rar folder"


for single_folder_name in [pdf_folder, app_folder, rar_folder]:
    des_dir = os.path.join(Dowload, single_folder_name)
    if not os.path.exists(des_dir):
        os.mkdir(des_dir)
    # else:
        # shutil.rmtree(des_dir)


all_files: list = glob.glob(os.path.join(Dowload, "*"))


for single_file in all_files:
    if os.path.isdir(single_file):
        continue
    extension = os.path.splitext(single_file)[-1]
    if extension == ".pdf":
        shutil.move(single_file, os.path.join(Dowload, pdf_folder))
    elif extension == ".exe":
        shutil.move(single_file, os.path.join(Dowload, app_folder))
    elif extension == ".zip" or extension == ".rar" or extension == ".7z":
        shutil.move(single_file, os.path.join(Dowload, rar_folder))
    else:
        continue
    print("Moved", single_file)
