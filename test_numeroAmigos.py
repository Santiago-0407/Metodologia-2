import pytest
from numeroAmigos import numeros_amigos
    
def Test_1():
    assert(9,13) == "9 y 13 son amigos"

def Test_2():
    assert(5,8) == "5 y 8 no son amigos"
    
def Test_3():
    assert(100,45) == "100 y 45 son amigos"

def Test_4():
    assert(1,3) == "1 y 3 son amigos"

def Test_5():
    assert(7,18) == "7 y 18 no son amigos"

def Test_6():
    assert(14,91) == "14 y 91 no son amigos"
    
def Test_7():
    assert(4,7) == "4 y 7 son amigos"

def Test_8():
    assert(15,30) == "15 y 30 son amigos"
    
def Test_9():
    assert(374,648) == "374 y 648 son amigos"

def Test_10():
    assert(777,666) == "777 y 666 no son amigos"
    
if __name__ == '__main__':
    Test_1()
    Test_2()
    Test_3()
    Test_4()
    Test_5()
    Test_6()
    Test_7()
    Test_8()
    Test_9()
    Test_10()
