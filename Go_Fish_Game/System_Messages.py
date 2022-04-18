from datetime import datetime


def print_info(message):
    print(f"\033[0;36;1m[{datetime.now().strftime('%H:%M:%S')} INFO]: {message}\033[0;0m")


def print_warn(message):
    print(f"\033[0;33;1m[{datetime.now().strftime('%H:%M:%S')} WARN]: {message}\033[0;0m")


def print_error(message):
    print(f"\033[0;31;1m[{datetime.now().strftime('%H:%M:%S')} ERROR]: {message}\033[0;0m")
