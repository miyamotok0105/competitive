
#円周の長さ = 直径 × 円周率 
#円の面積 = 半径 × 半径 × 円周率 

#半径1の円の面積3.14
#半径2の円の面積12.56
#半径3の円の面積18.84

from typing import AnyStr, Callable
from typing import Callable, List


#Callable[[メソッド引数の型]], 返り値の型]
def calcArea(_r: float, print_func: Callable[[list], None]) -> float:
    _PI: float = 3.14
    _area: float = (_r * _r) * _PI
    print_func([_PI, _area])
    return _area

def showAreaPrint(l: list) -> None:
    _r = l[0]
    _area = l[1]
    print("半径{0}の円の面積:{1}".format(_r, _area))

def main(compare_r: int) -> int:
    base_area: float = 0
    r: float = 1    #r = 半径
    base_area = calcArea(r, showAreaPrint)

    compare_area: float = 0
    # r: float = 2    #r = 半径
    compare_area = calcArea(compare_r, showAreaPrint)
    return compare_area / base_area

print(main(3))


# input：r=半径
# output:r=1の時と比べて何倍かを返す
# 半径2の円の面積は
# 半径1の円の面積の 
# 4倍です。
