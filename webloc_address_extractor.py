#!/usr/bin/python3
# -*- coding: ascii -*-

"""show address contained in safari bookmark files"""

import glob
from os import path
import sys
import xml.etree.ElementTree as ET
import plistlib

comment_character = "# "

def process_folder(folder_name):
    """Examine folder for .webloc files and print contained URLs to stdout"""
    for filename in glob.glob(folder_name + "/*.webloc"):
        with open(filename,'rb') as plf:
            results = plistlib.load(plf)
            print("# {filename}\n{address}\n".format(filename=filename,address=results['URL']))


def main():
    """testing"""
    for i, arg in enumerate(sys.argv):
        if (i>0):
            process_folder(arg)

if __name__ == '__main__':
    main()
