import pytest
import yaml

from calculator.calculator import Calculator
from getyamldata import *

data=getyanmdata()
calc=Calculator()
class TestCalc:
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expect",data["add"],ids=data["myid"][0])
    def test_add(self, a, b, expect):
        ''''
        测试加法
        '''
        assert expect == calc.add(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expect", data["sub"],ids=data["myid"][1])
    def test_sub(self, a, b, expect):
        '''
        测试减法
        '''
        assert calc.sub(a, b) == expect

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,expect", data["div"],ids=data["myid"][2])
    def test_division(self, a, b, expect):
        '''
        测试除法
        '''
        assert calc.division(a, b) == expect

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect", data["mul"],ids=data["myid"][3])
    def test_multiply(self, a, b, expect):
        '''
        测试乘法
        '''
        assert calc.Multiply(a, b) == expect
