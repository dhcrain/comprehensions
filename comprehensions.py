

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
# Sun: 2.5, Mon: 2.6......

from enum import Enum


# Find day of the week in python 3
# https://gist.github.com/taddeimania/765fcc32fef6399eddd2
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

wave = []
day = []
for wave_h in date_wave:
    wave.append(date_wave[wave_h])
for date in date_wave:
    sdate = date.split("-")
    day.append(get_day_of_week(int(sdate[0]), int(sdate[1]), int(sdate[2])))

wave_list = (string_float(wave))
# print(day)
zipped = zip(day, wave_list)
daywave = list(zipped)
print(daywave)







# avg_h = {day_week: wave[index] for index, day in enumerate(day_week)}
# print(list(enumerate(headers)))
# print(avg_h)

# get average for all of the same keys?




# Create a nested comprehension to get the average of the Homework 1 grades.
homework = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
            'Jordan': {'Homework 1': 92, 'Homework 2': 87},
            'Peyton': {'Homework 1': 84, 'Homework 2': 77},
            'River': {'Homework 1': 85, 'Homework 2': 91}
            }


# I don't know how to do this as a nested comprehension, but I can do it like this!
def hwavg(data):
    grades = [data[person]['Homework 1'] for person in data]
    hw1_avg = ((sum(grades)) / len(homework))
    return hw1_avg
# print(hwavg(homework))
