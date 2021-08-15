# -*- coding: utf-8 -*-
import traceback


class ExceptionCapture(object):

    def __init__(self, exception_list: list, is_raise=False):
        self.exception_list = exception_list
        self.is_raise = is_raise

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.is_raise:
            self.exception_list.append(traceback.format_exception(exc_type, exc_val, exc_tb))
            return True
        else:
            if self.exception_list:
                info = ''
                for i in self.exception_list:
                    info += (str(i) + '\n')
                raise Exception(info)
