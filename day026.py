# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

#todo  1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#todo 2. Create a list of the phonetic code words from a word that the user inputs.
import pandas
import csv

data = pandas.read_csv("100days/day026_nato_phonetic_alphabet.csv")


newdict = {row.letter:row.code for (index,row) in data.iterrows()}

#print (newdict)


word = input("Enter a word to be converted: ").upper()
outlist = [newdict[letter] for letter in word]
print (outlist)




