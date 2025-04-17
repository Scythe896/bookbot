def get_book_text(path_to_file):
    # Returns the text of a book
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def words_amount(text):
    # Returns the number of words in a text
    return len(text.split())

def get_chars(text):
    # Returns the amount of each lower case character as a dictionairy
    char_dict = {}
    for char in text.lower():
        if char.isalpha():
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict

def report(char_dict):
    # Returns a sorted list of dictionaries by number
    def sort_on(char_dict):
        return char_dict["count"]
    dict_list = []
    # Create list of dictionaries
    for k in char_dict:
        dict_list.append({"char": k, "count": char_dict[k]})
    # Sort list by number
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
