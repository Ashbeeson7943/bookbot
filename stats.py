def get_word_count(book_text):
    words = book_text.split()
    return len(words)


def get_character_count(book_text):
    sanitised_book_text = book_text.lower()
    sanitised_book_text = sanitised_book_text.split()
    character_dictionary = {}
    for word in sanitised_book_text:
        char_list = word[::1]   
        for char in char_list:
            if char.isalpha():
                if char in character_dictionary:
                    character_dictionary[char] += 1
                else:
                    character_dictionary[char] = 1
    return character_dictionary


def sort_character_count(character_count):
    new_chars = []
    for val in character_count:
        new_dict = {"char":"", "num": 0}
        new_dict["char"] = val
        new_dict["num"] = character_count[val]
        new_chars.append(new_dict)
    new_chars.sort(reverse=True, key=sort_on)
    return new_chars


def sort_on(items):
    return items["num"]