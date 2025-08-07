import os
import shutil

def copy_files(source, destinaton):
    if not os.path.exists(destinaton):
        os.mkdir(destinaton)

    for file in os.listdir(source):
        start = os.path.join(source, file)
        end = os.path.join(destinaton, file)
        print (f" * Copying {start} -> {end}")

        if os.path.isfile(start):
            shutil.copy(start, end)
        else:
           copy_files(start, end)