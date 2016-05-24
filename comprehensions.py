

# Remove all vowels from this sentence, List Comprehensions are the Greatest!
def devowel(words):
    vowels = "aeiouAEIOU"
    return ''.join([letter for letter in words if not letter in vowels])
sentence = "List Comprehensions are the Greatest!"
print(devowel(sentence))

# Create a list of Water Temps for each day the data set below.
import csv


def water_temp(data_file_csv):
    with open(data_file_csv, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # This skips the first row of the CSV file.
        return [row[4] for row in csvreader]
print("Temps -", water_temp("dataset.csv"))


# Convert the Water Temps from a string to a float
def string_float(strings):
    return [float(item) for item in strings]
temps = water_temp("dataset.csv")
print("Temps as Floats -", string_float(temps))


# Convert the Water Temps from Celsius to Fahrenheit rounded to an int
def c_f(c):
    return [int(item * (9/5) + 32) for item in c]
temps_in_c = string_float(temps)
print("Temps in F -", c_f(temps_in_c))


def date_wave_dict(data_csv):
    with open(data_csv) as csvfile:
        reader = csv.DictReader(csvfile)
        return (dict((line_dict["Date"], line_dict["Wave Height"]) for line_dict in reader))
    # print("Date: Wave Height", date_wave)
print("Date: Wave Height -", date_wave_dict('dataset.csv'))


# Create a dictionary with the average wave height for each day of the week
import statistics
import datetime
from collections import defaultdict

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def get_dow(date_string):
    return days[datetime.datetime.strptime(date_string, "%Y-%m-%d").weekday()]


def day_avg(datewavedict):
    my_wave_data = defaultdict(list)
    for date, wave in datewavedict.items():
        my_wave_data[get_dow(date)].append(float(wave))
    return {days_w: statistics.mean(waves) for days_w, waves in my_wave_data.items()}
date_wave = date_wave_dict('dataset.csv')
print("Day: Avg wave height -", day_avg(date_wave))


# Create a nested comprehension to get the average of the Homework 1 grades.
homework = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
            'Jordan': {'Homework 1': 92, 'Homework 2': 87},
            'Peyton': {'Homework 1': 84, 'Homework 2': 77},
            'River': {'Homework 1': 85, 'Homework 2': 91}
            }


def hwavg(data):
    return statistics.mean([data[person]['Homework 1'] for person in data])
print("HW 1 Average -", hwavg(homework))
