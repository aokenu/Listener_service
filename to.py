import time
import os
import os
import shutil



def move1(port):
    # Getting the path of the file
    f_path = f"C:/python_work/changes/port/{port}.csv"
    # Obtaining the creation time (in seconds) of the file/folder (datatype=int)
    t = os.path.getctime(f_path)
    # Converting the time to an epoch string(the output timestamp string would be recognizable by strptime() withoutformat quantifers)
    t_str = time.ctime(t)
    # Converting the string to a time object
    t_obj = time.strptime(t_str)
    # Transforming the time object to a timestamp
    # of ISO 8601 format
    form_t = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
    