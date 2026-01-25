import pandas

#Creating a dictionary in this format:{"A": "Alfa", "B": "Bravo"}
nato_data =  pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index,row) in nato_data.iterrows()}

#Creating a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    usr_input = input("Enter a word : ").upper()
    usr_input = usr_input.replace(" ", "")
    try:
        nato_word_list = [nato_dict[letter] for letter in usr_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_word_list)

generate_phonetic()