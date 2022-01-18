import csv

test_for = []

test_against = []

with open('AssetList.txt') as csv_file:
    first_csv_reader = csv.reader(csv_file, delimiter=',')
    first_line_count = 0
    for row in first_csv_reader:
        if first_line_count == 0:
            print(f'Column names are {", ".join(row)}')
            first_line_count =+ 1
        else:
            test_for.append(row[0])
            print(test_for)

with open('Mobility.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        elif line_count != 0:
            for i in test_for:
                if i == row[0]:
                    print(f'matchfound {i}')
           # print(f'\t{row[0]} is associated {row[1]} userNumber, and has product ID {row[5]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
