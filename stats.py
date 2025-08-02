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
    
    print (char_num_dict)

        

    

    