def count_words(book_txt):
    word_split = []
    counter = 0
    word_split = book_txt.split()
    for word in word_split:
        counter += 1
    print (f"{counter}" + " words found in the document")