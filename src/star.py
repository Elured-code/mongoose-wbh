import logging
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
                if roll <= 10:
                    self.starClass = tables.SPECIAL_STAR_CLASSES[roll - 2]
                    logger.debug('Star class is %s', self.starClass)
                pass
                
        # Modified rolls of 12 or greateer are Hot stars, handle them here

        elif roll > 12:
                logger.debug('Determining Hot star type')
                roll = dice.D6Rollx2()
                self.starType = tables.HOT_STAR_TYPES[roll - 2]   
                logger.debug('Star type is %s', self.starType)         

        # 'Normal' main sequence stars

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

    # Generate the star, calling the previous object methods to determine
    # stellar characteristics
    
    def genStar(self, dm, includeUnusual, isPrimary):
        self.genStarType(dm, includeUnusual, isPrimary)

