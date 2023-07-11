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
    
    #
    # Determine the star type
    # MGT2 WBH pp15-16
    #

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

                # Roll again on the Peculiar table on a roll of 2

                if roll == 2: 
                     logger.debug('Determining Peculiar object type')

                # Otherwise pick from the Unusual table     
                
                else:
                    pass

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
                        sDetails = self.genSubDwarfStar()
                        self.starClass = sDetails[0]
                        self.starType = sDetails[1]
                        self.starSubType = sDetails[2]

                    # Now determine for Class IV stars

                    elif self.starClass == 'IV':
                        pass

                # Now handle giants
                
                else:
                    pass

        # Modified rolls of 12 or greateer are Hot stars, handle them here

        elif roll >= 12:
            sDetails = self.genHotStar()
            self.starClass = sDetails[0]
            self.starType = sDetails[1]
            self.starSubType = sDetails[2]

        # All others are 'normal' main sequence stars

        else:
            logger.debug('Determining Normal object type')
            sDetails = self.genMainSequenceStar(roll, isPrimary)
            self.starClass = sDetails[0]
            self.starType = sDetails[1]
            self.starSubType = sDetails[2]

        logger.debug('Star type is %s', self.starType)
        logger.debug('Star subtype is %s', self.starSubType)
        logger.debug('Star class is %s', self.starClass)

    #
    # Generate the star, calling the previous object methods to determine
    # stellar characteristics
    #
    
    def genStar(self, dm, includeUnusual, isPrimary):
        self.genStarType(dm, includeUnusual, isPrimary)

    #
    # Generate a main sequence star
    #

    def genMainSequenceStar(self, roll, isPrimary):
        logger.debug('Determining Normal object type')

        # Subtract an additional 1 from the roll as a roll of 2 is 
        # a Special object

        sType = tables.STAR_TYPES[roll - 3] 
        sClass = 'V'

        # Determine the subtype

        logger.debug('Determining subtype') 

        # Non Type M stars first

        if sType != 'M':
            logger.debug('Determining subtype for %s class', sClass)
            r = dice.D6Rollx2() - 2
            sSubType = tables.STAR_SUBTYPES[r]
        
        # Type M stars are a special case and vary from primary to others
        
        elif isPrimary:
            logger.debug('Determinng subtype for %s class (PRIMARY)', \
                        sClass)
            r = dice.D6Rollx2() - 2
            sSubType = tables.MSTAR_SUBTYPES[r]
        else: 
            logger.debug('Determining subtype for %s class (NON-PRIMARY)', \
                        sClass)
            r = dice.D6Rollx2() - 2
            sSubType = tables.STAR_SUBTYPES[r]        

        logger.debug('Returning class %s, type %s, subtype %s', sClass, sType, sSubType)
        return sClass, sType, sSubType
    
    #
    # Generate a hot main sequence star
    #

    def genHotStar(self):
        sClass = 'V'
        logger.debug('Determining Hot star type')
        r = dice.D6Rollx2()
        sType = tables.HOT_STAR_TYPES[r]         
        
        logger.debug('Determining Hot star subtype')
        r = dice.D6Rollx2() - 2        
        sSubType = tables.STAR_SUBTYPES[r]
        
        logger.debug('Returning class %s, type %s, subtype %s', sClass, sType, sSubType)
        return sClass, sType, sSubType

    #
    # Generate a subdwarf star
    #

    def genSubDwarfStar(self):
        logger.debug('Determining subgiant star type')
        sClass = 'VI'
        roll = dice.D6Rollx2() + 1
            
        # Hot subdwarfs first

        if roll > 11:
            logging.debug('Determining hot subdwarf star subtype')
            r = dice.D6Rollx2() - 2
            sType = tables.HOT_STAR_TYPES[r]
                
            # Change Type A to Type B

            if self.starType == 'A': self.starType = 'B'

            logger.debug('Determining hot subdwarf star subtype')
            r = dice.D6Rollx2() - 2
            sSubType = tables.STAR_SUBTYPES[r]

        # Now all other subdwarfs

        else:

            # Remember to always subtract 3 when using the STAR_TYPES table

            logging.debug('Determining subdwarf type')
            r = dice.D6Rollx2() - 3
            sType = tables.STAR_TYPES[r]

            # Change Type F to Type G

            if sType == 'F':  sType = 'G'

            logging.debug('Determining subdward subtype')
            r = dice.D6Rollx2() - 2
            sSubType = tables.STAR_SUBTYPES[r]

        logger.debug('Returning class %s, type %s, subtype %s', sClass, sType, sSubType)
        return sClass, sType, sSubType
    
    #
    # Generate a subgiant star
    #

    #
    # Generate a giant star
    #