from tinydb import TinyDB, Query, where


db = TinyDB('db.json')

print('Clearing database')

db.truncate()

# Bright Supergiants (Luminosity Class I / Ia)

# Type O

db.insert({'starClass': 'Ia', 'starType': 'O', 'starSubType': 0, 'baseMass': 200.0, 'baseTemp': 50000, 'diameter': 25.0})
db.insert({'starClass': 'Ia', 'starType': 'O', 'starSubType': 1, 'baseMass': 176.0, 'baseTemp': 48000, 'diameter': 24.4})
db.insert({'starClass': 'Ia', 'starType': 'O', 'starSubType': 2, 'baseMass': 152.0, 'baseTemp': 46000, 'diameter': 23.8})
db.insert({'starClass': 'Ia', 'starType': 'O', 'starSubType': 3, 'baseMass': 128.0, 'baseTemp': 44000, 'diameter': 23.2})
db.insert({'starClass': 'Ia', 'starType': 'O', 'starSubType': 4, 'baseMass': 104.0, 'baseTemp': 42000, 'diameter': 22.6})
db.insert({'starClass': 'Ia', 'starType': 'O', 'starSubType': 5, 'baseMass': 80.0, 'baseTemp': 40000, 'diameter': 22.0})
db.insert({'starClass': 'Ia', 'starType': 'O', 'starSubType': 6, 'baseMass': 75.0, 'baseTemp': 38000, 'diameter': 21.6})
db.insert({'starClass': 'Ia', 'starType': 'O', 'starSubType': 7, 'baseMass': 70.0, 'baseTemp': 36000, 'diameter': 21.2})
db.insert({'starClass': 'Ia', 'starType': 'O', 'starSubType': 8, 'baseMass': 65.0, 'baseTemp': 34000, 'diameter': 20.8})
db.insert({'starClass': 'Ia', 'starType': 'O', 'starSubType': 9, 'baseMass': 60.0, 'baseTemp': 32000, 'diameter': 20.4})

# Bright Supergiants (Luminosity Class Ib)

# Supergiants (Luminosity Class II)

# Giants (Luminosity Class III)

# Subgiants (Luminosity Class IV)

# Type B

db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 0, 'baseMass': 20.0, 'baseTemp': 30000, 'diameter': 8.00})
db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 1, 'baseMass': 18.0, 'baseTemp': 27000, 'diameter': 7.40})
db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 2, 'baseMass': 16.0, 'baseTemp': 24000, 'diameter': 6.80})
db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 3, 'baseMass': 14.0, 'baseTemp': 21000, 'diameter': 6.20})
db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 4, 'baseMass': 12.0, 'baseTemp': 18000, 'diameter': 5.60})
db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 5, 'baseMass': 10.0, 'baseTemp': 15000, 'diameter': 8.00})
db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 6, 'baseMass': 8.80, 'baseTemp': 14000, 'diameter': 4.80})
db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 7, 'baseMass': 7.60, 'baseTemp': 13000, 'diameter': 4.60})
db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 8, 'baseMass': 6.40, 'baseTemp': 12000, 'diameter': 4.40})
db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 9, 'baseMass': 5.20, 'baseTemp': 11000, 'diameter': 4.20})


# Type A

db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 0, 'baseMass': 4.00, 'baseTemp': 10000, 'diameter': 4.00})
db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 1, 'baseMass': 3.66, 'baseTemp': 9600, 'diameter': 3.80})
db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 2, 'baseMass': 3.32, 'baseTemp': 9200, 'diameter': 3.60})
db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 3, 'baseMass': 2.98, 'baseTemp': 8800, 'diameter': 3.40})
db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 4, 'baseMass': 2.64, 'baseTemp': 8400, 'diameter': 3.20})
db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 5, 'baseMass': 2.30, 'baseTemp': 8000, 'diameter': 3.00})
db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 6, 'baseMass': 2.24, 'baseTemp': 7900, 'diameter': 2.90})
db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 7, 'baseMass': 2.18, 'baseTemp': 7800, 'diameter': 2.80})
db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 8, 'baseMass': 2.12, 'baseTemp': 7700, 'diameter': 2.80})
db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 9, 'baseMass': 2.06, 'baseTemp': 7600, 'diameter': 2.90})

