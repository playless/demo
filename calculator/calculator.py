class  Calculator:
    """
    计算器 加减乘除
    """
    def add(self,a,b):
        """

        :param a: 任意数字
        :param b: 任意数字
        :return: 两数之和
        """
        return a+b
    def sub(self,a,b):
        """

        :param a: 任意数字
        :param b:任意数字
        :return: 两数之差
        """
        return a-b

    def Multiply(self,a,b):
        '''

        :param a: 任意数字
        :param b: 任意数字
        :return: 两数之积
        '''
        return a*b
    def division(self,a,b):
        '''

        :param a: 任意数字
        :param b: 不能为0
        :return: 两数相除
        '''
        if b==0:
            print("b不能为0")
        else:
            return a/b


