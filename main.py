import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (
    index, row) in nato_data_frame.iterrows()}
print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
loop_is_on = True
while loop_is_on:
    user_input = input("Enter your word:")
    try:
        phonetic_code_words = [nato_dict[letter]
                               for letter in user_input.upper()]
    except KeyError:
        print("Sorry, only letters allowed in alphabets please")
    else:
        print(phonetic_code_words)
        loop_is_on = False
