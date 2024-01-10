"""dbload.py - load stellar data into a TinyDB database"""

# PyLint rule customisations
# pylint: disable=wrong-import-position
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-public-methods
# pylint: disable=line-too-long
# pylint: disable=too-many-lines

from tinydb import TinyDB, Query


db = TinyDB("db.json")

print("Clearing database")

db.truncate()

# Bright Supergiants (Luminosity Class I / Ia)

# Type O

db.insert(
    {
        "star_class": "Ia",
        "star_type": "O",
        "star_subtype": 0,
        "baseMass": 200.0,
        "baseTemp": 50000,
        "diameter": 25.0,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "O",
        "star_subtype": 1,
        "baseMass": 176.0,
        "baseTemp": 48000,
        "diameter": 24.4,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "O",
        "star_subtype": 2,
        "baseMass": 152.0,
        "baseTemp": 46000,
        "diameter": 23.8,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "O",
        "star_subtype": 3,
        "baseMass": 128.0,
        "baseTemp": 44000,
        "diameter": 23.2,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "O",
        "star_subtype": 4,
        "baseMass": 104.0,
        "baseTemp": 42000,
        "diameter": 22.6,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "O",
        "star_subtype": 5,
        "baseMass": 80.0,
        "baseTemp": 40000,
        "diameter": 22.0,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "O",
        "star_subtype": 6,
        "baseMass": 76.0,
        "baseTemp": 38000,
        "diameter": 21.6,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "O",
        "star_subtype": 7,
        "baseMass": 72.0,
        "baseTemp": 36000,
        "diameter": 21.2,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "O",
        "star_subtype": 8,
        "baseMass": 68.0,
        "baseTemp": 34000,
        "diameter": 20.8,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "O",
        "star_subtype": 9,
        "baseMass": 64.0,
        "baseTemp": 32000,
        "diameter": 20.4,
    }
)

# Type B

db.insert(
    {
        "star_class": "Ia",
        "star_type": "B",
        "star_subtype": 0,
        "baseMass": 60.0,
        "baseTemp": 30000,
        "diameter": 20.0,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "B",
        "star_subtype": 1,
        "baseMass": 54.0,
        "baseTemp": 27000,
        "diameter": 28.0,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "B",
        "star_subtype": 2,
        "baseMass": 48.0,
        "baseTemp": 24000,
        "diameter": 36.0,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "B",
        "star_subtype": 3,
        "baseMass": 42.0,
        "baseTemp": 21000,
        "diameter": 44.0,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "B",
        "star_subtype": 4,
        "baseMass": 36.0,
        "baseTemp": 18000,
        "diameter": 52.0,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "B",
        "star_subtype": 5,
        "baseMass": 30.0,
        "baseTemp": 15000,
        "diameter": 60.0,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "B",
        "star_subtype": 6,
        "baseMass": 28.0,
        "baseTemp": 14000,
        "diameter": 72.0,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "B",
        "star_subtype": 7,
        "baseMass": 26.0,
        "baseTemp": 13000,
        "diameter": 84.0,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "B",
        "star_subtype": 8,
        "baseMass": 24.0,
        "baseTemp": 12000,
        "diameter": 96.0,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "B",
        "star_subtype": 9,
        "baseMass": 22.0,
        "baseTemp": 10000,
        "diameter": 108,
    }
)

# Type A

db.insert(
    {
        "star_class": "Ia",
        "star_type": "A",
        "star_subtype": 0,
        "baseMass": 20.0,
        "baseTemp": 10000,
        "diameter": 120,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "A",
        "star_subtype": 1,
        "baseMass": 19.0,
        "baseTemp": 9600,
        "diameter": 132,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "A",
        "star_subtype": 2,
        "baseMass": 18.0,
        "baseTemp": 9200,
        "diameter": 144,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "A",
        "star_subtype": 3,
        "baseMass": 17.0,
        "baseTemp": 8800,
        "diameter": 156,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "A",
        "star_subtype": 4,
        "baseMass": 16.0,
        "baseTemp": 8400,
        "diameter": 168,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "A",
        "star_subtype": 5,
        "baseMass": 15.0,
        "baseTemp": 8000,
        "diameter": 180,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "A",
        "star_subtype": 6,
        "baseMass": 14.6,
        "baseTemp": 7600,
        "diameter": 186,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "A",
        "star_subtype": 7,
        "baseMass": 14.2,
        "baseTemp": 7200,
        "diameter": 192,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "A",
        "star_subtype": 8,
        "baseMass": 13.8,
        "baseTemp": 6800,
        "diameter": 198,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "A",
        "star_subtype": 9,
        "baseMass": 13.4,
        "baseTemp": 6400,
        "diameter": 204,
    }
)

# Type F

db.insert(
    {
        "star_class": "Ia",
        "star_type": "F",
        "star_subtype": 0,
        "baseMass": 13.0,
        "baseTemp": 7500,
        "diameter": 210,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "F",
        "star_subtype": 1,
        "baseMass": 12.8,
        "baseTemp": 7300,
        "diameter": 224,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "F",
        "star_subtype": 2,
        "baseMass": 12.6,
        "baseTemp": 7100,
        "diameter": 238,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "F",
        "star_subtype": 3,
        "baseMass": 12.4,
        "baseTemp": 6900,
        "diameter": 252,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "F",
        "star_subtype": 4,
        "baseMass": 12.2,
        "baseTemp": 6700,
        "diameter": 266,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "F",
        "star_subtype": 5,
        "baseMass": 12.0,
        "baseTemp": 6500,
        "diameter": 280,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "F",
        "star_subtype": 6,
        "baseMass": 12.0,
        "baseTemp": 6400,
        "diameter": 290,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "F",
        "star_subtype": 7,
        "baseMass": 12.0,
        "baseTemp": 6300,
        "diameter": 300,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "F",
        "star_subtype": 8,
        "baseMass": 12.0,
        "baseTemp": 6200,
        "diameter": 310,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "F",
        "star_subtype": 9,
        "baseMass": 12.0,
        "baseTemp": 6100,
        "diameter": 320,
    }
)

# Type G

db.insert(
    {
        "star_class": "Ia",
        "star_type": "G",
        "star_subtype": 0,
        "baseMass": 12.0,
        "baseTemp": 6000,
        "diameter": 330,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "G",
        "star_subtype": 1,
        "baseMass": 12.2,
        "baseTemp": 5920,
        "diameter": 336,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "G",
        "star_subtype": 2,
        "baseMass": 12.4,
        "baseTemp": 5840,
        "diameter": 342,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "G",
        "star_subtype": 3,
        "baseMass": 12.6,
        "baseTemp": 5760,
        "diameter": 348,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "G",
        "star_subtype": 4,
        "baseMass": 12.8,
        "baseTemp": 5680,
        "diameter": 354,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "G",
        "star_subtype": 5,
        "baseMass": 13.0,
        "baseTemp": 5600,
        "diameter": 360,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "G",
        "star_subtype": 6,
        "baseMass": 13.2,
        "baseTemp": 5520,
        "diameter": 372,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "G",
        "star_subtype": 7,
        "baseMass": 13.4,
        "baseTemp": 5440,
        "diameter": 384,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "G",
        "star_subtype": 8,
        "baseMass": 13.6,
        "baseTemp": 5360,
        "diameter": 396,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "G",
        "star_subtype": 9,
        "baseMass": 13.8,
        "baseTemp": 5280,
        "diameter": 408,
    }
)

# Type K

