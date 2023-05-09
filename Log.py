import logging
import os

dir_path = os.path.dirname(os.path.realpath(__file__)) + '\log.txt'
logging.basicConfig(filename=dir_path,level=logging.DEBUG)
