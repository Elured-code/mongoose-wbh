# from os import popen
# from _pytest.python_api import ApproxMapping
import pytest
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.star import Star

@pytest.fixture(autouse=True)
def init_cache(request, capsys):
    starCollection = []
    for i in range(0, 10):
        starName = 'Test' + str(i)
        thisStar = Star()
        thisStar.starName = starName
        thisStar.genStar(0, False, False)
        data = {'Star Age': thisStar.starAge}
        starCollection.append(data)
    with capsys.disabled(): print('Generated %i star objects' % i)  
    request.config.cache.set('star_data', starCollection)

@pytest.fixture
def new_Star():
    ''' Returns a newly initialised star object '''
    return Star('Test')

''' Test star age '''
def test_starAge(request):
    data = request.config.cache.get('star_data', None)
    errors = []
    assert data is not None
    for data_point in data: 
            
        # replace assertions by conditions
        if not data_point["Star Age"] <= 12.0: 
            errorMsg = 'Star age failed test - generated age = ' + str(data_point["Star Age"])
            errors.append(errorMsg)
    
    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))

''' Test star age '''
# @pytest.mark.parametrize("roll1", D6X2ROLLS)
# def test_gen_atm_siz0(new_World, roll1):
#     new_World.siz = 0
#     new_World.gen_atm(roll1)
#     assert new_World.atm == 0