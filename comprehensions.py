

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
import statistics
import datetime
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_dow(date_string):
    return days[datetime.datetime.strptime(date_string, "%Y-%m-%d").weekday()]


for date, wave in date_wave.items():
    day_wave = (get_dow(date), wave)
    day_wave = (list(day_wave))
    print(day_wave)
    a, b = day_wave
    # print(a)
    # print(b)

from collections import defaultdict
my_wave_data = defaultdict(list)

for day in a.split(" "):
    for wave in b.split(" "):
        my_wave_data[day].append(string_float(wave)

print(my_wave_data)

# print({get_dow(date): wave for date, wave in date_wave.items()})


# print([get_dow(date) for date in dates])


# avg_h = {day_week: wave[index] for index, day in enumerate(day_week)}
# print(list(enumerate(headers)))
# print(avg_h)

# get average for all of the same keys?
# dict = {day: mean(append(height))}?








# Create a nested comprehension to get the average of the Homework 1 grades.

homework = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
            'Jordan': {'Homework 1': 92, 'Homework 2': 87},
            'Peyton': {'Homework 1': 84, 'Homework 2': 77},
            'River': {'Homework 1': 85, 'Homework 2': 91}
            }


def hwavg(data):
    return statistics.mean([data[person]['Homework 1'] for person in data])
# print(hwavg(homework))
