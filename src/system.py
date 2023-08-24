# Import external modules

import json
import logging
import os
import sys

# Set the Python path to allow module discovery

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import local modules

import star as star

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

def createSystemJSON(System):
        '''Create a JSON string that represents the mainworld data'''

        logger.debug('Creating JSON object for %s', System.systemName)

        outputJSON = {}
        mainWorldJSON = {}

        # Create the JSON header and populate

        headerJSON = {}
        headerJSON['Object Type'] = 'System'
        headerJSON['Rules System'] = 'Mongoose Traveller'
        headerJSON['Edition'] = '2'
        headerJSON['Version'] = '2023'
        headerJSON['Extensions'] = 'TBC'

        outputJSON['Header'] = headerJSON

        systemJSON = {}
        systemJSON['System Name'] = System.systemName

        outputJSON['Description'] = systemJSON
        contentsJSON = ['Contents']

        starsJSON = []
        starsJSON.append('Stars')
        for star in System.Stars:
            i = 0
            starJSON = {}
            starJSON['Index'] = i
            starJSON['Stellar Type'] = star.star_type
            starJSON['Subtype'] = star.star_subtype
            starJSON['Stellar Class'] = star.star_class
            starJSON['Stellar Mass'] = star.star_mass
            starJSON['Stellar Surface Temperature'] = star.star_temperature
            starJSON['Stellar Diameter'] = star.star_diameter
            starJSON['Stellar Luminosity'] = star.star_luminosity
            starJSON['Stellar Age'] = star.star_age
            starJSON['Stellar Colour'] = star.star_colour
            
            starsJSON.append(starJSON)
            
            i += 1
        
        outputJSON['Contents'] = starsJSON
        return outputJSON


# System class - container class for a WBH hex location

class System:

    def __init__(self, name):
        logger.debug('Initialising system object for system %s',name)
        self.systemName = name
        self.Stars = []

    @property
    def systemName(self):
        return self.__systemName
    
    @systemName.setter
    def systemName(self, systemName):
        self.__systemName = systemName

    @property
    def Stars(self):
        return self.__Stars
    
    @Stars.setter
    def Stars(self, Stars):
        self.__Stars = Stars

    def genSystem(self):

        # Generate the primary

        star_Primary = star.Star()
        star_Primary.genStar(0, False, True)
        self.Stars.append(star_Primary)

    # Write system details to a JSON document

    def createJSON(self):
        pass

if __name__ == '__main__':
    these_Systems = []
    for x in range(1, 10000):
        this_System = System('Test System')
        this_System.genSystem()
        these_Systems.append(this_System)

    j = 0
    for a_System in these_Systems:
        
        i = 0
        for star in a_System.Stars:
            if star.star_class in ('Ia', 'Ib', 'II'):
                print('System %s \tIndex %s: \t%s%s %s \tAge %s \tMass %s' % \
                (j+1, i, star.star_type, star.star_subtype, star.star_class, \
                star.star_age, star.star_mass))
            i += 1
        j += 1

    # systemJSON = json.dumps(createSystemJSON(this_System), indent=4)

    # print(systemJSON)





    
