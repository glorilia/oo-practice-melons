############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""


    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.reporting_code = code
        self.first_harvest = first_harvest
        self.color = color 
        self.seedless = is_seedless
        self.bestseller = is_bestseller
        self.name = name


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.reporting_code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    cas.add_pairing('strawberries')
    cas.add_pairing('mint')
    all_melon_types.append(cas)

    cren = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 2013, 'yellow', False, True, 'Watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)


    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Traverse list of MelonType objects
    for melon in melon_types:
        print(f'{melon.name} pairs with')
        # Traverse list of pairings in specific instance of the MelonType obj
        for pairing in melon.pairings:
            print(f'- {pairing}')
        print('')


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Create empty melon dictionary
    melon_dict = {}

    # Traverse list of MelonType objects
    for melon in melon_types:
        # Add to dictionary with key of reporting code and value of object itself
        melon_dict[melon.reporting_code] = melon

    return melon_dict


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rating, color_rating, field, harvester_name):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester_name = harvester_name

    def is_sellable(self):
        return (self.shape_rating > 5 and self.color_rating > 5 
                and self.field != 3)


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    all_melons = []



def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



