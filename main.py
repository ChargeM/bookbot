import stats

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = "/home/chargedmite/workspace/github/bookbot/books/frankenstein.txt"
    book_content = get_book_text(filepath)
    #stats.count_words(book_content)
    book_data = stats.count_characters(book_content)
    stats.sorted_list(book_data)


main()