# Type F

db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 0, 'baseMass': 2.00, 'baseTemp': 7500, 'diameter': 4.00})
db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 1, 'baseMass': 1.90, 'baseTemp': 7300, 'diameter': 3.80})
db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 2, 'baseMass': 1.80, 'baseTemp': 7100, 'diameter': 3.60})
db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 3, 'baseMass': 1.70, 'baseTemp': 6900, 'diameter': 3.40})
db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 4, 'baseMass': 1.60, 'baseTemp': 6700, 'diameter': 3.20})
db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 5, 'baseMass': 1.50, 'baseTemp': 6500, 'diameter': 3.00})
db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 6, 'baseMass': 1.40, 'baseTemp': 6400, 'diameter': 3.00})
db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 7, 'baseMass': 1.40, 'baseTemp': 6300, 'diameter': 3.00})
db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 8, 'baseMass': 1.50, 'baseTemp': 6200, 'diameter': 3.00})
db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 9, 'baseMass': 1.60, 'baseTemp': 6100, 'diameter': 3.00})

# Type G

db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 0, 'baseMass': 1.70, 'baseTemp': 6000, 'diameter': 3.00})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 1, 'baseMass': 1.52, 'baseTemp': 5920, 'diameter': 3.20})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 2, 'baseMass': 1.44, 'baseTemp': 5840, 'diameter': 3.40})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 3, 'baseMass': 1.36, 'baseTemp': 5760, 'diameter': 3.60})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 4, 'baseMass': 1.28, 'baseTemp': 5680, 'diameter': 3.80})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 5, 'baseMass': 1.20, 'baseTemp': 5600, 'diameter': 4.00})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 6, 'baseMass': 1.26, 'baseTemp': 5520, 'diameter': 4.40})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 7, 'baseMass': 1.32, 'baseTemp': 5440, 'diameter': 4.80})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 8, 'baseMass': 1.38, 'baseTemp': 5360, 'diameter': 5.20})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 9, 'baseMass': 1.44, 'baseTemp': 5280, 'diameter': 5.60})

# Type K

db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 0, 'baseMass': 1.50, 'baseTemp': 5200, 'diameter': 6.00})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 1, 'baseMass': 1.56, 'baseTemp': 5040, 'diameter': 3.80})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 2, 'baseMass': 1.62, 'baseTemp': 4880, 'diameter': 3.60})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 3, 'baseMass': 1.68, 'baseTemp': 4720, 'diameter': 3.40})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 4, 'baseMass': 1.74, 'baseTemp': 4560, 'diameter': 3.20})


# Main sequence stars (Luminosity Class V)

# Type O

db.insert({'starClass': 'V', 'starType': 'O', 'starSubType': 0, 'baseMass': 90.0, 'baseTemp': 50000, 'diameter': 20.0})
db.insert({'starClass': 'V', 'starType': 'O', 'starSubType': 1, 'baseMass': 84.0, 'baseTemp': 48000, 'diameter': 18.4})
db.insert({'starClass': 'V', 'starType': 'O', 'starSubType': 2, 'baseMass': 78.0, 'baseTemp': 46000, 'diameter': 16.8})
db.insert({'starClass': 'V', 'starType': 'O', 'starSubType': 3, 'baseMass': 72.0, 'baseTemp': 44000, 'diameter': 15.2})
db.insert({'starClass': 'V', 'starType': 'O', 'starSubType': 4, 'baseMass': 66.0, 'baseTemp': 42000, 'diameter': 13.6})
db.insert({'starClass': 'V', 'starType': 'O', 'starSubType': 5, 'baseMass': 60.0, 'baseTemp': 40000, 'diameter': 12.0})
db.insert({'starClass': 'V', 'starType': 'O', 'starSubType': 6, 'baseMass': 51.6, 'baseTemp': 38000, 'diameter': 3.24})
db.insert({'starClass': 'V', 'starType': 'O', 'starSubType': 7, 'baseMass': 43.2, 'baseTemp': 36000, 'diameter': 2.98})
db.insert({'starClass': 'V', 'starType': 'O', 'starSubType': 8, 'baseMass': 34.8, 'baseTemp': 34000, 'diameter': 2.72})
db.insert({'starClass': 'V', 'starType': 'O', 'starSubType': 9, 'baseMass': 25.4, 'baseTemp': 32000, 'diameter': 2.46})

