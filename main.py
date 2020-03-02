from parser import Parser
from db_updater import update
import time

if __name__ == '__main__':
    parser = Parser()
    while(True):
        update(parser.parse())
        print('Update')
        time.sleep(360)
