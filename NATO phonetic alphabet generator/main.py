# importing the required libraries
import pandas as pd

# reading the csv containing the NATO phnetic alphabets
alphabet_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")

# creating a dictionary using the DataFrame
alphabet_dict  = {row.letter:row.code for (index, row) in alphabet_data_frame.iterrows()}
print(alphabet_dict)

# Asking the user for a string to be converted into its corresponding Phonetic form
input_string = input(" input the string to be converted to NATO phonetics:").upper()
phonetic_list = [alphabet_dict[alphabet] for alphabet in input_string]
print(phonetic_list)

