# -*- coding: utf-8 -*-
import sys
import time
import traceback


def print_for_times(content, wait=2, time_out=4):
    while time_out > 0:
        print(content + 'a')
        time.sleep(wait)
        time_out -= wait


def test():
    try:
        print_for_times(1)
    except Exception as e:
        # exc_type, exc_value, exc_tb = sys.exc_info()
        # traceback.print_exception(exc_type, exc_value, exc_tb)
        traceback.print_last()

        print('Exception: ', e)
        # raise


if __name__ == '__main__':
    test()
