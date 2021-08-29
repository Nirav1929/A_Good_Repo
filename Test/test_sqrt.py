import pytest
import os
import sys

sys.path.insert(1, os.getcwd())

from Code.__init__ import Array_Sqrt

def test_sqrt_1():
    array = [1,4,9,16]
    sqrt = Array_Sqrt()
    ans = [1,2,3,4]
    assert (sqrt.sqrt(array)==ans).all()