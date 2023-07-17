

# Imports

import json
import logging
import star

# Configure logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)s [%(funcName)-12s\t] \
                               %(levelname)s %(message)s',
                              '%d/%m/%Y %I:%M:%S %p')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.WARNING)

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
            starJSON['Stellar Type'] = star.starType
            starJSON['Subtype'] = star.starSubType
            starJSON['Stellar Class'] = star.starClass
            starJSON['Stellar Mass'] = star.starMass
            
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

        # Calculate the system age
        # First, if there are no post-stellar objects

        # if self.Stars[0].starClass == 'V':  self.genSystemAgePrimary(self)
    
    # Determine the system's age based on the primary

    def genSystemAgePrimary(self):

        # Main sequence stars first
        # determine the star life span

        pass

    # Determine the system's age based on post-stellar objects

if __name__ == '__main__':
    these_Systems = []
    for x in range(1, 2):
        this_System = System('Test System')
        this_System.genSystem()
        these_Systems.append(this_System)

    j = 0
    for a_System in these_Systems:
        
        i = 0
        for star in a_System.Stars:
            print('System %s \tIndex %s: \t%s%s %s' % (j+1, i, star.starType, star.starSubType, star.starClass))
            i += 1
        j += 1

    systemJSON = json.dumps(createSystemJSON(this_System), indent=4)


    systemJSON = json.dumps(createSystemJSON(this_System), indent=4)

    print(systemJSON)





    
