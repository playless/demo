import pytest

def setup_function():
    pass
def setup_module():
    print("整个模块只执行一次")
class TestDemo:
    def setup_class(self):
        print("整个类开始之前执行一次")
    def teardown_class(self):
        print("类结束之后执行")
    def setup_method(self):
        print("计算开始")
    def teardown_method(self):
        print("计算结束")
    def test_one(self):
        a=5
        b=1
        assert  a!=b
        print("我是第一个")
    def test_two(self):
        print("我是帅哥")