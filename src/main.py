from textnode import *
import os
import shutil
from copystatic import copy_files
from generate import *

source = './static'
destinaton = './public'
from_path = './content/index.md'
template_path = './template.html'
destination_path = './public/index.html' 

def main():

    # Clears and/or creates public directory
    if os.path.exists(destinaton):
        shutil.rmtree(destinaton)
    os.mkdir(destinaton)

    copy_files(source, destinaton)
    generate_page(from_path, template_path, destination_path)


main()