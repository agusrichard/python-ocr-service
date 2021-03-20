import os
import argparse
from app import main as application

parser = argparse.ArgumentParser(description='Command line interface to interact with the application')
parser.add_argument('main_command', help='Main command, list: run')

args = parser.parse_args()

if __name__ == '__main__':
    try:
        if args.main_command == 'runserver':
            application.run()
        else:
            raise ValueError('The command must be either run or admin')
    except:
        raise Exception('Cannot run input command')