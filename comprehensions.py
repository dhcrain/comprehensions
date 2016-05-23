# Remove all vowels from this sentence, List Comprehensions are the Greatest!
sentence = "List Comprehensions are the Greatest!"
vowels = "aeiouAEIOU"
no_vowels = ''.join([letter for letter in sentence if not letter in vowels])
print(no_vowels)

# Create a list of Water Temps for each day the data set below.

with open("dataset") as opened_file:
    data = opened_file.read()

