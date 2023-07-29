# from os import popen
# from _pytest.python_api import ApproxMapping
import pytest
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.star import Star

@pytest.fixture
def new_Star():
    ''' Returns a newly initialised World object '''
    return Star('Test')

''' Test atmosphere for siz = 0 '''

def test1():
    assert 1 > 0