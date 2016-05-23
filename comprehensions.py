# Remove all vowels from this sentence, List Comprehensions are the Greatest!
sentence = "List Comprehensions are the Greatest!"
vowels = "aeiouAEIOU"
no_vowels = ''.join([letter for letter in sentence if not letter in vowels])
# print(no_vowels)

# Create a list of Water Temps for each day the data set below.
import csv

# with open("dataset.csv") as opened_file:
#     data_list = list(csv.reader(opened_file))
# print((data_list))

# with open('dataset.csv', 'r') as csvfile:
#     data_set = csvfile.readlines()
# print("Read Lines: ", data_set)

with open('dataset.csv', 'r') as csvfile:
    csvreader = (csv.reader(csvfile))
    next(csvreader)     # This skips the first row of the CSV file.
    # for row in csvreader:
    #     temps.append(row[4])
    temps = [row[4] for row in csvreader]
# print("Temps: ", temps)

# Convert the Water Temps from a string to a float
float_temps = [float (item) for item in temps]
# print("Temps in Floats: ", float_temps)

# Convert the Water Temps from Celsius to Fahrenheit rounded to an int
temps_f = [int(item * (9/5) + 32) for item in float_temps]
# print("temps in F: ", temps_f)

# Create a dictionary with Date as the key and Wave Height as the value
# date_wave = []
# with open('dataset.csv', 'r') as csvfile:
#     data_set2 = list(csv.reader(csvfile))
#     # date_wave = {data_set2[5][4] for index, row in (data_set2)}
#     for index in data_set2:
#         date_wave.append(data_set2[5])
# print("Date/Wave: ", date_wave)

with open('dataset.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row[Date], row[1])