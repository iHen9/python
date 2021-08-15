# -*- coding: utf-8 -*-
import _thread, threading, time
import ctypes


class Thread1(object):
    """
    强制推退出 父线程终止
    """

    def __init__(self):
        self.status = True

    def test(self):
        times = 10
        while times:
            print(f'{self.__class__} is running, lefts {times} times!')
            time.sleep(1)
            times -= 1

    def run(self):
        _thread.start_new_thread(self.test, ())
        while True:
            time.sleep(1)
            if not self.status:
                break

    def start(self):
        _thread.start_new_thread(self.run, ())

    def stop(self):
        self.status = False
        print(f'{self.__class__} is killed, no result !')


class Thread2(threading.Thread):
    """
    强制推退出 传递异常
    """

    def run(self, times=10):
        while times:
            print(f'{self.__class__} is running, lefts {times} times!')
            time.sleep(1)
            times -= 1

    def get_id(self):
        if hasattr(self, "_thread_id"):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def stop(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
        print(f'{self.__class__} is killed ! ,has result')


class Thread3(threading.Thread):
    """
    通知退出 信号传递
    """

    def __init__(self):
        self.run_status = True
        super().__init__()

    def run(self):
        times = 10
        while times:
            print(f'{self.__class__} is running, lefts {times} times!')
            time.sleep(1)
            times -= 1
            if not self.run_status:
                break

    def stop(self):
        self.run_status = False
        self.join()
        print(f'{self.__class__} is stopped !, has result')


class Thread4():
    """
    通知退出 函数传递
    """

    def __init__(self):
        self.run_status = True
        super().__init__()

    def run(self, get_status):
        times = 10
        while times:
            print(f'{self.__class__} is running, lefts {times} times!')
            time.sleep(1)
            times -= 1
            if not get_status():
                break

    def start(self):
        _thread.start_new_thread(self.run, (lambda: self.run_status,))

    def stop(self):
        self.run_status = False
        print(f'{self.__class__} is stopped !, no result')


def test():
    thread = Thread2()
    thread.start()
    time.sleep(5)
    thread.stop()


if __name__ == '__main__':
    test()