db.insert(
    {
        "star_class": "Ia",
        "star_type": "K",
        "star_subtype": 0,
        "baseMass": 14.0,
        "baseTemp": 5200,
        "diameter": 420,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "K",
        "star_subtype": 1,
        "baseMass": 14.8,
        "baseTemp": 5040,
        "diameter": 458,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "K",
        "star_subtype": 2,
        "baseMass": 15.6,
        "baseTemp": 4880,
        "diameter": 506,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "K",
        "star_subtype": 3,
        "baseMass": 16.4,
        "baseTemp": 4720,
        "diameter": 544,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "K",
        "star_subtype": 4,
        "baseMass": 17.2,
        "baseTemp": 4560,
        "diameter": 582,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "K",
        "star_subtype": 5,
        "baseMass": 18.0,
        "baseTemp": 4400,
        "diameter": 600,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "K",
        "star_subtype": 6,
        "baseMass": 18.4,
        "baseTemp": 4260,
        "diameter": 660,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "K",
        "star_subtype": 7,
        "baseMass": 18.8,
        "baseTemp": 4120,
        "diameter": 720,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "K",
        "star_subtype": 8,
        "baseMass": 19.2,
        "baseTemp": 3920,
        "diameter": 780,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "K",
        "star_subtype": 9,
        "baseMass": 19.6,
        "baseTemp": 3840,
        "diameter": 840,
    }
)

# Type M

db.insert(
    {
        "star_class": "Ia",
        "star_type": "M",
        "star_subtype": 0,
        "baseMass": 20.0,
        "baseTemp": 3700,
        "diameter": 60.0,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "M",
        "star_subtype": 1,
        "baseMass": 21.0,
        "baseTemp": 3560,
        "diameter": 68.0,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "M",
        "star_subtype": 2,
        "baseMass": 22.0,
        "baseTemp": 3420,
        "diameter": 76.0,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "M",
        "star_subtype": 3,
        "baseMass": 23.0,
        "baseTemp": 3280,
        "diameter": 84.0,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "M",
        "star_subtype": 4,
        "baseMass": 24.0,
        "baseTemp": 3140,
        "diameter": 92.0,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "M",
        "star_subtype": 5,
        "baseMass": 25.0,
        "baseTemp": 3000,
        "diameter": 100,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "M",
        "star_subtype": 6,
        "baseMass": 26.2,
        "baseTemp": 2850,
        "diameter": 125,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "M",
        "star_subtype": 7,
        "baseMass": 27.5,
        "baseTemp": 2700,
        "diameter": 150,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "M",
        "star_subtype": 8,
        "baseMass": 28.8,
        "baseTemp": 2550,
        "diameter": 175,
    }
)
db.insert(
    {
        "star_class": "Ia",
        "star_type": "M",
        "star_subtype": 9,
        "baseMass": 30.0,
        "baseTemp": 2400,
        "diameter": 200,
    }
)

# Bright Supergiants (Luminosity Class Ib)

# Type O

db.insert(
    {
        "star_class": "Ib",
        "star_type": "O",
        "star_subtype": 0,
        "baseMass": 150,
        "baseTemp": 50000,
        "diameter": 24.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "O",
        "star_subtype": 1,
        "baseMass": 132,
        "baseTemp": 48000,
        "diameter": 23.2,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "O",
        "star_subtype": 2,
        "baseMass": 114,
        "baseTemp": 46000,
        "diameter": 22.4,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "O",
        "star_subtype": 3,
        "baseMass": 96.0,
        "baseTemp": 44000,
        "diameter": 21.6,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "O",
        "star_subtype": 4,
        "baseMass": 78.0,
        "baseTemp": 42000,
        "diameter": 20.8,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "O",
        "star_subtype": 5,
        "baseMass": 60.0,
        "baseTemp": 40000,
        "diameter": 20.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "O",
        "star_subtype": 6,
        "baseMass": 56.0,
        "baseTemp": 38000,
        "diameter": 18.8,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "O",
        "star_subtype": 7,
        "baseMass": 52.0,
        "baseTemp": 36000,
        "diameter": 17.6,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "O",
        "star_subtype": 8,
        "baseMass": 48.0,
        "baseTemp": 34000,
        "diameter": 16.4,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "O",
        "star_subtype": 9,
        "baseMass": 44.0,
        "baseTemp": 32000,
        "diameter": 15.2,
    }
)

# Type B

db.insert(
    {
        "star_class": "Ib",
        "star_type": "B",
        "star_subtype": 0,
        "baseMass": 40.0,
        "baseTemp": 30000,
        "diameter": 14.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "B",
        "star_subtype": 1,
        "baseMass": 37.0,
        "baseTemp": 27000,
        "diameter": 16.2,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "B",
        "star_subtype": 2,
        "baseMass": 34.0,
        "baseTemp": 24000,
        "diameter": 18.4,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "B",
        "star_subtype": 3,
        "baseMass": 31.0,
        "baseTemp": 21000,
        "diameter": 20.6,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "B",
        "star_subtype": 4,
        "baseMass": 28.0,
        "baseTemp": 18000,
        "diameter": 22.8,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "B",
        "star_subtype": 5,
        "baseMass": 25.0,
        "baseTemp": 15000,
        "diameter": 25.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "B",
        "star_subtype": 6,
        "baseMass": 23.0,
        "baseTemp": 14000,
        "diameter": 30.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "B",
        "star_subtype": 7,
        "baseMass": 21.0,
        "baseTemp": 13000,
        "diameter": 35.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "B",
        "star_subtype": 8,
        "baseMass": 19.0,
        "baseTemp": 12000,
        "diameter": 40.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "B",
        "star_subtype": 9,
        "baseMass": 17.0,
        "baseTemp": 10000,
        "diameter": 45.0,
    }
)

# Type A

db.insert(
    {
        "star_class": "Ib",
        "star_type": "A",
        "star_subtype": 0,
        "baseMass": 15.0,
        "baseTemp": 10000,
        "diameter": 50.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "A",
        "star_subtype": 1,
        "baseMass": 14.6,
        "baseTemp": 9600,
        "diameter": 55.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "A",
        "star_subtype": 2,
        "baseMass": 14.2,
        "baseTemp": 9200,
        "diameter": 60.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "A",
        "star_subtype": 3,
        "baseMass": 13.8,
        "baseTemp": 8800,
        "diameter": 65.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "A",
        "star_subtype": 4,
        "baseMass": 13.4,
        "baseTemp": 8400,
        "diameter": 70.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "A",
        "star_subtype": 5,
        "baseMass": 13.0,
        "baseTemp": 8000,
        "diameter": 75.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "A",
        "star_subtype": 6,
        "baseMass": 12.8,
        "baseTemp": 7600,
        "diameter": 77.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "A",
        "star_subtype": 7,
        "baseMass": 12.6,
        "baseTemp": 7200,
        "diameter": 79.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "A",
        "star_subtype": 8,
        "baseMass": 12.4,
        "baseTemp": 6800,
        "diameter": 81.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "A",
        "star_subtype": 9,
        "baseMass": 12.2,
        "baseTemp": 6400,
        "diameter": 82.0,
    }
)

# Type F

db.insert(
    {
        "star_class": "Ib",
        "star_type": "F",
        "star_subtype": 0,
        "baseMass": 12.0,
        "baseTemp": 7500,
        "diameter": 85.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "F",
        "star_subtype": 1,
        "baseMass": 11.6,
        "baseTemp": 7300,
        "diameter": 91.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "F",
        "star_subtype": 2,
        "baseMass": 11.2,
        "baseTemp": 7100,
        "diameter": 97.0,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "F",
        "star_subtype": 3,
        "baseMass": 10.8,
        "baseTemp": 6900,
        "diameter": 103,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "F",
        "star_subtype": 4,
        "baseMass": 10.4,
        "baseTemp": 6700,
        "diameter": 109,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "F",
        "star_subtype": 5,
        "baseMass": 10.0,
        "baseTemp": 6500,
        "diameter": 115,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "F",
        "star_subtype": 6,
        "baseMass": 10.0,
        "baseTemp": 6400,
        "diameter": 119,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "F",
        "star_subtype": 7,
        "baseMass": 10.0,
        "baseTemp": 6300,
        "diameter": 123,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "F",
        "star_subtype": 8,
        "baseMass": 10.0,
        "baseTemp": 6200,
        "diameter": 127,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "F",
        "star_subtype": 9,
        "baseMass": 10.0,
        "baseTemp": 6100,
        "diameter": 131,
    }
)

# Type G

