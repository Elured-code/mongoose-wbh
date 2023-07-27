# from os import popen
# from _pytest.python_api import ApproxMapping
import pytest

from src import star

@pytest.fixture
def new_Star():
    ''' Returns a newly initialised World object '''
    return Star('Test')