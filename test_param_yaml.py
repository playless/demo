import pytest
import yaml

from calculator.calculator import Calculator
from getyanmdata import *

data=getyanmdata()
calc=Calculator()
class TestCalc:

    @pytest.mark.parametrize("a,b,expect",data["datas"],ids=data["myid"])
    def test_add(self, a, b, expect):
        ''''
        测试加法
        '''
        assert expect == calc.add(a, b)
