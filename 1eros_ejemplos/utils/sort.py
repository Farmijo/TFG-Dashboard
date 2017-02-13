import csv

with open('file.csv', 'r') as infile, open('reordered.csv', 'a') as outfile:
    # output dict needs a list for new column ordering
    fieldnames = ['A', 'C', 'D', 'E', 'B']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    # reorder the header first
    writer.writeheader()
    for row in csv.DictReader(infile):
        # writes the reordered rows to the new file
        writer.writerow(row)