db.insert(
    {
        "star_class": "Ib",
        "star_type": "G",
        "star_subtype": 0,
        "baseMass": 10.0,
        "baseTemp": 6000,
        "diameter": 135,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "G",
        "star_subtype": 1,
        "baseMass": 10.2,
        "baseTemp": 5920,
        "diameter": 138,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "G",
        "star_subtype": 2,
        "baseMass": 10.4,
        "baseTemp": 5840,
        "diameter": 144,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "G",
        "star_subtype": 3,
        "baseMass": 10.6,
        "baseTemp": 5760,
        "diameter": 144,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "G",
        "star_subtype": 4,
        "baseMass": 10.8,
        "baseTemp": 5680,
        "diameter": 147,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "G",
        "star_subtype": 5,
        "baseMass": 11.0,
        "baseTemp": 5600,
        "diameter": 150,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "G",
        "star_subtype": 6,
        "baseMass": 11.2,
        "baseTemp": 5520,
        "diameter": 156,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "G",
        "star_subtype": 7,
        "baseMass": 11.4,
        "baseTemp": 5440,
        "diameter": 162,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "G",
        "star_subtype": 8,
        "baseMass": 11.6,
        "baseTemp": 5360,
        "diameter": 168,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "G",
        "star_subtype": 9,
        "baseMass": 11.8,
        "baseTemp": 5280,
        "diameter": 174,
    }
)

# Type K

db.insert(
    {
        "star_class": "Ib",
        "star_type": "K",
        "star_subtype": 0,
        "baseMass": 12.0,
        "baseTemp": 5200,
        "diameter": 180,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "K",
        "star_subtype": 1,
        "baseMass": 12.2,
        "baseTemp": 5040,
        "diameter": 196,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "K",
        "star_subtype": 2,
        "baseMass": 12.4,
        "baseTemp": 4880,
        "diameter": 212,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "K",
        "star_subtype": 3,
        "baseMass": 12.6,
        "baseTemp": 4720,
        "diameter": 228,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "K",
        "star_subtype": 4,
        "baseMass": 12.8,
        "baseTemp": 4560,
        "diameter": 244,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "K",
        "star_subtype": 5,
        "baseMass": 13.0,
        "baseTemp": 4400,
        "diameter": 260,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "K",
        "star_subtype": 6,
        "baseMass": 13.4,
        "baseTemp": 4260,
        "diameter": 284,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "K",
        "star_subtype": 7,
        "baseMass": 13.8,
        "baseTemp": 4120,
        "diameter": 308,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "K",
        "star_subtype": 8,
        "baseMass": 14.2,
        "baseTemp": 3920,
        "diameter": 332,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "K",
        "star_subtype": 9,
        "baseMass": 14.6,
        "baseTemp": 3840,
        "diameter": 356,
    }
)

# Type M

db.insert(
    {
        "star_class": "Ib",
        "star_type": "M",
        "star_subtype": 0,
        "baseMass": 15.0,
        "baseTemp": 3700,
        "diameter": 380,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "M",
        "star_subtype": 1,
        "baseMass": 16.0,
        "baseTemp": 3560,
        "diameter": 424,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "M",
        "star_subtype": 2,
        "baseMass": 17.0,
        "baseTemp": 3420,
        "diameter": 468,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "M",
        "star_subtype": 3,
        "baseMass": 18.0,
        "baseTemp": 3280,
        "diameter": 512,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "M",
        "star_subtype": 4,
        "baseMass": 19.0,
        "baseTemp": 3140,
        "diameter": 556,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "M",
        "star_subtype": 5,
        "baseMass": 20.0,
        "baseTemp": 3000,
        "diameter": 600,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "M",
        "star_subtype": 6,
        "baseMass": 21.2,
        "baseTemp": 2850,
        "diameter": 650,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "M",
        "star_subtype": 7,
        "baseMass": 23.5,
        "baseTemp": 2700,
        "diameter": 700,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "M",
        "star_subtype": 8,
        "baseMass": 23.8,
        "baseTemp": 2550,
        "diameter": 750,
    }
)
db.insert(
    {
        "star_class": "Ib",
        "star_type": "M",
        "star_subtype": 9,
        "baseMass": 25.0,
        "baseTemp": 2400,
        "diameter": 800,
    }
)

# Supergiants (Luminosity Class II)

# Type O

db.insert(
    {
        "star_class": "II",
        "star_type": "O",
        "star_subtype": 0,
        "baseMass": 130,
        "baseTemp": 50000,
        "diameter": 22.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "O",
        "star_subtype": 1,
        "baseMass": 112,
        "baseTemp": 48000,
        "diameter": 21.2,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "O",
        "star_subtype": 2,
        "baseMass": 94.0,
        "baseTemp": 46000,
        "diameter": 20.4,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "O",
        "star_subtype": 3,
        "baseMass": 76.0,
        "baseTemp": 44000,
        "diameter": 19.6,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "O",
        "star_subtype": 4,
        "baseMass": 58.0,
        "baseTemp": 42000,
        "diameter": 18.8,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "O",
        "star_subtype": 5,
        "baseMass": 40.0,
        "baseTemp": 40000,
        "diameter": 18.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "O",
        "star_subtype": 6,
        "baseMass": 38.0,
        "baseTemp": 38000,
        "diameter": 16.8,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "O",
        "star_subtype": 7,
        "baseMass": 36.0,
        "baseTemp": 36000,
        "diameter": 15.6,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "O",
        "star_subtype": 8,
        "baseMass": 34.0,
        "baseTemp": 34000,
        "diameter": 14.4,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "O",
        "star_subtype": 9,
        "baseMass": 32.0,
        "baseTemp": 32000,
        "diameter": 13.2,
    }
)

# Type B

db.insert(
    {
        "star_class": "II",
        "star_type": "B",
        "star_subtype": 0,
        "baseMass": 30.0,
        "baseTemp": 30000,
        "diameter": 12.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "B",
        "star_subtype": 1,
        "baseMass": 28.0,
        "baseTemp": 27000,
        "diameter": 12.4,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "B",
        "star_subtype": 2,
        "baseMass": 26.0,
        "baseTemp": 24000,
        "diameter": 12.8,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "B",
        "star_subtype": 3,
        "baseMass": 24.0,
        "baseTemp": 21000,
        "diameter": 13.2,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "B",
        "star_subtype": 4,
        "baseMass": 22.0,
        "baseTemp": 18000,
        "diameter": 13.6,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "B",
        "star_subtype": 5,
        "baseMass": 20.0,
        "baseTemp": 15000,
        "diameter": 14.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "B",
        "star_subtype": 6,
        "baseMass": 18.8,
        "baseTemp": 14000,
        "diameter": 17.2,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "B",
        "star_subtype": 7,
        "baseMass": 17.6,
        "baseTemp": 13000,
        "diameter": 20.4,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "B",
        "star_subtype": 8,
        "baseMass": 16.4,
        "baseTemp": 12000,
        "diameter": 23.6,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "B",
        "star_subtype": 9,
        "baseMass": 15.2,
        "baseTemp": 10000,
        "diameter": 26.8,
    }
)

# Type A

db.insert(
    {
        "star_class": "II",
        "star_type": "A",
        "star_subtype": 0,
        "baseMass": 14.0,
        "baseTemp": 10000,
        "diameter": 30.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "A",
        "star_subtype": 1,
        "baseMass": 13.4,
        "baseTemp": 9600,
        "diameter": 33.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "A",
        "star_subtype": 2,
        "baseMass": 12.8,
        "baseTemp": 9200,
        "diameter": 36.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "A",
        "star_subtype": 3,
        "baseMass": 12.2,
        "baseTemp": 8800,
        "diameter": 39.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "A",
        "star_subtype": 4,
        "baseMass": 11.6,
        "baseTemp": 8400,
        "diameter": 42.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "A",
        "star_subtype": 5,
        "baseMass": 11.0,
        "baseTemp": 8000,
        "diameter": 45.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "A",
        "star_subtype": 6,
        "baseMass": 10.8,
        "baseTemp": 7600,
        "diameter": 46.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "A",
        "star_subtype": 7,
        "baseMass": 10.6,
        "baseTemp": 7200,
        "diameter": 47.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "A",
        "star_subtype": 8,
        "baseMass": 10.4,
        "baseTemp": 6800,
        "diameter": 48.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "A",
        "star_subtype": 9,
        "baseMass": 10.2,
        "baseTemp": 6400,
        "diameter": 49.0,
    }
)

