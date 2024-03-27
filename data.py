import json
from difflib import get_close_matches

# Step 2: Loading JSON Data into Python Dictionary
def load_dictionary():
    with open("data.json") as file:  # Adjusted file name to "data.json"
        data = json.load(file)
    return data

# Step 3: Function to Return Definition of a Word
def get_definition(word, dictionary):
    word = word.lower()  # Convert to lowercase for case insensitivity
    if word in dictionary:
        return dictionary[word]
    else:
        # Step 5: Handle misspelled words
        suggestions = get_close_matches(word, dictionary.keys())
        if suggestions:
            return f"Word not found. Did you mean '{suggestions[0]}'?"
        else:
            return "Word not found."

# Main function to demonstrate usage
def main():
    dictionary = load_dictionary()

    while True:
        user_input = input("Enter a word to get its definition (q to quit): ").strip()
        if user_input.lower() == 'q':
            break
        definition = get_definition(user_input, dictionary)
        print(definition)

if __name__ == "__main__":
    main()
