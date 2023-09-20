import sys
import numpy as np
from myinfo import ID, PW

def py_version():
    print("파이썬 버전:" +sys.version)

class PyClass():
    def __init__(self, num=1):
        self.num = num
        print("클래스 객체 생성")

    def add(self):
        result = 0
        for n in range(1,self.num+1):
            result += n
        return result

    def multiply(self):
        # result = 1
        for n in range(1,self.num+1):
            result *= n
        return result

if __name__=="__main__":
    key
