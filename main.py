def main():
    book_path = "books/frankenstein.txt"
    text = get_books_text(book_path)
    word_count = count_words(text)
    char_dict = count_chars(text)
    print(f"--- Report of book: {book_path} ---\n")
    print(f"Book consists of {word_count} words\n")
    sort_char_dict = sorted(char_dict.items(), key=lambda x:x[1], reverse=True)
    for char_times in sort_char_dict:
        if char_times[0] >= "a" and char_times[0] <= "z":
            print(f"The Character {char_times[0]} has appeared in the text {char_times[1]} times")
    
    
def get_books_text(path):
    with open(path) as fp:
        return fp.read()
    
def count_words(text):
    text = text.split()
    word_count = len(text)
    return word_count

def count_chars(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def sort_on(dict):
    return dict["num"]

main()