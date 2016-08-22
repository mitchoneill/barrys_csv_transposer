import csv
from collections import defaultdict

# Put this script in the same folder as the csv folder
# Set CSV_FILE the same of the CSV file
CSV_FILE = 'example.csv'

# Name of the heading with the ID
ID_HEADING = 'ID'

# Name of the heading with the date
DATE_HEADING = 'DATE'

# Set this to true if you want to see the dictionary output.
# Dictionaries are formatted as {'key1': 'output1', 'key2': 'output2'...}
# So you'll see the output as {'ID1': ['date1', 'date2'...], 'ID2': ['date3, date4...],  ...}
# If you're processing a large file then turn this to false as you don't want
# to output that big dictionary file, it's just fun to look at
DICTIONARY_OUTPUT = True

# This is a basic usage of the CSV module which can be
# found at https://docs.python.org/3/library/csv.html

with open(CSV_FILE, newline='') as csvfile:
    reader = csv.reader(csvfile)
    have_read_columns = False

# Default dictionaries are great when you don't know if a key exists yet or not,
# you can just assume the key does exist and the (list) part means we can also
# assume the value will be a list no matter what
# https://docs.python.org/3/library/collections.html#collections.defaultdict

    result = defaultdict(list)

# Now we're going to read the input csv file row by row and make the ID the
# key of our results list, and the values and ever growing list of DATES

    for row in reader:

        # The first row will be the column names, so we need to find out
        # which column the ID and DATE is in. idx is just short for index

        if have_read_columns is False:
            id_idx = row.index(ID_HEADING)
            date_idx = row.index(DATE_HEADING)
            have_read_columns = True

        # Now when we read a row from the csv file, we want to get the value
        # in the column of our ID (the row[id_idx]) and make the our key,
        # then add the date to the ever growing list of dates attached to
        # that key
 
        else:
            result[row[id_idx]].append(row[date_idx])

if DICTIONARY_OUTPUT:
    print(result)

# Now we have to write the output file, our new file will have the same
# filename as the input file but will have 'processed-' at the start of it
# (dont worry the old file doesnt get deleted).
# For each key (ie. ID) we have we're going to write that to the first column
# of each row and then its dates to the other columns

with open('processed-' + CSV_FILE, 'w') as csvfile:
    writer = csv.writer(csvfile)
    for key, value in result.items():
        writer.writerow([key] + value)
