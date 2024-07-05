def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin Report of {book_path} ---")
    print(f"Number of words found in document: {num_words}")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']} character was found {item['num']} times.'")

    print()
    print("--- END OF REPORT ---")



def get_num_words(text):
    words = text.split()

    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []

    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list    


def get_chars_dict(text):
    chars = {}

    for char in text:
        lowered = char.lower()

        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars




def get_book_text(path):
    with open(path) as f:

        return f.read()
    

main()

