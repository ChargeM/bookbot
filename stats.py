def count_words(book_txt):
    word_split = []
    counter = 0
    word_split = book_txt.split()
    for word in word_split:
        counter += 1
    print (f"{counter}" + " words found in the document")

def count_characters(book_txt):
    lower_book_txt = book_txt.lower()
    char_num_dict = {}
    char_list = []
    counter = 0
    for char in lower_book_txt:
        char_list.append(char)

    for item in char_list:
        if (item in char_num_dict):
            char_num_dict[item] += 1
        else:
            char_num_dict[item] = 1
    
    return char_num_dict

def sorted_list(char_dict):
    sorted_char = {k: v for k, v in sorted(char_dict.items(), key = lambda item: item[1])}
    reversed_sorted_char = dict(reversed(sorted_char.items()))
    sorted_char_list = []
    for item in reversed_sorted_char:
        sorted_char_list.append({item : reversed_sorted_char[item]})