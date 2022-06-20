# Saving and loading in Python 3

import pickle
import os
os.system("clear")

# List
names = ["Angus Young", "Malcolm Young", "Bon Scott"]

print("Original List:")
print(names)

# Save List
pickle.dump(names, open("names.txt", "wb"))

# Change
names.remove("Bon Scott")

print("Changed List")
print(names)

# Load
names = pickle.load(open("names.txt", "rb"))
print("Original List")
print(names)