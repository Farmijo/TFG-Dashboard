import csv

reader = csv.DictReader(open('result.csv', 'r'))
result = sorted(reader, key=lambda d: float(d['fecha']))

writer = csv.DictWriter(open('output.csv', 'w'), reader.fieldnames)
writer.writeheader()
writer.writerows(result)