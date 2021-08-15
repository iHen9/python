# -*- coding: utf-8 -*-
import random


class Singleton1(object):
    _instance = None
    time = random.random()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class Singleton2(object):
    time = random.random()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance


def test():
    s1 = Singleton1()
    s1.name = 123
    print(id(s1), s1.__dict__, s1.time)
    s2 = Singleton1()
    print(id(s2), s2.__dict__, s2.time)


if __name__ == '__main__':
    test()
