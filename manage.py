import os
import argparse
from app import main as application

parser = argparse.ArgumentParser(description='Command line interface to interact with the application')
parser.add_argument('main_command', help='Main command, list: run, createmigrations, or migrate')
parser.add_argument('-m', '--comment', help='Migrations script comment')

args = parser.parse_args()

if __name__ == '__main__':
    try:
        if args.main_command == 'runserver':
            application.run()
        elif args.main_command == 'createmigrations':
            os.system(f'alembic revision --autogenerate -m "{args.comment}"')
        elif args.main_command == 'migrate':
            os.system('alembic upgrade head')
        else:
            raise ValueError('The command must be either run or admin')
    except:
        raise Exception('Cannot run input command')