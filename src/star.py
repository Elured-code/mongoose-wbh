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
            self.starMass = 0
            self.starDiameter = 0

    # Class properties go here
    # Using properties to leave open the possibility of verifying and modifying
    # values as they are set

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

    @property
    def starMassVariance(self):
        return self.__starMassVariance
    
    @starMassVariance.setter
    def starMassVariance(self, starMassVariance):
        self.__starMassVariance = starMassVariance


    @property
    def starTemp(self):
        return self.__starTemp
    
    @starTemp.setter
    def starTemp(self, starTemp):
        self.__starTemp = starTemp
    
    @property
    def starDiameter(self):
        return self.__starDiameter
    
    @starDiameter.setter
    def starDiameter(self, starDiameter):
        self.__starDiameter = starDiameter

    @property
    def starLuminosity(self):
        return self.__starLuminosity
    
    @starLuminosity.setter
    def starLuminosity(self, starLuminosity):
        self.__starLuminosity = starLuminosity

    @property
    def starAge(self):
        return self.__starAge
    
    @starAge.setter
    def starAge(self, starAge):
        self.__starAge = starAge

    @property
    def starColour(self):
        return self.__starColour
    
    @starColour.setter
    def starColour(self, starColour):
        self.__starColour = starColour
    
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

                if roll <= 8:
                    
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
                        sDetails = self.genSubGiantStar()
                        self.starClass = sDetails[0]
                        self.starType  = sDetails[1]
                        self.starSubType = sDetails[2]

                # Now handle giants
                
                else:
                    sDetails = self.genGiantStar()
                    self.starClass = sDetails[0]
                    self.starType = sDetails[1]
                    self.starSubType = sDetails[2]                    

        # Modified rolls of 12 or greater are Hot stars, handle them here

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

    # Generate the star mass

    def genStarMass(self):

            # Build a query from the star class, type and subtype

            db = TinyDB('db.json')
            q = Query()
            r = db.search((q.starClass == self.starClass) \
                        & (q.starType == self.starType) \
                        & (q.starSubType == self.starSubType))
            
            # There shouldn't be duplicates, but only accept the first result

            r = r[0]

            # Vary the stellar mass around the base mass by up to 20%
            # Using a normal distribution with a standard deviation of 7% 
            # of the base mass, so about 99.5% of values will fall within 
            # the 20% value

            # Because numpy.random can return multiple values, select the first
            # (of one in this case)
            # Round the result to 3 decimals and return

            mass = numpy.random.normal(r['baseMass'], r['baseMass'] * 0.07, 1)[0]
            self.starMassVariance = mass/r['baseMass'] 
            self.starMass = round(mass, 3)

    # Generate the star surface temperature
        
    def genStarTemp(self):
            
            # Build a query from the star class, type and subtype

            db = TinyDB('db.json')
            q = Query()
            r = db.search((q.starClass == self.starClass) \
                        & (q.starType == self.starType) \
                        & (q.starSubType == self.starSubType))
            
            # There shouldn't be duplicates, but only accept the first result

            r = r[0]
            self.starTemp = r['baseTemp']

    # Generate the star diameter

    def genStarDiameter(self):
            
            # Build a query from the star class, type and subtype

            db = TinyDB('db.json')
            q = Query()
            r = db.search((q.starClass == self.starClass) \
                        & (q.starType == self.starType) \
                        & (q.starSubType == self.starSubType))
            
            # There shouldn't be duplicates, but only accept the first result

            r = r[0]
            self.starDiameter = r['diameter']

    # Generate star luminosity

    def genStarLuminosity(self):
        self.starLuminosity = \
            (self.starDiameter ** 2) * (self.starTemp/5800) ** 4
        
        # Apply the mass variance to luminosity

        self.starLuminosity = round((self.starLuminosity * self.starMassVariance), 3)

    # Generate the star/system age

    def genStarAge(self):

        # Handle main sequence stars first

        if self.starClass == 'V':
            
            # First determine the star lifespan

            msLifeSpan = round(10 / (self.starMass ** 2.5), 1)
            print('Life Span:  ', msLifeSpan)

            # Determine age for small main sequence stars
            # (mass <= 0.9)

            if self.starMass <= 0.9:
                age = (dice.D6Roll() * 2) + (dice.D3Roll() - 2) + \
                    (dice.D10Roll() / 10) + (dice.D10Roll() / 100)

                # Using the WBH assumption that star formation began around
                # 12 billion years ago, cap the age at 12

                if age > 12: age = 12.0
                age = round(age, 2)

            # Determine age for larger main sequence stars

            else:
                age = round((msLifeSpan * (dice.D100Roll() / 100)), 2)

        else:
            pass

        self.starAge = age

    # Get the star colour

    def genStarColour(self):
        db = TinyDB('db.json')
        q = Query()
        r = db.search((q.starType == self.starType))
        r = r[0]
        self.starColour = r['starColour']

    # The methods below determine class, type and subtypes
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
        r = dice.D6Rollx2() - 2
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

            # Hot subdwards

            if r == 9:
                r2 = dice.D6Rollx2() - 2
                sType = tables.HOT_STAR_TYPES[r2]

            # 'Normal' subdwarfs

            else: sType = tables.STAR_TYPES[r]

            # Change Type F to Type G

            if sType == 'F':  sType = 'G'

            # Change Type A to Type B

            if sType == 'A':  sType = 'B'

            logging.debug('Determining subdwarf subtype')
            r = dice.D6Rollx2() - 2
            sSubType = tables.STAR_SUBTYPES[r]

        logger.debug('Returning class %s, type %s, subtype %s', sClass, sType, sSubType)
        return sClass, sType, sSubType
    
    #
    # Generate a subgiant star
    #

    def genSubGiantStar(self):
        sClass = 'IV'
        logging.debug('Determining Subgiant type')
        r = dice.D6Rollx2() - 3 + 1 # +1 DM for class rolls
                                    # -2 to match table index

        # Deal with hot subgiants first

        if r >= 9:
            r2 = dice.D6Rollx2() - 2
            sType = tables.HOT_STAR_TYPES[r2]

            # Change O to B

            if sType == 'O': sType = 'B'

            # Now determine the subtype

            logging.debug('Determining star subtype')
            r3 = dice.D6Rollx2() - 2
            sSubType = tables.STAR_SUBTYPES[r]

        # Now non-hot sugiants

        else:

            # Limit Class IV to the range B0 - K4

            if r in range(1, 5): r += 5

            # Cap the roll at 8 to avoid the 'Hot' result

            if r >= 8: r = 8

            sType = tables.STAR_TYPES[r]

            logging.debug('Determining star subtype')
            r = dice.D6Rollx2() - 2
            sSubType = tables.STAR_SUBTYPES[r]

            # Any K5 or lower gets converted to K4

            if (sType == 'K') and (sSubType > 4): sSubType = 4

        return sClass, sType, sSubType

    #
    # Generate a giant star
    #

    def genGiantStar(self):
        logging.debug('Determining Giant class')
        r = dice.D6Rollx2() - 2
        sClass = tables.GIANT_STAR_CLASSES[r]

        logging.debug('Determining Giant type')

        # Remember to always subtract 3 when using the STAR_TYPES table
        # DM +1 for Giants on this table, upper limit remains 12

        r = dice.D6Rollx2() + 1

        # Ignore Special results
        if r < 3: r = 3

        # Note that the bounds of the roll will now be 3 to 13

        # A roll of 12 indicates a hot giant, roll on the Hot table

        if r >= 12:
            logging.debug('Determining Hot Giant type')
            r2 = dice.D6Rollx2() - 2
            sType = tables.HOT_STAR_TYPES[r2]

        # Otherwise use the normal type table (roll is now 3 to 11)
        # Subtract 3 to get the correct table entry

        else:
            logging.debug('Determining non-Hot Giant type')
            sType = tables.STAR_TYPES[r - 3]

        # Now determine the subtype

        logging.debug('Determining the Giant subtype')
        r = dice.D6Rollx2() - 2
        sSubType = tables.STAR_SUBTYPES[r] 

        return sClass, sType, sSubType 

    # Generate the star, calling the previous object methods to determine
    # stellar characteristics
    #
    
    def genStar(self, dm, includeUnusual, isPrimary):
        self.genStarType(dm, includeUnusual, isPrimary)
        self.genStarMass()
        self.genStarTemp()
        self.genStarDiameter()
        self.genStarLuminosity()
        self.genStarAge()
        self.genStarColour()

        # Debugging code to catch non-typed stars

        if self.starType == '': input("Press Enter to continue...")   

if __name__ == '__main__':
    thisStar = Star()
    thisStar.genStar(0, False, True)

    print('Mass', thisStar.starMass) 
    print('Variance', thisStar.starMassVariance)
    print('Temperature', thisStar.starTemp)  
    print('Diameter', thisStar.starDiameter)
    print('Luminosity', thisStar.starLuminosity)   