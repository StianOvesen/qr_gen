import csv
import qrcode
import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage

with open('objects.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=';')
    for line in csvReader:
        guid, filename = line
        # generate the QR code SVG using the url
        img = qrcode.make(guid, image_factory=factory)
        img.save(f'codes/{filename}.svg')
        print(f'{filename}.svg created with {guid} guid')