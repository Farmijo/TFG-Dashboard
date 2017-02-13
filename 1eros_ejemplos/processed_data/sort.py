import csv

reader = csv.DictReader(open('processed_freq_signDowns.csv', 'r'))
result = sorted(reader, key=lambda d: float(d['fecha']))

writer = csv.DictWriter(open('output.csv', 'w'), reader.fieldnames)
writer.writeheader()
writer.writerows(result)