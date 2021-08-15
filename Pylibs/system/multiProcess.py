# -*- coding: utf-8 -*-
import multiprocessing
import os
import random
import time

class Singleton2(object):
    time = time.ctime()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
            print('main test\n')
        return cls._instance


def test(b):
    singleton = Singleton2()
    print(b, id(singleton), singleton.time, os.getpid())


if __name__ == '__main__':
    pool = multiprocessing.Pool(3)
    for i in range(1):
        pool.map(test, [1, 2, 3, 4, 5, 6])
    pool.close()
    pool.join()
