# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
Hello World, but with more meat.
"""
import _thread
import multiprocessing
import sys
import time

import wx
# from future.backports.test.ssl_servers \
import threading

frm = None


class HelloFrame(wx.Frame):
    """
    A Frame that says Hello World
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(HelloFrame, self).__init__(*args, **kw)
        self.process = None
        self.button()
        self.m_button1.Bind(wx.EVT_LEFT_DOWN, self.test_manager)

    def button(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.m_button1 = wx.Button(self, wx.ID_ANY, u"start", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.m_button1, 0, wx.ALL, 5)
        self.SetSizer(sizer)
        self.Layout()

    def test_manager(self, event):
        self.m_button1.Enable(False)
        if self.m_button1.GetLabel() == u"start":
            if self.process is None:
                _thread.start_new_thread(self.run, ())
                # self.process = threading.Thread(target=self.run())
                # self.process.daemon = True
                # self.process.start()
            self.m_button1.SetLabel(u"stop")
        elif self.m_button1.GetLabel() == u"stop":
            print('process is %s' % self.process.__class__)
            # if self.process:
            self.stop()
            self.m_button1.SetLabel(u"start")
        self.m_button1.Enable(True)

    def test(self, times=5):
        while times:
            time.sleep(1)
            times -= 1
            print("times left is %s" % times)

    def run(self):
        self.status = True
        _thread.start_new_thread(self.test, ())
        while True:
            time.sleep(1)
            if not self.status:
                sys.exit()

    def stop(self):
        self.status = False
        # print(f'{self.process.__class__()} is killed, no result !')
        # print("%s" % self.process)
        # self.process = None


def main():
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    global frm
    frm = HelloFrame(None, title='Hello World')
    frm.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
