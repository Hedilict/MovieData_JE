import time

from softwareproperties.gtk.DialogMirror import cmp

from user.key_parameter import time_advance


def open_time(start_time):
    start_dtime = time.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    start_stime = time.mktime(start_dtime)
    open_stime = start_stime - time_advance
    open_dtime = time.localtime(open_stime)
    return time.strftime('%Y-%m-%d %H:%M:%S', open_dtime)


if __name__ == '__main__':
    c1 = '2015-12-05 00:18:07'
    c2 = open_time(c1)
    res = cmp(c1, c2)
    print(c2)
    print(res)