# Type F

db.insert(
    {
        "star_class": "II",
        "star_type": "F",
        "star_subtype": 0,
        "baseMass": 10.0,
        "baseTemp": 7500,
        "diameter": 50.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "F",
        "star_subtype": 1,
        "baseMass": 9.60,
        "baseTemp": 7300,
        "diameter": 53.2,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "F",
        "star_subtype": 2,
        "baseMass": 9.20,
        "baseTemp": 7100,
        "diameter": 56.4,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "F",
        "star_subtype": 3,
        "baseMass": 8.80,
        "baseTemp": 6900,
        "diameter": 59.6,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "F",
        "star_subtype": 4,
        "baseMass": 8.40,
        "baseTemp": 6700,
        "diameter": 62.8,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "F",
        "star_subtype": 5,
        "baseMass": 8.00,
        "baseTemp": 6500,
        "diameter": 66.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "F",
        "star_subtype": 6,
        "baseMass": 8.00,
        "baseTemp": 6400,
        "diameter": 68.2,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "F",
        "star_subtype": 7,
        "baseMass": 8.00,
        "baseTemp": 6300,
        "diameter": 70.4,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "F",
        "star_subtype": 8,
        "baseMass": 8.00,
        "baseTemp": 6200,
        "diameter": 72.6,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "F",
        "star_subtype": 9,
        "baseMass": 8.00,
        "baseTemp": 6100,
        "diameter": 74.8,
    }
)

# Type G

db.insert(
    {
        "star_class": "II",
        "star_type": "G",
        "star_subtype": 0,
        "baseMass": 8.00,
        "baseTemp": 6000,
        "diameter": 77.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "G",
        "star_subtype": 1,
        "baseMass": 8.40,
        "baseTemp": 5920,
        "diameter": 79.6,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "G",
        "star_subtype": 2,
        "baseMass": 8.80,
        "baseTemp": 5840,
        "diameter": 82.2,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "G",
        "star_subtype": 3,
        "baseMass": 9.20,
        "baseTemp": 5760,
        "diameter": 84.8,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "G",
        "star_subtype": 4,
        "baseMass": 9.60,
        "baseTemp": 5680,
        "diameter": 87.4,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "G",
        "star_subtype": 5,
        "baseMass": 10.0,
        "baseTemp": 5600,
        "diameter": 90.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "G",
        "star_subtype": 6,
        "baseMass": 10.0,
        "baseTemp": 5520,
        "diameter": 94.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "G",
        "star_subtype": 7,
        "baseMass": 10.0,
        "baseTemp": 5440,
        "diameter": 98.0,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "G",
        "star_subtype": 8,
        "baseMass": 10.0,
        "baseTemp": 5360,
        "diameter": 102,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "G",
        "star_subtype": 9,
        "baseMass": 10.0,
        "baseTemp": 5280,
        "diameter": 106,
    }
)

# Type K

db.insert(
    {
        "star_class": "II",
        "star_type": "K",
        "star_subtype": 0,
        "baseMass": 10.0,
        "baseTemp": 5200,
        "diameter": 110,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "K",
        "star_subtype": 1,
        "baseMass": 10.4,
        "baseTemp": 5040,
        "diameter": 120,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "K",
        "star_subtype": 2,
        "baseMass": 10.8,
        "baseTemp": 4880,
        "diameter": 130,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "K",
        "star_subtype": 3,
        "baseMass": 11.2,
        "baseTemp": 4720,
        "diameter": 140,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "K",
        "star_subtype": 4,
        "baseMass": 11.6,
        "baseTemp": 4560,
        "diameter": 150,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "K",
        "star_subtype": 5,
        "baseMass": 12.0,
        "baseTemp": 4400,
        "diameter": 160,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "K",
        "star_subtype": 6,
        "baseMass": 12.4,
        "baseTemp": 4260,
        "diameter": 174,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "K",
        "star_subtype": 7,
        "baseMass": 12.8,
        "baseTemp": 4120,
        "diameter": 188,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "K",
        "star_subtype": 8,
        "baseMass": 13.2,
        "baseTemp": 3920,
        "diameter": 202,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "K",
        "star_subtype": 9,
        "baseMass": 13.6,
        "baseTemp": 3840,
        "diameter": 216,
    }
)

# Type M

db.insert(
    {
        "star_class": "II",
        "star_type": "M",
        "star_subtype": 0,
        "baseMass": 14.0,
        "baseTemp": 3700,
        "diameter": 230,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "M",
        "star_subtype": 1,
        "baseMass": 14.4,
        "baseTemp": 3560,
        "diameter": 254,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "M",
        "star_subtype": 2,
        "baseMass": 14.8,
        "baseTemp": 3420,
        "diameter": 278,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "M",
        "star_subtype": 3,
        "baseMass": 15.2,
        "baseTemp": 3280,
        "diameter": 302,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "M",
        "star_subtype": 4,
        "baseMass": 15.6,
        "baseTemp": 3140,
        "diameter": 326,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "M",
        "star_subtype": 5,
        "baseMass": 16.0,
        "baseTemp": 3000,
        "diameter": 350,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "M",
        "star_subtype": 6,
        "baseMass": 16.5,
        "baseTemp": 2850,
        "diameter": 387,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "M",
        "star_subtype": 7,
        "baseMass": 17.0,
        "baseTemp": 2700,
        "diameter": 425,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "M",
        "star_subtype": 8,
        "baseMass": 17.5,
        "baseTemp": 2550,
        "diameter": 463,
    }
)
db.insert(
    {
        "star_class": "II",
        "star_type": "M",
        "star_subtype": 9,
        "baseMass": 18.0,
        "baseTemp": 2400,
        "diameter": 500,
    }
)

# Giants (Luminosity Class III)

# Type O

db.insert(
    {
        "star_class": "III",
        "star_type": "O",
        "star_subtype": 0,
        "baseMass": 110.0,
        "baseTemp": 50000,
        "diameter": 21.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "O",
        "star_subtype": 1,
        "baseMass": 94.0,
        "baseTemp": 48000,
        "diameter": 19.8,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "O",
        "star_subtype": 2,
        "baseMass": 78.0,
        "baseTemp": 46000,
        "diameter": 18.6,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "O",
        "star_subtype": 3,
        "baseMass": 62.0,
        "baseTemp": 44000,
        "diameter": 17.4,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "O",
        "star_subtype": 4,
        "baseMass": 46.0,
        "baseTemp": 42000,
        "diameter": 16.2,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "O",
        "star_subtype": 5,
        "baseMass": 30.0,
        "baseTemp": 40000,
        "diameter": 15.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "O",
        "star_subtype": 6,
        "baseMass": 28.0,
        "baseTemp": 38000,
        "diameter": 14.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "O",
        "star_subtype": 7,
        "baseMass": 26.0,
        "baseTemp": 36000,
        "diameter": 13.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "O",
        "star_subtype": 8,
        "baseMass": 24.0,
        "baseTemp": 34000,
        "diameter": 12.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "O",
        "star_subtype": 9,
        "baseMass": 22.0,
        "baseTemp": 32000,
        "diameter": 11.0,
    }
)

# Type B

db.insert(
    {
        "star_class": "III",
        "star_type": "B",
        "star_subtype": 0,
        "baseMass": 20.0,
        "baseTemp": 30000,
        "diameter": 10.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "B",
        "star_subtype": 1,
        "baseMass": 18.0,
        "baseTemp": 27000,
        "diameter": 9.20,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "B",
        "star_subtype": 2,
        "baseMass": 16.0,
        "baseTemp": 24000,
        "diameter": 8.40,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "B",
        "star_subtype": 3,
        "baseMass": 14.0,
        "baseTemp": 21000,
        "diameter": 7.60,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "B",
        "star_subtype": 4,
        "baseMass": 12.0,
        "baseTemp": 18000,
        "diameter": 6.80,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "B",
        "star_subtype": 5,
        "baseMass": 10.0,
        "baseTemp": 15000,
        "diameter": 6.00,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "B",
        "star_subtype": 6,
        "baseMass": 9.60,
        "baseTemp": 14000,
        "diameter": 5.80,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "B",
        "star_subtype": 7,
        "baseMass": 9.20,
        "baseTemp": 13000,
        "diameter": 5.60,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "B",
        "star_subtype": 8,
        "baseMass": 8.80,
        "baseTemp": 12000,
        "diameter": 5.40,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "B",
        "star_subtype": 9,
        "baseMass": 8.40,
        "baseTemp": 10000,
        "diameter": 5.20,
    }
)