# Type B

db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 0, 'baseMass': 18.0, 'baseTemp': 30000, 'diameter': 7.00})
db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 1, 'baseMass': 15.4, 'baseTemp': 27000, 'diameter': 6.30})
db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 2, 'baseMass': 12.8, 'baseTemp': 24000, 'diameter': 5.60})
db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 3, 'baseMass': 10.2, 'baseTemp': 21000, 'diameter': 4.90})
db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 4, 'baseMass': 7.60, 'baseTemp': 18000, 'diameter': 4.20})
db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 5, 'baseMass': 5.00, 'baseTemp': 15000, 'diameter': 3.50})
db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 6, 'baseMass': 4.44, 'baseTemp': 14000, 'diameter': 3.24})
db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 7, 'baseMass': 3.88, 'baseTemp': 13000, 'diameter': 2.98})
db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 8, 'baseMass': 3.32, 'baseTemp': 12000, 'diameter': 2.72})
db.insert({'starClass': 'V', 'starType': 'B', 'starSubType': 9, 'baseMass': 2.76, 'baseTemp': 11000, 'diameter': 2.46})

# Type A

db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 0, 'baseMass': 2.20, 'baseTemp': 10000, 'diameter': 2.20})
db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 1, 'baseMass': 2.12, 'baseTemp': 9600, 'diameter': 2.16})
db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 2, 'baseMass': 2.04, 'baseTemp': 9200, 'diameter': 2.12})
db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 3, 'baseMass': 1.98, 'baseTemp': 8800, 'diameter': 2.08})
db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 4, 'baseMass': 1.88, 'baseTemp': 8400, 'diameter': 2.04})
db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 5, 'baseMass': 1.80, 'baseTemp': 8000, 'diameter': 2.00})
db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 6, 'baseMass': 1.74, 'baseTemp': 7600, 'diameter': 2.10})
db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 7, 'baseMass': 1.68, 'baseTemp': 7200, 'diameter': 2.00})
db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 8, 'baseMass': 1.62, 'baseTemp': 6800, 'diameter': 1.90})
db.insert({'starClass': 'V', 'starType': 'A', 'starSubType': 9, 'baseMass': 1.56, 'baseTemp': 6400, 'diameter': 1.80})

# Type F

db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 0, 'baseMass': 1.50, 'baseTemp': 7500, 'diameter': 1.70})
db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 1, 'baseMass': 1.46, 'baseTemp': 7300, 'diameter': 1.66})
db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 2, 'baseMass': 1.42, 'baseTemp': 7100, 'diameter': 1.62})
db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 3, 'baseMass': 1.38, 'baseTemp': 6900, 'diameter': 1.58})
db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 4, 'baseMass': 1.34, 'baseTemp': 6700, 'diameter': 1.54})
db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 5, 'baseMass': 1.30, 'baseTemp': 6500, 'diameter': 1.50})
db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 6, 'baseMass': 1.26, 'baseTemp': 6400, 'diameter': 1.42})
db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 7, 'baseMass': 1.22, 'baseTemp': 6300, 'diameter': 1.34})
db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 8, 'baseMass': 1.18, 'baseTemp': 6200, 'diameter': 1.26})
db.insert({'starClass': 'V', 'starType': 'F', 'starSubType': 9, 'baseMass': 1.14, 'baseTemp': 6100, 'diameter': 1.18})

