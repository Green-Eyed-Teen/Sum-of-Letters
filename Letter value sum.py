print("Note: This program will help you in calculating the Sum of all Letters in 1 word!")

# Importing
from ModuleCalculation import calculation

# 'Total' variable gets the sum of the characters and 'word' gets the "word" that the user enters.
total, word = calculation()

print(f"The total sum of every letter in {word} is {total}")
