from textnode import *
import os
import shutil
from copystatic import copy_files

source = './static'
destinaton = './public'

def main():

    # Clears and/or creates public directory
    if os.path.exists(destinaton):
        shutil.rmtree(destinaton)
    os.mkdir(destinaton)

    copy_files(source, destinaton)

main()