# Type A

db.insert(
    {
        "star_class": "III",
        "star_type": "A",
        "star_subtype": 0,
        "baseMass": 8.00,
        "baseTemp": 10000,
        "diameter": 5.00,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "A",
        "star_subtype": 1,
        "baseMass": 7.60,
        "baseTemp": 9600,
        "diameter": 5.00,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "A",
        "star_subtype": 2,
        "baseMass": 7.20,
        "baseTemp": 9200,
        "diameter": 5.00,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "A",
        "star_subtype": 3,
        "baseMass": 6.80,
        "baseTemp": 8800,
        "diameter": 5.00,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "A",
        "star_subtype": 4,
        "baseMass": 6.40,
        "baseTemp": 8400,
        "diameter": 5.00,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "A",
        "star_subtype": 5,
        "baseMass": 6.00,
        "baseTemp": 8000,
        "diameter": 5.00,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "A",
        "star_subtype": 6,
        "baseMass": 5.60,
        "baseTemp": 7600,
        "diameter": 5.00,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "A",
        "star_subtype": 7,
        "baseMass": 5.20,
        "baseTemp": 7200,
        "diameter": 5.00,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "A",
        "star_subtype": 8,
        "baseMass": 4.80,
        "baseTemp": 6800,
        "diameter": 5.00,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "A",
        "star_subtype": 9,
        "baseMass": 4.40,
        "baseTemp": 6400,
        "diameter": 5.00,
    }
)

# Type F

db.insert(
    {
        "star_class": "III",
        "star_type": "F",
        "star_subtype": 0,
        "baseMass": 4.00,
        "baseTemp": 7500,
        "diameter": 1.70,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "F",
        "star_subtype": 1,
        "baseMass": 3.80,
        "baseTemp": 7300,
        "diameter": 1.66,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "F",
        "star_subtype": 2,
        "baseMass": 3.60,
        "baseTemp": 7100,
        "diameter": 1.62,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "F",
        "star_subtype": 3,
        "baseMass": 3.40,
        "baseTemp": 6900,
        "diameter": 1.58,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "F",
        "star_subtype": 4,
        "baseMass": 3.20,
        "baseTemp": 6700,
        "diameter": 1.54,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "F",
        "star_subtype": 5,
        "baseMass": 3.00,
        "baseTemp": 6500,
        "diameter": 1.50,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "F",
        "star_subtype": 6,
        "baseMass": 2.90,
        "baseTemp": 6400,
        "diameter": 1.42,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "F",
        "star_subtype": 7,
        "baseMass": 2.80,
        "baseTemp": 6300,
        "diameter": 1.34,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "F",
        "star_subtype": 8,
        "baseMass": 2.70,
        "baseTemp": 6200,
        "diameter": 1.26,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "F",
        "star_subtype": 9,
        "baseMass": 2.60,
        "baseTemp": 6100,
        "diameter": 1.18,
    }
)

# Type G

db.insert(
    {
        "star_class": "III",
        "star_type": "G",
        "star_subtype": 0,
        "baseMass": 2.50,
        "baseTemp": 6000,
        "diameter": 10.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "G",
        "star_subtype": 1,
        "baseMass": 2.40,
        "baseTemp": 5920,
        "diameter": 11.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "G",
        "star_subtype": 2,
        "baseMass": 2.30,
        "baseTemp": 5840,
        "diameter": 12.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "G",
        "star_subtype": 3,
        "baseMass": 2.20,
        "baseTemp": 5760,
        "diameter": 13.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "G",
        "star_subtype": 4,
        "baseMass": 2.10,
        "baseTemp": 5680,
        "diameter": 14.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "G",
        "star_subtype": 5,
        "baseMass": 2.00,
        "baseTemp": 5600,
        "diameter": 15.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "G",
        "star_subtype": 6,
        "baseMass": 1.82,
        "baseTemp": 5520,
        "diameter": 16.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "G",
        "star_subtype": 7,
        "baseMass": 1.64,
        "baseTemp": 5440,
        "diameter": 17.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "G",
        "star_subtype": 8,
        "baseMass": 1.46,
        "baseTemp": 5360,
        "diameter": 18.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "G",
        "star_subtype": 9,
        "baseMass": 1.28,
        "baseTemp": 5280,
        "diameter": 19.0,
    }
)

# Type K

db.insert(
    {
        "star_class": "III",
        "star_type": "K",
        "star_subtype": 0,
        "baseMass": 1.10,
        "baseTemp": 5200,
        "diameter": 20.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "K",
        "star_subtype": 1,
        "baseMass": 1.18,
        "baseTemp": 5040,
        "diameter": 24.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "K",
        "star_subtype": 2,
        "baseMass": 1.26,
        "baseTemp": 4880,
        "diameter": 28.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "K",
        "star_subtype": 3,
        "baseMass": 1.34,
        "baseTemp": 4720,
        "diameter": 32.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "K",
        "star_subtype": 4,
        "baseMass": 1.42,
        "baseTemp": 4560,
        "diameter": 36.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "K",
        "star_subtype": 5,
        "baseMass": 1.50,
        "baseTemp": 4400,
        "diameter": 40.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "K",
        "star_subtype": 6,
        "baseMass": 1.56,
        "baseTemp": 4260,
        "diameter": 44.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "K",
        "star_subtype": 7,
        "baseMass": 1.62,
        "baseTemp": 4120,
        "diameter": 48.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "K",
        "star_subtype": 8,
        "baseMass": 1.68,
        "baseTemp": 3920,
        "diameter": 52.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "K",
        "star_subtype": 9,
        "baseMass": 1.74,
        "baseTemp": 3840,
        "diameter": 56.0,
    }
)

# Type M

db.insert(
    {
        "star_class": "III",
        "star_type": "M",
        "star_subtype": 0,
        "baseMass": 1.80,
        "baseTemp": 3700,
        "diameter": 60.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "M",
        "star_subtype": 1,
        "baseMass": 1.92,
        "baseTemp": 3560,
        "diameter": 68.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "M",
        "star_subtype": 2,
        "baseMass": 2.04,
        "baseTemp": 3420,
        "diameter": 76.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "M",
        "star_subtype": 3,
        "baseMass": 2.16,
        "baseTemp": 3280,
        "diameter": 84.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "M",
        "star_subtype": 4,
        "baseMass": 2.28,
        "baseTemp": 3140,
        "diameter": 92.0,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "M",
        "star_subtype": 5,
        "baseMass": 2.40,
        "baseTemp": 3000,
        "diameter": 100,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "M",
        "star_subtype": 6,
        "baseMass": 3.80,
        "baseTemp": 2850,
        "diameter": 125,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "M",
        "star_subtype": 7,
        "baseMass": 5.20,
        "baseTemp": 2700,
        "diameter": 150,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "M",
        "star_subtype": 8,
        "baseMass": 6.60,
        "baseTemp": 2550,
        "diameter": 175,
    }
)
db.insert(
    {
        "star_class": "III",
        "star_type": "M",
        "star_subtype": 9,
        "baseMass": 8.00,
        "baseTemp": 2400,
        "diameter": 200,
    }
)


# Subgiants (Luminosity Class IV)

# Type B

