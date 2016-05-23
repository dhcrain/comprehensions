# Remove all vowels from this sentence, List Comprehensions are the Greatest!
sentence = "List Comprehensions are the Greatest!"
vowels = "aeiouAEIOU"
no_vowels = ''.join([letter for letter in sentence if not letter in vowels])
print(no_vowels)

# Create a list of Water Temps for each day the data set below.
import csv

# with open("dataset.csv") as opened_file:
#     data_list = list(csv.reader(opened_file))
# print((data_list))

temps = []
with open('dataset.csv', 'r') as csvfile:
    csvreader = (csv.reader(csvfile))
    # This skips the first row of the CSV file.
    next(csvreader)
    # for row in csvreader:
    #     temps.append(row[4])
    temps = [row[4] for row in csvreader]
print(temps)
