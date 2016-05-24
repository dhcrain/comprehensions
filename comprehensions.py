# Remove all vowels from this sentence, List Comprehensions are the Greatest!


def devowel(words):
    vowels = "aeiouAEIOU"
    no_vowels = ''.join([letter for letter in words if not letter in vowels])
    return no_vowels
sentence = "List Comprehensions are the Greatest!"
# print(devowel(sentence))

# Create a list of Water Temps for each day the data set below.
import csv

with open('dataset.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    temps = next(csvreader)     # This skips the first row of the CSV file.
    temps = [row[4] for row in csvreader]
temperatures = temps
# print("Temps: ", temperatures)


# Convert the Water Temps from a string to a float
def string_float(strings):
    float_temps = [float(item) for item in strings]
    return float_temps
temps_in_c = string_float(temperatures)
# print("Temps as Floats: ", temps_in_c)


# Convert the Water Temps from Celsius to Fahrenheit rounded to an int
def c_f(c):
    temps_f = [int(item * (9/5) + 32) for item in c]
    return temps_f
# print("Temps in F: ", c_f(temps_in_c))

# Create a dictionary with Date as the key and Wave Height as the value
with open('dataset.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    date_wave = (dict((line_dict["Date"], line_dict["Wave Height"]) for line_dict in reader))
# print("Date: Wave Height", date_wave)



# Create a dictionary with the average wave height for each day of the week
# https://docs.python.org/3/library/datetime.html
# Sun: 2.5, Mon: 2.6......

# Find day of the week in python 3
# https://gist.github.com/taddeimania/765fcc32fef6399eddd2
from enum import Enum
import datetime

class DayOfWeek(Enum):
    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6


def get_day_of_week(year, month, day):
    month_table = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= 1 if month < 3 else 0
    return DayOfWeek(int((year + year / 4 - year / 100 + year / 400 + month_table[month - 1] + day) % 7))



# for wave_h in date_wave:
#     print(date_wave[wave_h])
for date in date_wave:
    sdate = date.split("-")
    day_week = get_day_of_week(int(sdate[0]), int(sdate[1]), int(sdate[2]))
    # print(day_week)
# make a dict of week day and wave height
# get average for all of the same keys?

# Create a nested comprehension to get the average of the Homework 1 grades.
homework = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
            'Jordan': {'Homework 1': 92, 'Homework 2': 87},
            'Peyton': {'Homework 1': 84, 'Homework 2': 77},
            'River': {'Homework 1': 85, 'Homework 2': 91}
            }
print(homework[person]['Homework 1'])
for person in enumerate(homework.items()):
    # print(homework[person]['Homework 1'])
    print(person)
    for k in person[1].items():
        print(k)

    # print(person)

# hw1_avg = value of 'homework 1' / len(homework)