db.insert(
    {
        "star_class": "IV",
        "star_type": "B",
        "star_subtype": 0,
        "baseMass": 20.0,
        "baseTemp": 30000,
        "diameter": 8.00,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "B",
        "star_subtype": 1,
        "baseMass": 18.0,
        "baseTemp": 27000,
        "diameter": 7.40,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "B",
        "star_subtype": 2,
        "baseMass": 16.0,
        "baseTemp": 24000,
        "diameter": 6.80,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "B",
        "star_subtype": 3,
        "baseMass": 14.0,
        "baseTemp": 21000,
        "diameter": 6.20,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "B",
        "star_subtype": 4,
        "baseMass": 12.0,
        "baseTemp": 18000,
        "diameter": 5.60,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "B",
        "star_subtype": 5,
        "baseMass": 10.0,
        "baseTemp": 15000,
        "diameter": 8.00,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "B",
        "star_subtype": 6,
        "baseMass": 8.80,
        "baseTemp": 14000,
        "diameter": 4.80,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "B",
        "star_subtype": 7,
        "baseMass": 7.60,
        "baseTemp": 13000,
        "diameter": 4.60,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "B",
        "star_subtype": 8,
        "baseMass": 6.40,
        "baseTemp": 12000,
        "diameter": 4.40,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "B",
        "star_subtype": 9,
        "baseMass": 5.20,
        "baseTemp": 11000,
        "diameter": 4.20,
    }
)


# Type A

db.insert(
    {
        "star_class": "IV",
        "star_type": "A",
        "star_subtype": 0,
        "baseMass": 4.00,
        "baseTemp": 10000,
        "diameter": 4.00,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "A",
        "star_subtype": 1,
        "baseMass": 3.66,
        "baseTemp": 9600,
        "diameter": 3.80,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "A",
        "star_subtype": 2,
        "baseMass": 3.32,
        "baseTemp": 9200,
        "diameter": 3.60,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "A",
        "star_subtype": 3,
        "baseMass": 2.98,
        "baseTemp": 8800,
        "diameter": 3.40,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "A",
        "star_subtype": 4,
        "baseMass": 2.64,
        "baseTemp": 8400,
        "diameter": 3.20,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "A",
        "star_subtype": 5,
        "baseMass": 2.30,
        "baseTemp": 8000,
        "diameter": 3.00,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "A",
        "star_subtype": 6,
        "baseMass": 2.24,
        "baseTemp": 7900,
        "diameter": 2.90,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "A",
        "star_subtype": 7,
        "baseMass": 2.18,
        "baseTemp": 7800,
        "diameter": 2.80,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "A",
        "star_subtype": 8,
        "baseMass": 2.12,
        "baseTemp": 7700,
        "diameter": 2.80,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "A",
        "star_subtype": 9,
        "baseMass": 2.06,
        "baseTemp": 7600,
        "diameter": 2.90,
    }
)

# Type F

db.insert(
    {
        "star_class": "IV",
        "star_type": "F",
        "star_subtype": 0,
        "baseMass": 2.00,
        "baseTemp": 7500,
        "diameter": 4.00,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "F",
        "star_subtype": 1,
        "baseMass": 1.90,
        "baseTemp": 7300,
        "diameter": 3.80,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "F",
        "star_subtype": 2,
        "baseMass": 1.80,
        "baseTemp": 7100,
        "diameter": 3.60,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "F",
        "star_subtype": 3,
        "baseMass": 1.70,
        "baseTemp": 6900,
        "diameter": 3.40,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "F",
        "star_subtype": 4,
        "baseMass": 1.60,
        "baseTemp": 6700,
        "diameter": 3.20,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "F",
        "star_subtype": 5,
        "baseMass": 1.50,
        "baseTemp": 6500,
        "diameter": 3.00,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "F",
        "star_subtype": 6,
        "baseMass": 1.40,
        "baseTemp": 6400,
        "diameter": 3.00,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "F",
        "star_subtype": 7,
        "baseMass": 1.40,
        "baseTemp": 6300,
        "diameter": 3.00,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "F",
        "star_subtype": 8,
        "baseMass": 1.50,
        "baseTemp": 6200,
        "diameter": 3.00,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "F",
        "star_subtype": 9,
        "baseMass": 1.60,
        "baseTemp": 6100,
        "diameter": 3.00,
    }
)

# Type G

db.insert(
    {
        "star_class": "IV",
        "star_type": "G",
        "star_subtype": 0,
        "baseMass": 1.70,
        "baseTemp": 6000,
        "diameter": 3.00,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "G",
        "star_subtype": 1,
        "baseMass": 1.52,
        "baseTemp": 5920,
        "diameter": 3.20,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "G",
        "star_subtype": 2,
        "baseMass": 1.44,
        "baseTemp": 5840,
        "diameter": 3.40,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "G",
        "star_subtype": 3,
        "baseMass": 1.36,
        "baseTemp": 5760,
        "diameter": 3.60,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "G",
        "star_subtype": 4,
        "baseMass": 1.28,
        "baseTemp": 5680,
        "diameter": 3.80,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "G",
        "star_subtype": 5,
        "baseMass": 1.20,
        "baseTemp": 5600,
        "diameter": 4.00,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "G",
        "star_subtype": 6,
        "baseMass": 1.26,
        "baseTemp": 5520,
        "diameter": 4.40,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "G",
        "star_subtype": 7,
        "baseMass": 1.32,
        "baseTemp": 5440,
        "diameter": 4.80,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "G",
        "star_subtype": 8,
        "baseMass": 1.38,
        "baseTemp": 5360,
        "diameter": 5.20,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "G",
        "star_subtype": 9,
        "baseMass": 1.44,
        "baseTemp": 5280,
        "diameter": 5.60,
    }
)

# Type K

db.insert(
    {
        "star_class": "IV",
        "star_type": "K",
        "star_subtype": 0,
        "baseMass": 1.50,
        "baseTemp": 5200,
        "diameter": 6.00,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "K",
        "star_subtype": 1,
        "baseMass": 1.56,
        "baseTemp": 5040,
        "diameter": 3.80,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "K",
        "star_subtype": 2,
        "baseMass": 1.62,
        "baseTemp": 4880,
        "diameter": 3.60,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "K",
        "star_subtype": 3,
        "baseMass": 1.68,
        "baseTemp": 4720,
        "diameter": 3.40,
    }
)
db.insert(
    {
        "star_class": "IV",
        "star_type": "K",
        "star_subtype": 4,
        "baseMass": 1.74,
        "baseTemp": 4560,
        "diameter": 3.20,
    }
)


# Main sequence stars (Luminosity Class V)

# Type O

db.insert(
    {
        "star_class": "V",
        "star_type": "O",
        "star_subtype": 0,
        "baseMass": 90.0,
        "baseTemp": 50000,
        "diameter": 20.0,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "O",
        "star_subtype": 1,
        "baseMass": 84.0,
        "baseTemp": 48000,
        "diameter": 18.4,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "O",
        "star_subtype": 2,
        "baseMass": 78.0,
        "baseTemp": 46000,
        "diameter": 16.8,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "O",
        "star_subtype": 3,
        "baseMass": 72.0,
        "baseTemp": 44000,
        "diameter": 15.2,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "O",
        "star_subtype": 4,
        "baseMass": 66.0,
        "baseTemp": 42000,
        "diameter": 13.6,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "O",
        "star_subtype": 5,
        "baseMass": 60.0,
        "baseTemp": 40000,
        "diameter": 12.0,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "O",
        "star_subtype": 6,
        "baseMass": 51.6,
        "baseTemp": 38000,
        "diameter": 3.24,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "O",
        "star_subtype": 7,
        "baseMass": 43.2,
        "baseTemp": 36000,
        "diameter": 2.98,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "O",
        "star_subtype": 8,
        "baseMass": 34.8,
        "baseTemp": 34000,
        "diameter": 2.72,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "O",
        "star_subtype": 9,
        "baseMass": 25.4,
        "baseTemp": 32000,
        "diameter": 2.46,
    }
)

# Type B

