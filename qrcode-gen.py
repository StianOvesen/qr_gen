### WRITTEN BY:
### STIAN OVESEN

import csv
import qrcode.image.pil
import os



### DELETE PREVIOUS QR-CODES
dir = ('codes')

for file in os.listdir(dir):
    os.remove(os.path.join(dir, file))


### OPEN CSV AND GENERATE QR-CODES.
factory = qrcode.image.pil.PilImage


with open('objects.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=';')
    for line in csvReader:
        guid, number, filename = line
        # generate the QR code SVG using the url
        img = qrcode.make(guid, image_factory=factory)
        img.save(f'codes/{number} {filename}.png')
        print(f'{filename}.svg created with {guid} guid')

