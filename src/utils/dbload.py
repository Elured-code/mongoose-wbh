from tinydb import TinyDB, Query


db = TinyDB('db.json')

print('Clearing database')

db.truncate()

# Bright Supergiants (Luminosity Class I / Ia)
# Type O

# Main sequence stars

# Type G

db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 0, 'baseMass': 1.1, 'baseTemp': 6000})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 1, 'baseMass': 1.06, 'baseTemp': 5920})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 2, 'baseMass': 1.02, 'baseTemp': 5840})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 3, 'baseMass': 0.98, 'baseTemp': 5760})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 4, 'baseMass': 0.94, 'baseTemp': 5680})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 5, 'baseMass': 0.9, 'baseTemp': 5600})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 6, 'baseMass': 0.88, 'baseTemp': 5520})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 7, 'baseMass': 0.86, 'baseTemp': 5440})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 8, 'baseMass': 0.84, 'baseTemp': 5360})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 9, 'baseMass': 0.82, 'baseTemp': 5280})

# Type K

db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 0, 'baseMass': 0.8, 'baseTemp': 5200})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 1, 'baseMass': 0.78, 'baseTemp': 5040})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 2, 'baseMass': 0.76, 'baseTemp': 4880})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 3, 'baseMass': 0.74, 'baseTemp': 4720})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 4, 'baseMass': 0.73, 'baseTemp': 4560})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 5, 'baseMass': 0.7, 'baseTemp': 4400})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 6, 'baseMass': 0.66, 'baseTemp': 4260})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 7, 'baseMass': 0.62, 'baseTemp': 4120})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 8, 'baseMass': 0.58, 'baseTemp': 3980})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 9, 'baseMass': 0.54, 'baseTemp': 3840})

# Type M

db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 0, 'baseMass': 0.5, 'baseTemp': 3700})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 1, 'baseMass': 0.432, 'baseTemp': 3560})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 2, 'baseMass': 0.364, 'baseTemp': 3420})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 3, 'baseMass': 0.296, 'baseTemp': 3280})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 4, 'baseMass': 0.228, 'baseTemp': 3140})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 5, 'baseMass': 0.16, 'baseTemp': 3000})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 6, 'baseMass': 0.14, 'baseTemp': 2850})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 7, 'baseMass': 0.12, 'baseTemp': 2700})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 8, 'baseMass': 0.1, 'baseTemp': 2550})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 9, 'baseMass': 0.08, 'baseTemp': 2400})

print('Loaded ' + str(len(db)) + ' items.')