db.insert(
    {
        "star_class": "V",
        "star_type": "B",
        "star_subtype": 0,
        "baseMass": 18.0,
        "baseTemp": 30000,
        "diameter": 7.00,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "B",
        "star_subtype": 1,
        "baseMass": 15.4,
        "baseTemp": 27000,
        "diameter": 6.30,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "B",
        "star_subtype": 2,
        "baseMass": 12.8,
        "baseTemp": 24000,
        "diameter": 5.60,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "B",
        "star_subtype": 3,
        "baseMass": 10.2,
        "baseTemp": 21000,
        "diameter": 4.90,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "B",
        "star_subtype": 4,
        "baseMass": 7.60,
        "baseTemp": 18000,
        "diameter": 4.20,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "B",
        "star_subtype": 5,
        "baseMass": 5.00,
        "baseTemp": 15000,
        "diameter": 3.50,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "B",
        "star_subtype": 6,
        "baseMass": 4.44,
        "baseTemp": 14000,
        "diameter": 3.24,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "B",
        "star_subtype": 7,
        "baseMass": 3.88,
        "baseTemp": 13000,
        "diameter": 2.98,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "B",
        "star_subtype": 8,
        "baseMass": 3.32,
        "baseTemp": 12000,
        "diameter": 2.72,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "B",
        "star_subtype": 9,
        "baseMass": 2.76,
        "baseTemp": 11000,
        "diameter": 2.46,
    }
)

# Type A

db.insert(
    {
        "star_class": "V",
        "star_type": "A",
        "star_subtype": 0,
        "baseMass": 2.20,
        "baseTemp": 10000,
        "diameter": 2.20,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "A",
        "star_subtype": 1,
        "baseMass": 2.12,
        "baseTemp": 9600,
        "diameter": 2.16,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "A",
        "star_subtype": 2,
        "baseMass": 2.04,
        "baseTemp": 9200,
        "diameter": 2.12,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "A",
        "star_subtype": 3,
        "baseMass": 1.98,
        "baseTemp": 8800,
        "diameter": 2.08,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "A",
        "star_subtype": 4,
        "baseMass": 1.88,
        "baseTemp": 8400,
        "diameter": 2.04,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "A",
        "star_subtype": 5,
        "baseMass": 1.80,
        "baseTemp": 8000,
        "diameter": 2.00,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "A",
        "star_subtype": 6,
        "baseMass": 1.74,
        "baseTemp": 7600,
        "diameter": 2.10,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "A",
        "star_subtype": 7,
        "baseMass": 1.68,
        "baseTemp": 7200,
        "diameter": 2.00,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "A",
        "star_subtype": 8,
        "baseMass": 1.62,
        "baseTemp": 6800,
        "diameter": 1.90,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "A",
        "star_subtype": 9,
        "baseMass": 1.56,
        "baseTemp": 6400,
        "diameter": 1.80,
    }
)

# Type F

db.insert(
    {
        "star_class": "V",
        "star_type": "F",
        "star_subtype": 0,
        "baseMass": 1.50,
        "baseTemp": 7500,
        "diameter": 1.70,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "F",
        "star_subtype": 1,
        "baseMass": 1.46,
        "baseTemp": 7300,
        "diameter": 1.66,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "F",
        "star_subtype": 2,
        "baseMass": 1.42,
        "baseTemp": 7100,
        "diameter": 1.62,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "F",
        "star_subtype": 3,
        "baseMass": 1.38,
        "baseTemp": 6900,
        "diameter": 1.58,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "F",
        "star_subtype": 4,
        "baseMass": 1.34,
        "baseTemp": 6700,
        "diameter": 1.54,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "F",
        "star_subtype": 5,
        "baseMass": 1.30,
        "baseTemp": 6500,
        "diameter": 1.50,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "F",
        "star_subtype": 6,
        "baseMass": 1.26,
        "baseTemp": 6400,
        "diameter": 1.42,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "F",
        "star_subtype": 7,
        "baseMass": 1.22,
        "baseTemp": 6300,
        "diameter": 1.34,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "F",
        "star_subtype": 8,
        "baseMass": 1.18,
        "baseTemp": 6200,
        "diameter": 1.26,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "F",
        "star_subtype": 9,
        "baseMass": 1.14,
        "baseTemp": 6100,
        "diameter": 1.18,
    }
)

# Type G

db.insert(
    {
        "star_class": "V",
        "star_type": "G",
        "star_subtype": 0,
        "baseMass": 1.10,
        "baseTemp": 6000,
        "diameter": 1.10,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "G",
        "star_subtype": 1,
        "baseMass": 1.06,
        "baseTemp": 5920,
        "diameter": 1.07,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "G",
        "star_subtype": 2,
        "baseMass": 1.02,
        "baseTemp": 5840,
        "diameter": 1.04,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "G",
        "star_subtype": 3,
        "baseMass": 0.98,
        "baseTemp": 5760,
        "diameter": 1.01,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "G",
        "star_subtype": 4,
        "baseMass": 0.94,
        "baseTemp": 5680,
        "diameter": 0.98,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "G",
        "star_subtype": 5,
        "baseMass": 0.90,
        "baseTemp": 5600,
        "diameter": 0.95,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "G",
        "star_subtype": 6,
        "baseMass": 0.88,
        "baseTemp": 5520,
        "diameter": 0.94,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "G",
        "star_subtype": 7,
        "baseMass": 0.86,
        "baseTemp": 5440,
        "diameter": 0.93,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "G",
        "star_subtype": 8,
        "baseMass": 0.84,
        "baseTemp": 5360,
        "diameter": 0.92,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "G",
        "star_subtype": 9,
        "baseMass": 0.82,
        "baseTemp": 5280,
        "diameter": 0.91,
    }
)

# Type K

db.insert(
    {
        "star_class": "V",
        "star_type": "K",
        "star_subtype": 0,
        "baseMass": 0.80,
        "baseTemp": 5200,
        "diameter": 0.90,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "K",
        "star_subtype": 1,
        "baseMass": 0.78,
        "baseTemp": 5040,
        "diameter": 0.88,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "K",
        "star_subtype": 2,
        "baseMass": 0.76,
        "baseTemp": 4880,
        "diameter": 0.86,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "K",
        "star_subtype": 3,
        "baseMass": 0.74,
        "baseTemp": 4720,
        "diameter": 0.84,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "K",
        "star_subtype": 4,
        "baseMass": 0.73,
        "baseTemp": 4560,
        "diameter": 0.82,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "K",
        "star_subtype": 5,
        "baseMass": 0.70,
        "baseTemp": 4400,
        "diameter": 0.80,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "K",
        "star_subtype": 6,
        "baseMass": 0.66,
        "baseTemp": 4260,
        "diameter": 0.78,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "K",
        "star_subtype": 7,
        "baseMass": 0.62,
        "baseTemp": 4120,
        "diameter": 0.76,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "K",
        "star_subtype": 8,
        "baseMass": 0.58,
        "baseTemp": 3980,
        "diameter": 0.74,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "K",
        "star_subtype": 9,
        "baseMass": 0.54,
        "baseTemp": 3840,
        "diameter": 0.72,
    }
)

# Type M

db.insert(
    {
        "star_class": "V",
        "star_type": "M",
        "star_subtype": 0,
        "baseMass": 0.50,
        "baseTemp": 3700,
        "diameter": 0.70,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "M",
        "star_subtype": 1,
        "baseMass": 0.43,
        "baseTemp": 3560,
        "diameter": 0.60,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "M",
        "star_subtype": 2,
        "baseMass": 0.37,
        "baseTemp": 3420,
        "diameter": 0.50,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "M",
        "star_subtype": 3,
        "baseMass": 0.30,
        "baseTemp": 3280,
        "diameter": 0.40,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "M",
        "star_subtype": 4,
        "baseMass": 0.23,
        "baseTemp": 3140,
        "diameter": 0.30,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "M",
        "star_subtype": 5,
        "baseMass": 0.16,
        "baseTemp": 3000,
        "diameter": 0.20,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "M",
        "star_subtype": 6,
        "baseMass": 0.14,
        "baseTemp": 2850,
        "diameter": 0.18,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "M",
        "star_subtype": 7,
        "baseMass": 0.12,
        "baseTemp": 2700,
        "diameter": 0.15,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "M",
        "star_subtype": 8,
        "baseMass": 0.10,
        "baseTemp": 2550,
        "diameter": 0.12,
    }
)
db.insert(
    {
        "star_class": "V",
        "star_type": "M",
        "star_subtype": 9,
        "baseMass": 0.08,
        "baseTemp": 2400,
        "diameter": 0.10,
    }
)

