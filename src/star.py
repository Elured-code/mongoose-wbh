import logging
import numpy
from tinydb import TinyDB, Query
import utils.dice as dice
import utils.tables as tables

# Get the logging context from the calling module

logger = logging.getLogger(__name__)

# Star internal class - attributes and methods for stellar generation

class Star:
    def __init__(self):
            logger.debug('Initialising star object')
            self.starName = ''
            self.starType = ''
            self.starSubType = ''
            self.starClass = ''

    @property
    def starName(self):
        return self.__starName
    
    @starName.setter
    def starName(self, starName):
        self.__starName = starName

    @property
    def starType(self):
        return self.__starType
    
    @starType.setter
    def starType(self, starType):
        self.__starType = starType

    @property
    def starClass(self):
        return self.__starClass
    
    @starClass.setter
    def starClass(self, starClass):
         self.__starClass = starClass
    
    @property
    def starMass(self):
        return self.__starMass
    
    @starMass.setter
    def starMass(self, starMass):
        self.__starMass = starMass
    
    # Determine the star type
    # MGT2 WBH pp15-16

    def genStarType(self, dm, includeUnusual, isPrimary):
        logger.debug('Determining star type')
        roll = dice.D6Rollx2() + dm
        logger.debug('Roll = %s', roll)

        # Modified rolls of 2 or less are Special or Unusual stars, handle them here

        if roll <= 2:

            # If Unusual stars are allowed generate here

            if includeUnusual:
                roll = dice.D6Rollx2()
                logger.debug('Determining Unusual object type')

                if roll == 2: 
                     logger.debug('Determining Peculiar object type')
                     self.starType = 'Peculiar'

            # Otherwise roll for a Special type
            
            else:  
                logger.debug('Determining Special object type')  
                roll = dice.D6Rollx2()

                # Handle non-giants first

                if roll <= 10:
                    
                    # Determine the stellar class
                    
                    self.starClass = tables.SPECIAL_STAR_CLASSES[roll - 2]
                    logger.debug('Star class is %s', self.starClass)
                
                    # Now determine the stellar type
                    # First for Class VI stars

                    if self.starClass == 'VI':
                        logger.debug('Determining Class VI type')
                        roll = dice.D6Rollx2() + 1
                         
                        # Hot subdwarfs first

                        if roll > 11:
                            self.starType = \
                            tables.HOT_STAR_TYPES[dice.D6Rollx2()]
                              
                            # Change Type A to Type B

                            if self.starType == 'A': self.starType = 'B'

                            self.starSubType = \
                            tables.STAR_SUBTYPES[dice.D6Roll() - 2]

                        else:
                            self.starType = \
                            tables.STAR_TYPES[dice.D6Rollx2()]

                            # Change Type F to Type G

                            if self.starType == 'F':  self.starType = 'G'

                            self.starSubType = \
                            tables.STAR_SUBTYPES[dice.D6Roll() - 2]

                    # Now determine for Class IV stars

                    elif self.starClass == 'IV':
                        pass

                # Now handle giants
                
                else:
                    pass

        # Modified rolls of 12 or greateer are Hot stars, handle them here

        elif roll >= 12:
                logger.debug('Determining Hot star type')
                roll = dice.D6Rollx2()
                self.starType = tables.HOT_STAR_TYPES[roll - 2]   
                logger.debug('Star type is %s', self.starType) 
                self.starSubType = tables.STAR_SUBTYPES[dice.D6Rollx2() - 2]
                logger.debug('Star subtype is $s', self.starSubType)
                self.starClass = 'V'


        # 'Normal' main sequence stars

        else:
            logger.debug('Determining Normal object type')

            # Subtract an additional 1 from the roll as a roll of 2 is 
            # a Special object

            self.starType = tables.STAR_TYPES[roll - 3] 
            self.starClass = 'V'

            # Determine the subtype

            logger.debug('Determining subtype') 
            if self.starType != 'M':
                logger.debug('Determining subtype for %s class', self.starClass)
                self.starSubType = tables.STAR_SUBTYPES[dice.D6Rollx2() - 2]
            elif isPrimary:
                logger.debug('Determinng subtype for %s class (PRIMARY)', \
                            self.starClass)
                self.starSubType = tables.MSTAR_SUBTYPES[dice.D6Rollx2() - 2]
            else: 
                logger.debug('Determinng subtype for %s class (NON-PRIMARY)', \
                            self.starClass)
                self.starSubType = tables.STAR_SUBTYPES[dice.D6Rollx2() - 2]

        logger.debug('Star type is %s', self.starType)
        logger.debug('Star subtype is %s', self.starSubType)
        logger.debug('Star class is %s', self.starClass)

    def genStarMass(self, aClass, aType, aSubType):

        # Build a query from the star class, type and subtype

        db = TinyDB('db.json')
        q = Query()
        r = db.search((q.starClass == aClass) & (q.starType == aType) \
                      & (q.starSubType == aSubType))
        
        # There shouldn't be duplicates, but only accept the first result

        r = r[0]

        # Vary the stellar mass around the base mass by up to 20%
        # Using a normal distribution with a standard deviation of 7% 
        # of the base mass, so about 99.5% of values will fall within 
        # the 20% value

        mass = numpy.random.normal(r['baseMass'], r['baseMass'] * 0.07, 1) 

        # Because numpy.random can return multiple values, select the first
        # (of one in this case)
        # Round the result to 3 decimals and return

        self.starMass = round(mass[0], 3)
        
  
    # Generate the star, calling the previous object methods to determine
    # stellar characteristics
    
    def genStar(self, dm, includeUnusual, isPrimary):
        self.genStarType(dm, includeUnusual, isPrimary)

        self.genStarMass(self.starClass, self.starType, self.starSubType)


if __name__ == '__main__':
    thisStar = Star()
    thisStar.genStar(0, False, True)

    print(thisStar.starMass)
