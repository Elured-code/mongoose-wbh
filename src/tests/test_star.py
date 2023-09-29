''' test_star.py:  Unit Tests for star generation '''

# from os import popen
# from _pytest.python_api import ApproxMapping

import os
import sys
import pytest

from src.star import Star

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


@pytest.fixture(name='star_collection', scope='session')
def fixture_star_collection():
    ''' A fixture to generate a collection of star objects for testing '''
    star_collection = []
    for i in range(0, 101):
        star_name = 'Test' + str(i)
        this_star = Star()
        this_star.star_name = star_name
        this_star.gen_star(0, False, False)
        data = {'Star Age': this_star.star_age}
        data['Star Class'] =  this_star.star_class
        data['Star Type'] = this_star.star_type
        data['Star SubType'] = this_star.star_subtype
        star_collection.append(data)
    return star_collection

# Test star age

def test_star_age(star_collection):
    ''' Check the star age is within bounds '''
    errors = []
    assert star_collection is not None
    for data_point in star_collection:

        # replace assertions by conditions because we are  looping through
        # numerous data points and dont want to stop on the first failure

        if not (data_point["Star Age"] <= 12.0 or data_point["Star Age"] == 0):

            # Format the error message
            error_msg = 'Invalid age: ' + str(data_point["Star Age"]) \
                + ' ' + data_point['Star Type'] \
                + str(data_point['Star SubType']) + ' ' \
                + data_point['Star Class'] + ')'
            errors.append(error_msg)

    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))

# Test star Class VI restrictions
def test_star_class_vi(star_collection):
    ''' Check that Class VI stars have correct type and subtype '''
    errors = []
    assert star_collection is not None
    for data_point in star_collection:

        # replace assertions by conditions as above
        if (data_point['Star Class'] == 'VI') \
        and data_point['Star Type'] in ('A', 'F'):

            # Format the error message
            error_msg = 'Invalid type for Class VI star: ' \
            + (data_point["Star Type"])
            errors.append(error_msg)

    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))
