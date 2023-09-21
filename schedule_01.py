import sys
import numpy as np

class Item():
    def __init__(self, name, LT, inven, S_inven, order):
        self.name=name
        self.LT=LT
        self.inven=inven
        self.S_inven=S_inven
        self.order=order
        print(f'{name}객체를 완성했습니다.')

A=Item('part_A',2,50,0,1250)
print(A.name,A.LT,A.inven,A.S_inven,A.order)