# Type G

db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 0, 'baseMass': 1.10, 'baseTemp': 6000, 'diameter': 1.10})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 1, 'baseMass': 1.06, 'baseTemp': 5920, 'diameter': 1.07})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 2, 'baseMass': 1.02, 'baseTemp': 5840, 'diameter': 1.04})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 3, 'baseMass': 0.98, 'baseTemp': 5760, 'diameter': 1.01})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 4, 'baseMass': 0.94, 'baseTemp': 5680, 'diameter': 0.98})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 5, 'baseMass': 0.90, 'baseTemp': 5600, 'diameter': 0.95})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 6, 'baseMass': 0.88, 'baseTemp': 5520, 'diameter': 0.94})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 7, 'baseMass': 0.86, 'baseTemp': 5440, 'diameter': 0.93})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 8, 'baseMass': 0.84, 'baseTemp': 5360, 'diameter': 0.92})
db.insert({'starClass': 'V', 'starType': 'G', 'starSubType': 9, 'baseMass': 0.82, 'baseTemp': 5280, 'diameter': 0.91})

# Type K

db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 0, 'baseMass': 0.80, 'baseTemp': 5200, 'diameter': 0.90})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 1, 'baseMass': 0.78, 'baseTemp': 5040, 'diameter': 0.88})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 2, 'baseMass': 0.76, 'baseTemp': 4880, 'diameter': 0.86})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 3, 'baseMass': 0.74, 'baseTemp': 4720, 'diameter': 0.84})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 4, 'baseMass': 0.73, 'baseTemp': 4560, 'diameter': 0.82})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 5, 'baseMass': 0.70, 'baseTemp': 4400, 'diameter': 0.80})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 6, 'baseMass': 0.66, 'baseTemp': 4260, 'diameter': 0.78})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 7, 'baseMass': 0.62, 'baseTemp': 4120, 'diameter': 0.76})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 8, 'baseMass': 0.58, 'baseTemp': 3980, 'diameter': 0.74})
db.insert({'starClass': 'V', 'starType': 'K', 'starSubType': 9, 'baseMass': 0.54, 'baseTemp': 3840, 'diameter': 0.72})

# Type M

db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 0, 'baseMass': 0.50, 'baseTemp': 3700, 'diameter': 0.70})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 1, 'baseMass': 0.43, 'baseTemp': 3560, 'diameter': 0.60})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 2, 'baseMass': 0.37, 'baseTemp': 3420, 'diameter': 0.50})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 3, 'baseMass': 0.30, 'baseTemp': 3280, 'diameter': 0.40})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 4, 'baseMass': 0.23, 'baseTemp': 3140, 'diameter': 0.30})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 5, 'baseMass': 0.16, 'baseTemp': 3000, 'diameter': 0.20})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 6, 'baseMass': 0.14, 'baseTemp': 2850, 'diameter': 0.18})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 7, 'baseMass': 0.12, 'baseTemp': 2700, 'diameter': 0.15})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 8, 'baseMass': 0.10, 'baseTemp': 2550, 'diameter': 0.12})
db.insert({'starClass': 'V', 'starType': 'M', 'starSubType': 9, 'baseMass': 0.08, 'baseTemp': 2400, 'diameter': 0.10})

# Subdwarf stars (Luminosity class VI)

# Dwarf stars (Luminosity class D)

# Add star colours

sO = Query()
db.update({'starColour': 'Blue'}, sO.starType == 'O')
db.update({'starColour': 'Blue-White'}, sO.starType == 'B')
db.update({'starColour': 'White'}, sO.starType == 'A')
db.update({'starColour': 'Yellow-White'}, sO.starType == 'F')
db.update({'starColour': 'Yellow'}, sO.starType == 'G')
db.update({'starColour': 'Light Orange'}, sO.starType == 'K')
db.update({'starColour': 'Orange-Red'}, sO.starType == 'M')







print('Loaded ' + str(len(db)) + ' items.')
