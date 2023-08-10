# from os import popen
# from _pytest.python_api import ApproxMapping
import pytest
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.star import Star

@pytest.fixture(scope='session')
def star_Collection():
    starCollection = []
    for i in range(0, 10001):
        starName = 'Test' + str(i)
        thisStar = Star()
        thisStar.starName = starName
        thisStar.genStar(0, False, False)
        data = {'Star Age': thisStar.starAge}
        data['Star Class'] =  thisStar.starClass
        data['Star Type'] = thisStar.starType
        data['Star SubType'] = thisStar.starSubType
        starCollection.append(data)

    return starCollection

''' Test star age '''
def test_starAge(star_Collection):

    errors = []
    assert star_Collection is not None
    for data_point in star_Collection: 
            
        # replace assertions by conditions because we are
        # looping through numerous data points and dont want to stop
        # on the first failure
        if not (data_point["Star Age"] <= 12.0 or data_point["Star Age"] == 0): 

            # Format the error message
            errorMsg = 'Invalid age: ' + str(data_point["Star Age"]) \
                + ' ' + data_point['Star Type'] \
                + str(data_point['Star SubType']) + ' ' \
                + data_point['Star Class'] + ')'
            errors.append(errorMsg)
    
    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))

''' Test star Class VI restrictions '''
def test_starClassVI(star_Collection):

    errors = []
    assert star_Collection is not None
    for data_point in star_Collection:    

        # replace assertions by conditions as above
        if (data_point['Star Class'] == 'VI') \
            and data_point['Star Type'] in ('A', 'F'):
                
                # Format the error message
                errorMsg = 'Invalid type for Class VI star: ' \
                + (data_point["Star Type"])
                errors.append(errorMsg)
    
    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))            
