import pytest
""" Function to raise power recursively """
def raise_power(base,exp):

    """ Base Cases """
    """ Checks to see if exp == 0 """
    if(exp == 0):
        return 1

    """ Checks to see if exp == 1 """
    if(exp == 1):
        """ Returns base of any num raise to 1 equals num itself """
        return(base)

    """ Recursive Case """
    """ Checks to see if exp is not equal to one """
    if(exp != 1):

        """ Mulitiply base recursively by the function """
        return(base * raise_power(base, exp-1))

""" Prints result after function is complete """
print(raise_power(9,2))
print(raise_power(4,1))
print(raise_power(9,0))
print(raise_power(-4,2))


def test_raise_power():
    assert raise_power(9,2) == 81

def test_raise_power2():
    assert raise_power(4,1) == 4

def test_raise_power3():
    assert raise_power(9,0) == 1

def test_raise_power5():
    assert raise_power(-4,2) == 16