# Subdwarf stars (Luminosity class VI)

# Type O

db.insert(
    {
        "star_class": "VI",
        "star_type": "O",
        "star_subtype": 0,
        "baseMass": 2.00,
        "baseTemp": 50000,
        "diameter": 0.18,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "O",
        "star_subtype": 1,
        "baseMass": 1.90,
        "baseTemp": 48000,
        "diameter": 0.18,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "O",
        "star_subtype": 2,
        "baseMass": 1.80,
        "baseTemp": 46000,
        "diameter": 0.18,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "O",
        "star_subtype": 3,
        "baseMass": 1.70,
        "baseTemp": 44000,
        "diameter": 0.18,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "O",
        "star_subtype": 4,
        "baseMass": 1.60,
        "baseTemp": 42000,
        "diameter": 0.18,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "O",
        "star_subtype": 5,
        "baseMass": 1.50,
        "baseTemp": 40000,
        "diameter": 0.18,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "O",
        "star_subtype": 6,
        "baseMass": 1.30,
        "baseTemp": 38000,
        "diameter": 0.18,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "O",
        "star_subtype": 7,
        "baseMass": 1.10,
        "baseTemp": 36000,
        "diameter": 0.19,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "O",
        "star_subtype": 8,
        "baseMass": 0.90,
        "baseTemp": 34000,
        "diameter": 0.19,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "O",
        "star_subtype": 9,
        "baseMass": 0.70,
        "baseTemp": 32000,
        "diameter": 0.19,
    }
)

# Type B

db.insert(
    {
        "star_class": "VI",
        "star_type": "B",
        "star_subtype": 0,
        "baseMass": 0.50,
        "baseTemp": 30000,
        "diameter": 0.20,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "B",
        "star_subtype": 1,
        "baseMass": 0.48,
        "baseTemp": 27000,
        "diameter": 0.26,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "B",
        "star_subtype": 2,
        "baseMass": 0.46,
        "baseTemp": 24000,
        "diameter": 0.32,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "B",
        "star_subtype": 3,
        "baseMass": 0.44,
        "baseTemp": 21000,
        "diameter": 0.38,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "B",
        "star_subtype": 4,
        "baseMass": 0.42,
        "baseTemp": 18000,
        "diameter": 0.44,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "B",
        "star_subtype": 5,
        "baseMass": 0.40,
        "baseTemp": 15000,
        "diameter": 0.50,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "B",
        "star_subtype": 6,
        "baseMass": 0.38,
        "baseTemp": 14000,
        "diameter": 0.56,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "B",
        "star_subtype": 7,
        "baseMass": 0.36,
        "baseTemp": 13000,
        "diameter": 0.62,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "B",
        "star_subtype": 8,
        "baseMass": 0.34,
        "baseTemp": 12000,
        "diameter": 0.68,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "B",
        "star_subtype": 9,
        "baseMass": 0.32,
        "baseTemp": 11000,
        "diameter": 0.74,
    }
)

# Type G

db.insert(
    {
        "star_class": "VI",
        "star_type": "G",
        "star_subtype": 0,
        "baseMass": 0.80,
        "baseTemp": 6000,
        "diameter": 0.80,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "G",
        "star_subtype": 1,
        "baseMass": 0.78,
        "baseTemp": 5920,
        "diameter": 0.78,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "G",
        "star_subtype": 2,
        "baseMass": 0.76,
        "baseTemp": 5840,
        "diameter": 0.76,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "G",
        "star_subtype": 3,
        "baseMass": 0.74,
        "baseTemp": 5760,
        "diameter": 0.74,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "G",
        "star_subtype": 4,
        "baseMass": 0.72,
        "baseTemp": 5680,
        "diameter": 0.72,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "G",
        "star_subtype": 5,
        "baseMass": 0.70,
        "baseTemp": 5600,
        "diameter": 0.70,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "G",
        "star_subtype": 6,
        "baseMass": 0.68,
        "baseTemp": 5520,
        "diameter": 0.68,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "G",
        "star_subtype": 7,
        "baseMass": 0.66,
        "baseTemp": 5440,
        "diameter": 0.66,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "G",
        "star_subtype": 8,
        "baseMass": 0.64,
        "baseTemp": 5360,
        "diameter": 0.64,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "G",
        "star_subtype": 9,
        "baseMass": 0.62,
        "baseTemp": 5280,
        "diameter": 0.62,
    }
)

# Type K

db.insert(
    {
        "star_class": "VI",
        "star_type": "K",
        "star_subtype": 0,
        "baseMass": 0.60,
        "baseTemp": 5200,
        "diameter": 0.60,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "K",
        "star_subtype": 1,
        "baseMass": 0.58,
        "baseTemp": 5040,
        "diameter": 0.56,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "K",
        "star_subtype": 2,
        "baseMass": 0.56,
        "baseTemp": 4880,
        "diameter": 0.56,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "K",
        "star_subtype": 3,
        "baseMass": 0.54,
        "baseTemp": 4720,
        "diameter": 0.54,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "K",
        "star_subtype": 4,
        "baseMass": 0.52,
        "baseTemp": 4560,
        "diameter": 0.52,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "K",
        "star_subtype": 5,
        "baseMass": 0.50,
        "baseTemp": 4400,
        "diameter": 0.50,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "K",
        "star_subtype": 6,
        "baseMass": 0.48,
        "baseTemp": 4260,
        "diameter": 0.48,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "K",
        "star_subtype": 7,
        "baseMass": 0.46,
        "baseTemp": 4120,
        "diameter": 0.46,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "K",
        "star_subtype": 8,
        "baseMass": 0.44,
        "baseTemp": 3980,
        "diameter": 0.44,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "K",
        "star_subtype": 9,
        "baseMass": 0.42,
        "baseTemp": 3840,
        "diameter": 0.42,
    }
)

# Type M

db.insert(
    {
        "star_class": "VI",
        "star_type": "M",
        "star_subtype": 0,
        "baseMass": 0.50,
        "baseTemp": 3700,
        "diameter": 0.40,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "M",
        "star_subtype": 1,
        "baseMass": 0.43,
        "baseTemp": 3560,
        "diameter": 0.344,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "M",
        "star_subtype": 2,
        "baseMass": 0.37,
        "baseTemp": 3420,
        "diameter": 0.288,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "M",
        "star_subtype": 3,
        "baseMass": 0.30,
        "baseTemp": 3280,
        "diameter": 0.232,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "M",
        "star_subtype": 4,
        "baseMass": 0.23,
        "baseTemp": 3140,
        "diameter": 0.176,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "M",
        "star_subtype": 5,
        "baseMass": 0.16,
        "baseTemp": 3000,
        "diameter": 0.120,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "M",
        "star_subtype": 6,
        "baseMass": 0.14,
        "baseTemp": 2850,
        "diameter": 0.109,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "M",
        "star_subtype": 7,
        "baseMass": 0.12,
        "baseTemp": 2700,
        "diameter": 0.098,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "M",
        "star_subtype": 8,
        "baseMass": 0.10,
        "baseTemp": 2550,
        "diameter": 0.086,
    }
)
db.insert(
    {
        "star_class": "VI",
        "star_type": "M",
        "star_subtype": 9,
        "baseMass": 0.08,
        "baseTemp": 2400,
        "diameter": 0.075,
    }
)

# Dwarf stars (Luminosity class D)

# Add star colours

sO = Query()
db.update({"star_colour": "Blue"}, sO.star_type == "O")
db.update({"star_colour": "Blue-White"}, sO.star_type == "B")
db.update({"star_colour": "White"}, sO.star_type == "A")
db.update({"star_colour": "Yellow-White"}, sO.star_type == "F")
db.update({"star_colour": "Yellow"}, sO.star_type == "G")
db.update({"star_colour": "Light Orange"}, sO.star_type == "K")
db.update({"star_colour": "Orange-Red"}, sO.star_type == "M")

print("Loaded " + str(len(db)) + " items.")
