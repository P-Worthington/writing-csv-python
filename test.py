import csv

# r read w write
with open('names.csv', 'r') as csv_file:
    #must use reader not DictReader 
    csv_reader = csv.reader(csv_file)

    #to step over first value usually the key 
    next(csv_reader)

    # 2 is the index will only print email
    for line in csv_reader:
        print(line[2])

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)