# -*- coding: utf-8 -*-


class Observer(object):

    def __init__(self, name):
        self.name = name

    def update(self, msg):
        print(self.name, msg)


class Subject(object):

    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify(self, msg):
        for observer in self.observers:
            observer.update(msg)


def test():
    a = Observer('a')
    b = Observer('b')
    rain = Subject()
    rain.add_observer(a)
    rain.add_observer(b)
    rain.notify('rain')


if __name__ == '__main__':
    test()
    complex