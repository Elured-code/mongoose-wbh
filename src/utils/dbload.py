from tinydb import TinyDB, Query


db = TinyDB('db.json')

print('Clearing database')

db.truncate()

# Bright Supergiants (Luminosity Class I / Ia)
# Type O

# Main sequence stars

# Type G

db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 0, 'baseMass': 1.1})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 1, 'baseMass': 1.06})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 2, 'baseMass': 1.02})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 3, 'baseMass': 0.98})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 4, 'baseMass': 0.94})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 5, 'baseMass': 0.9})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 6, 'baseMass': 0.88})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 7, 'baseMass': 0.86})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 8, 'baseMass': 0.84})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 9, 'baseMass': 0.82})

# Type K

db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 0, 'baseMass': 0.8})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 1, 'baseMass': 0.78})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 2, 'baseMass': 0.76})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 3, 'baseMass': 0.74})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 4, 'baseMass': 0.73})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 5, 'baseMass': 0.7})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 6, 'baseMass': 0.66})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 7, 'baseMass': 0.62})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 8, 'baseMass': 0.58})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 9, 'baseMass': 0.54})

# Type M

db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 0, 'baseMass': 0.5})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 1, 'baseMass': 0.432})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 2, 'baseMass': 0.364})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 3, 'baseMass': 0.296})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 4, 'baseMass': 0.228})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 5, 'baseMass': 0.16})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 6, 'baseMass': 0.14})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 7, 'baseMass': 0.12})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 8, 'baseMass': 0.1})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 9, 'baseMass': 0.08})

print('Loaded ' + str(len(db)) + ' items.')
