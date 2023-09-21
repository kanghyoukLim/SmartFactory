import sys
import numpy as np
from myinfo import ID, PW

def py_version():
    print("파이썬 버전: " + sys.version)

class PyClass:
    def __init__(self, num=1):
        self.num = num
        print("클래스 객체 생성 : init 함수")

    def add(self):
        result = 0
        for n in range(1, self.num+1):
            result += n
        return result

    def multiply(self):
        result = 1
        for n in range(1, self.num+1):
            result *= n
        return result

if __name__ == "__main__":
    key = 'erp'
    print('id:'+ ID[key])
    print('password:', PW[key])

    print(py_version.__doc__)
    py_version()
    print(dir(sys))

    print(PyClass.__doc__)
    print(dir(PyClass))
    a = PyClass(10)
    #Python 2버전
    print('1에서 %d까지의 합: %s' % (a.num, format(a.add(), ",")))
    # Python 3버전
    print('1에서 {}까지의 곱:{:,}'.format(a.num, a.multiply()))

