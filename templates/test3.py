# coding=utf-8

import Tkinter


def handler(a, b, c):
    '''''事件处理函数'''
    print "handler", a, b, c


if __name__ == '__main__':
    root = Tkinter.Tk()
    # 通过中介函数handlerAdapotor进行command设置
    btn = Tkinter.Button(text=u'按钮', command=lambda: handler(a=1, b=2, c=3))
    btn.pack()
    root.mainloop()