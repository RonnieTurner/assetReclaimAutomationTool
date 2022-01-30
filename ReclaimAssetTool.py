import csv

test_for = []

work_order = []

test_against = []
# AssetList.txt is csv file pulled from excel spreadshet, info is entered
# directly from Asset Reclaim lists
with open('Asset Reclaim List.txt') as csv_file:
    first_csv_reader = csv.reader(csv_file, delimiter=',')
    first_line_count = 0
    for row in first_csv_reader:
        if first_line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            first_line_count =+ 1
        else:
            test_for.append(row[0])
            work_order.append(row[2])
            # print(test_for)
            # print(work_order)

with open('Mobility.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
        elif line_count != 0:
            for i in test_for:
                if i == row[0]:
                    # index = test_for.index(i)
                    print(f'____MATCH!____ AB: {i} ---- Workorder: {work_order[test_for.index(i)]}')
                    
           # print(f'\t{row[0]} is associated {row[1]} userNumber, and has product ID {row[5]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
