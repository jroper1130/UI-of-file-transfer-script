#drill6

import datetime
import os
import shutil

src = "C:/Users/warbe/Desktop/a/"
des = "C:/Users/warbe/Desktop/b/"

def f_transfer():
    for root,dirs,files in os.walk(src):
        for file_name in files:
            now = datetime.datetime.now()
            before = now - datetime.timedelta(hours=24)
            files = os.path.join(src, file_name)
            mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(files))
            if mod_time > before:
                shutil.move(os.path.join(src, file_name), des)
#f_transfer()
