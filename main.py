
import csv

f = open('updated_AB_NYC_2019.csv', 'w')
writer = csv.writer(f)

with open('AB_NYC_2019.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if '\n' in row[1]:
            print(f'\t anomaly found in ID {row[0]}')
            updated_value = row[1].replace('\n', '')
            row[1] = updated_value
        writer.writerow(row)

# close the file
f.close()
