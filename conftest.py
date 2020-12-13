#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
@pytest.fixture(scope="module",autouse=True)
def myfix():
    print("计算开始")
    yield
    print("计算结束")