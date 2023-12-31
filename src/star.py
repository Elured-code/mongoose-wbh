''' star.py - system primary generation '''

# PyLint rule customisations
# pylint: disable=wrong-import-position
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-public-methods

# Import external modules

import sys
import os
import logging
import numpy

from tinydb import TinyDB, Query

# Set the Python path to allow module discovery

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import local modules

from src.utils import dice
from src.utils import tables

# Get the logging context from the calling module

logger = logging.getLogger(__name__)

class Star:
    ''' Star class - for stellar bodies '''

    def __init__(self):
        logger.debug('Initialising star object')
        self.star_name = ''
        self.star_type = ''
        self.star_subtype = ''
        self.star_class = ''
        self.star_mass = 0
        self.star_diameter = 0

    # Class properties go here
    # Using properties to leave open the possibility of verifying and modifying
    # values as they are set

    @property
    def star_name(self):
        ''' The name of the stellar object (not necessarily the system name)'''
        return self.__star_name

    @star_name.setter
    def star_name(self, star_name):
        self.__star_name = star_name

    @property
    def star_type(self):
        ''' Star spectral type '''
        return self.__star_type

    @star_type.setter
    def star_type(self, star_type):
        self.__star_type = star_type

    @property
    def star_class(self):
        ''' Star mass class '''
        return self.__star_class

    @star_class.setter
    def star_class(self, star_class):
        self.__star_class = star_class

    @property
    def star_mass(self):
        ''' Star mass in solar masses '''
        return self.__star_mass

    @star_mass.setter
    def star_mass(self, star_mass):
        self.__star_mass = star_mass

    @property
    def star_mass_variance(self):
        ''' Variance between class/type/subtype mass and actual mass '''
        return self.__star_mass_variance

    @star_mass_variance.setter
    def star_mass_variance(self, star_mass_variance):
        self.__star_mass_variance = star_mass_variance

    @property
    def star_temp(self):
        ''' Star surface temperature '''
        return self.__star_temp

    @star_temp.setter
    def star_temp(self, star_temp):
        self.__star_temp = star_temp

    @property
    def star_diameter(self):
        ''' Stellar diameter in solar diameters '''
        return self.__star_diameter

    @star_diameter.setter
    def star_diameter(self, star_diameter):
        self.__star_diameter = star_diameter

    @property
    def star_luminosity(self):
        ''' Stellar luminosity in solar luminosities '''
        return self.__star_luminosity

    @star_luminosity.setter
    def star_luminosity(self, star_luminosity):
        self.__star_luminosity = star_luminosity

    @property
    def star_age(self):
        ''' Star age '''
        return self.__star_age

    @star_age.setter
    def star_age(self, star_age):
        self.__star_age = star_age

    @property
    def star_colour(self):
        ''' Star colour classification '''
        return self.__star_colour

    @star_colour.setter
    def star_colour(self, star_colour):
        self.__star_colour = star_colour

    # Determine the star type
    # MGT2 WBH pp15-16
    #

    def genstar_type(self, die_modifier, include_unusual, is_primary):
        ''' Generate the star spectral type '''
        logger.debug('Determining star type')
        roll = dice.D6Rollx2() + die_modifier
        logger.debug('Roll = %s', roll)

        # Modified rolls of 2 or less are Special or Unusual stars, handle them here

        if roll <= 2:

            # If Unusual stars are allowed generate here

            if include_unusual:
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

                    self.star_class = tables.SPECIAL_STAR_CLASSES[roll - 2]
                    logger.debug('Star class is %s', self.star_class)

                    # Now determine the stellar type
                    # First for Class VI stars

                    if self.star_class == 'VI':
                        logger.debug('Determining Class VI type')
                        roll = dice.D6Rollx2() + 1
                        star_details = self.genSubDwarfStar()
                        self.star_class = star_details[0]
                        self.star_type = star_details[1]
                        self.star_subtype = star_details[2]

                    # Now determine for Class IV stars

                    elif self.star_class == 'IV':
                        star_details = self.genSubGiantStar()
                        self.star_class = star_details[0]
                        self.star_type  = star_details[1]
                        self.star_subtype = star_details[2]

                # Now handle giants

                else:
                    star_details = self.genGiantStar()
                    self.star_class = star_details[0]
                    self.star_type = star_details[1]
                    self.star_subtype = star_details[2]

        # Modified rolls of 12 or greater are Hot stars, handle them here

        elif roll >= 12:
            star_details = self.genHotStar()
            self.star_class = star_details[0]
            self.star_type = star_details[1]
            self.star_subtype = star_details[2]

        # All others are 'normal' main sequence stars

        else:
            logger.debug('Determining Normal object type')
            star_details = self.gen_main_sequence_star(roll, is_primary)
            self.star_class = star_details[0]
            self.star_type = star_details[1]
            self.star_subtype = star_details[2]

        logger.debug('Star type is %s', self.star_type)
        logger.debug('Star subtype is %s', self.star_subtype)
        logger.debug('Star class is %s', self.star_class)

    # Generate the star mass

    def genstar_mass(self):
        ''' Determine stellar mass '''
        logger.debug('Determining star mass')

        # Build a query from the star class, type and subtype

        star_details_db = TinyDB('db.json')
        this_query = Query()
        query_result = star_details_db.search((this_query.star_class == self.star_class) \
                    & (this_query.star_type == self.star_type) \
                    & (this_query.star_subtype == self.star_subtype))

        # There shouldn't be duplicates, but only accept the first result

        query_result = query_result[0]

        # Vary the stellar mass around the base mass by up to 20%
        # Using a normal distribution with a standard deviation of 7%
        # of the base mass, so about 99.5% of values will fall within
        # the 20% value

        # Because numpy.random can return multiple values, select the first
        # (of one in this case)
        # Round the result to 3 decimals and return

        mass = numpy.random.normal(query_result['baseMass'], query_result['baseMass'] * 0.07, 1)[0]
        self.star_mass_variance = mass/query_result['baseMass']
        self.star_mass = round(mass, 3)
        logger.debug('Star mass is %s solar masses', self.star_mass)

    # Generate the star surface temperature

    def genstar_temp(self):
        ''' Generate the stellar surface temperature '''
        logger.debug('Determining star surface temperature')

        # Build a query from the star class, type and subtype

        star_details_db = TinyDB('db.json')
        this_query = Query()
        query_result = star_details_db.search((this_query.star_class == self.star_class) \
                    & (this_query.star_type == self.star_type) \
                    & (this_query.star_subtype == self.star_subtype))

        # There shouldn't be duplicates, but only accept the first result

        query_result = query_result[0]
        self.star_temp = query_result['baseTemp']
        logger.debug('Star surface temperature is %sK', self.star_temp)

    # Generate the star diameter

    def genstar_diameter(self):
        ''' Generate stellar diameter '''
        logger.debug('Calculating star diameter')

        # Build a query from the star class, type and subtype

        star_details_db = TinyDB('db.json')
        this_query = Query()
        query_result = star_details_db.search((this_query.star_class == self.star_class) \
                    & (this_query.star_type == self.star_type) \
                    & (this_query.star_subtype == self.star_subtype))

        # There shouldn't be duplicates, but only accept the first result

        query_result = query_result[0]
        self.star_diameter = query_result['diameter']
        logger.debug('Star diameter is %s solar diameters', self.star_diameter)

    # Generate star luminosity

    def genstar_luminosity(self):
        ''' Generate star lumininosity value '''
        logger.debug('Calculating star luminosity')
        self.star_luminosity = \
            (self.star_diameter ** 2) * (self.star_temp/5800) ** 4

        # Apply the mass variance to luminosity

        self.star_luminosity = round((self.star_luminosity * self.star_mass_variance), 3)
        logger.debug('Star luminosity is %s x solar luminosity', self.star_luminosity)

    # Generate the star/system age

    def genstar_age(self):
        ''' Determine the star age '''
        logger.debug('Calculating star age')

        # Handle non-post-main sequence stars first
        # This includes class Ia, Ib, II and VI

        if self.star_class in ['Ia', 'Ib', 'II', 'V', 'VI']:
            logger.debug('Determining main sequence star age')

            # First determine the star lifespan

            main_sequence_lifespan = round(10 / (self.star_mass ** 2.5), 3)
            logger.debug('Main sequence star life span is %s Gy', main_sequence_lifespan)

            # Determine age for small main sequence stars
            # (mass <= 0.9)

            if self.star_mass <= 0.9:
                logger.debug ('Determining age of small main sequence star')
                age = (dice.D6Roll() * 2) + (dice.D3Roll() - 2) + \
                    (dice.D10Roll() / 10) + (dice.D10Roll() / 100)

            # Determine age for larger main sequence stars

            else:
                logger.debug('Determining age of large main sequence star')
                age = round((main_sequence_lifespan * (dice.D100Roll() / 100)), 3)

        # Subgiant (Class IV) stars

        elif self.star_class == 'IV':

            # First get the lifespan of the star in the main sequence

            main_sequence_lifespan = round(10 / (self.star_mass ** 2.5), 3)
            logger.debug('Main sequence star life span is %s Gy', main_sequence_lifespan)

            # Now get the lifespan of the star as a subgiant

            logger.debug('Determining age for subgiant star')
            subgiant_lifespan = round(main_sequence_lifespan/(4 + self.star_mass), 3)
            logger.debug('Subgiant life span is %s Gy', subgiant_lifespan)

            # Determine the stars position in its life as a subgiant

            age = main_sequence_lifespan + (subgiant_lifespan * (dice.D100Roll() / 100))
            age = round(age, 3)

        # Giant (Class III) stars

        elif self.star_class == 'III':

            # First get the lifespan of the star in the main sequence

            main_sequence_lifespan = round(10 / (self.star_mass ** 2.5), 3)
            logger.debug('Main sequence star life span is %s Gy', main_sequence_lifespan)

            # Then calculate the subgiant life span

            subgiant_lifespan = round(main_sequence_lifespan/(4 + self.star_mass), 3)
            logger.debug('Subgiant life span is %s Gy', subgiant_lifespan)

            # Now calculate the lifespan of the star as a giant

            giant_lifespan = round(main_sequence_lifespan / (10 * self.star_mass ** 3), 3)
            logger.debug('Giant lifespan is %s Gy', giant_lifespan)

            # Getting the variance value (place in giant lifespan)

            variance = (giant_lifespan * (dice.D1000Roll() / 100))

            # Finally calculate the star age from previous values

            age = round(main_sequence_lifespan + subgiant_lifespan + variance, 1)

        else:

            # Placeholder to avoid crashes where i havent finished code

            age = 0

        # Using the WBH assumption that star formation began around
        # 12 billion years ago, cap the age at 12

        age = min(age, 12.0)
        age = round(age, 3)

        # Put a lower bound on the age to allow for protostars later
        age = max(age, 0.001)

        self.star_age = age
        logger.debug('Star age is %s Gy', self.star_age)

    # Get the star colour

    def genstar_colour(self):
        ''' Determine the star colour based on spectral class/subclass '''
        logger.debug('Determining star colour')
        star_details_db = TinyDB('db.json')
        q = Query()
        r = star_details_db.search((q.star_type == self.star_type))
        r = r[0]
        self.star_colour = r['star_colour']
        logger.debug('Star colour is %s', self.star_colour)

    # The methods below determine class, type and subtypes
    #
    # Generate a main sequence star
    #

    def gen_main_sequence_star(self, roll, is_primary):
        ''' Generate characteristics for a main sequence (Class V) star '''
        logger.debug('Determining Normal object type')

        # Subtract an additional 1 from the roll as a roll of 2 is
        # a Special object

        star_type = tables.STAR_TYPES[roll - 3]
        star_class = 'V'

        # Determine the subtype

        logger.debug('Determining subtype')

        # Non Type M stars first

        if star_type != 'M':
            logger.debug('Determining subtype for %s class', star_class)
            r = dice.D6Rollx2() - 2
            sSubType = tables.STAR_SUBTYPES[r]

        # Type M stars are a special case and vary from primary to others

        elif is_primary:
            logger.debug('Determinng subtype for %s class (PRIMARY)', \
                        star_class)
            r = dice.D6Rollx2() - 2
            sSubType = tables.MSTAR_SUBTYPES[r]
        else: 
            logger.debug('Determining subtype for %s class (NON-PRIMARY)', \
                        star_class)
            r = dice.D6Rollx2() - 2
            sSubType = tables.STAR_SUBTYPES[r]        

        logger.debug('Returning class %s, type %s, subtype %s', star_class, star_type, sSubType)
        return star_class, star_type, sSubType

    #
    # Generate a hot main sequence star
    #

    def genHotStar(self):
        star_class = 'V'
        logger.debug('Determining Hot star type')
        r = dice.D6Rollx2() - 2
        star_type = tables.HOT_STAR_TYPES[r]         

        logger.debug('Determining Hot star subtype')
        r = dice.D6Rollx2() - 2        
        sSubType = tables.STAR_SUBTYPES[r]

        logger.debug('Returning class %s, type %s, subtype %s', star_class, star_type, sSubType)
        return star_class, star_type, sSubType

    #
    # Generate a subdwarf star
    #

    def genSubDwarfStar(self):
        logger.debug('Determining subgiant star type')
        star_class = 'VI'
        roll = dice.D6Rollx2() + 1

        # Hot subdwarfs first

        if roll > 11:
            logging.debug('Determining hot subdwarf star subtype')
            roll2 = dice.D6Rollx2() - 2
            star_type = tables.HOT_STAR_TYPES[roll2]

            # Change Type A to Type B

            if star_type == 'A':
                star_type = 'B'

            logger.debug('Determining hot subdwarf star subtype')
            roll3 = dice.D6Rollx2() - 2
            sSubType = tables.STAR_SUBTYPES[roll3]

        # Now all other subdwarfs

        else:

            # Remember to always subtract 3 when using the STAR_TYPES table

            logging.debug('Determining subdwarf type')
            r = dice.D6Rollx2() - 3

            # Hot subdwards

            if r == 9:
                r2 = dice.D6Rollx2() - 2
                star_type = tables.HOT_STAR_TYPES[r2]

            # 'Normal' subdwarfs

            else: star_type = tables.STAR_TYPES[r]

            # Change Type F to Type G

            if star_type == 'F':  star_type = 'G'

            # Change Type A to Type B

            if star_type == 'A':  star_type = 'B'

            logging.debug('Determining subdwarf subtype')
            r = dice.D6Rollx2() - 2
            sSubType = tables.STAR_SUBTYPES[r]

        logger.debug('Returning class %s, type %s, subtype %s', star_class, star_type, sSubType)
        return star_class, star_type, sSubType

    #
    # Generate a subgiant star
    #

    def genSubGiantStar(self):
        star_class = 'IV'
        logging.debug('Determining Subgiant type')
        r = dice.D6Rollx2() - 3 + 1 # +1 die_modifier for class rolls
                                    # -2 to match table index

        # Deal with hot subgiants first

        if r >= 9:
            r2 = dice.D6Rollx2() - 2
            star_type = tables.HOT_STAR_TYPES[r2]

            # Change O to B

            if star_type == 'O': star_type = 'B'

            # Now determine the subtype

            logging.debug('Determining star subtype')
            r3 = dice.D6Rollx2() - 2
            sSubType = tables.STAR_SUBTYPES[r3]

        # Now non-hot sugiants

        else:

            # Limit Class IV to the range B0 - K4

            if r in range(0, 5): r += 5

            # Cap the roll at 8 to avoid the 'Hot' result

            if r >= 8: r = 8

            star_type = tables.STAR_TYPES[r]

            logging.debug('Determining star subtype')
            r = dice.D6Rollx2() - 2
            sSubType = tables.STAR_SUBTYPES[r]

            # Any K5 or lower gets converted to K4

            if (star_type == 'K') and (sSubType > 4): sSubType = 4

        return star_class, star_type, sSubType

    #
    # Generate a giant star
    #

    def genGiantStar(self):
        logging.debug('Determining Giant class')
        r = dice.D6Rollx2() - 2
        star_class = tables.GIANT_STAR_CLASSES[r]

        logging.debug('Determining Giant type')

        # Remember to always subtract 3 when using the STAR_TYPES table
        # die_modifier +1 for Giants on this table, upper limit remains 12

        r = dice.D6Rollx2() + 1

        # Ignore Special results
        if r < 3: r = 3

        # Note that the bounds of the roll will now be 3 to 13

        # A roll of 12 indicates a hot giant, roll on the Hot table

        if r >= 12:
            logging.debug('Determining Hot Giant type')
            r2 = dice.D6Rollx2() - 2
            star_type = tables.HOT_STAR_TYPES[r2]

        # Otherwise use the normal type table (roll is now 3 to 11)
        # Subtract 3 to get the correct table entry

        else:
            logging.debug('Determining non-Hot Giant type')
            star_type = tables.STAR_TYPES[r - 3]

        # Now determine the subtype

        logging.debug('Determining the Giant subtype')
        r = dice.D6Rollx2() - 2
        sSubType = tables.STAR_SUBTYPES[r] 

        return star_class, star_type, sSubType 

    # Generate the star, calling the previous object methods to determine
    # stellar characteristics
    #
    
    def genStar(self, die_modifier, include_unusual, is_primary):
        self.genstar_type(die_modifier, include_unusual, is_primary)
        self.genstar_mass()
        self.genstar_temp()
        self.genstar_diameter()
        self.genstar_luminosity()
        self.genstar_age()
        self.genstar_colour()

        # Debugging code to catch non-typed stars

        if self.star_type == '': input("Press Enter to continue...")   

if __name__ == '__main__':
    thisStar = Star()
    thisStar.genStar(0, False, True)

    print('Mass', thisStar.star_mass) 
    print('Variance', thisStar.star_mass_variance)
    print('Temperature', thisStar.star_temp)  
    print('Diameter', thisStar.star_diameter)
    print('Luminosity', thisStar.star_luminosity)
