import pytest

from pyhtondemo.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("测试开始")
    def teardown_class(self):
        print("测试结束")
    def setup_method(self):
        print("计算开始")
    def teardown_method(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 8), (-1, -2, -3), (100, 300, 400)
    ])
    def test_add(self, a, b, expect):
        ''''
        测试加法
        '''
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expect",[(3,5,-2),(5,1,4),(-1,-2,1),(100,200,-100)])
    def test_sub(self,a,b,expect):
        '''
        测试减法
        '''
        assert self.calc.sub(a,b)==expect

    @pytest.mark.parametrize("a,b,expect",[(6,3,2),(-9,-3,3),(-12,4,-3),(5,2,2.5),(10,0,None)])
    def test_division(self,a,b,expect):
        '''
        测试除法
        '''
        assert self.calc.division(a,b)==expect

    @pytest.mark.parametrize("a,b,expect",[(3,5,15),(-5,1,-5),(-1,-2,2),(100,0,0)])
    def test_multiply(self,a,b,expect):
        '''
        测试乘法
        '''
        assert self.calc.Multiply(a,b)==expect
