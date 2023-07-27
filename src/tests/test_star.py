# from os import popen
# from _pytest.python_api import ApproxMapping
import pytest
import os.path
import sys

sys.path.append('../src')
print(sys.path)

from src.star import Star

@pytest.fixture
def new_Star():
    ''' Returns a newly initialised World object '''
    return Star('Test')

''' Test atmosphere for siz = 0 '''

def test1():
    assert 1 > 0