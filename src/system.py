''' system.py:  MG2T WBH system generation '''

# PyLint rule customisations
# pylint: disable=wrong-import-position
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-public-methods

# Import external modules

import json
import logging
import os
import sys

# Set the Python path to allow module discovery

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import local modules

from src import star

# Configure logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)s [%(funcName)-12s\t] \
                               %(levelname)s %(message)s',
                              '%d/%m/%Y %I:%M:%S %p')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Create a JSON object containing the system data


def create_system_json(a_system):
    '''Create a JSON string that represents the mainworld data'''

    logger.debug('Creating JSON object for %s', a_system.system_name)

    output_json = {}
    # mainworld_json = {}

    # Create the JSON header and populate

    header_json = {}
    header_json['Object Type'] = 'System'
    header_json['Rules System'] = 'Mongoose Traveller'
    header_json['Edition'] = '2'
    header_json['Version'] = '2023'
    header_json['Extensions'] = 'TBC'

    output_json['Header'] = header_json

    system_json = {}
    system_json['System Name'] = a_system.system_name

    output_json['Description'] = system_json
    # contents_json = ['Contents']

    stars_json = []
    stars_json.append('Stars')
    for this_star in a_system.system_stars:
        index_value = 0
        star_json = {}
        star_json['Index'] = index_value
        star_json['Stellar Type'] = this_star.star_type
        star_json['Subtype'] = this_star.star_subtype
        star_json['Stellar Class'] = this_star.star_class
        star_json['Stellar Mass'] = this_star.star_mass
        star_json['Stellar Surface Temperature'] = this_star.star_temp
        star_json['Stellar Diameter'] = this_star.star_diameter
        star_json['Stellar Luminosity'] = this_star.star_luminosity
        star_json['Stellar Age'] = this_star.star_age
        star_json['Stellar Colour'] = this_star.star_colour

        stars_json.append(star_json)

        index_value += 1

    output_json['Contents'] = stars_json
    return output_json


# System class - container class for a WBH hex location

class System:
    """Class to hold a MGT2 system/hex"""

    def __init__(self, name):
        logger.debug('Initialising system object for system %s',name)
        self.system_name = name
        self.system_stars = []

    @property
    def system_name(self):
        """Get system_name"""
        return self.__system_name

    @system_name.setter
    def system_name(self, system_name):
        """Set system_name"""
        self.__system_name = system_name

    @property
    def system_stars(self):
        """Get system_stars"""
        return self.__system_stars

    @system_stars.setter
    def system_stars(self, system_stars):
        """Set system_stars"""
        self.__system_stars = system_stars

    def generate_system(self):
        """Generate the system/hex contents"""

        # Generate the primary

        primary_star = star.Star()
        primary_star.gen_star(0, False, True)
        self.system_stars.append(primary_star)

        # Generate companions

        for companion_orbit_type in primary_star.star_companions:

            # Only check for Close, Near and Far orbits

            if companion_orbit_type != "Companion":

                # Check for the presence of a companion object in the orbit band
                if primary_star.star_companions[companion_orbit_type] is True:

                    # Ok, now generate the companion

                    companion_star = star.CompanionStar(companion_orbit_type)
                    companion_star.gen_star()



if __name__ == '__main__':
    these_Systems = []
    for x in range(1, 51):
        this_System = System('Test System')
        this_System.generate_system()
        these_Systems.append(this_System)

    j = 0
    for a_System in these_Systems:

        i = 0
        for star in a_System.system_stars:
            if star.star_class in ('V'):
                print(f'System {j+1}\tIndex {i}\t{star.star_type}\
                      {star.star_subtype} {star.star_class}')

            i += 1
        j += 1

    systemJSON = json.dumps(create_system_json(this_System), indent=4)

    #print(systemJSON)
