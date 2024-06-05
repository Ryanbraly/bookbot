
def main():
    book_path = "books/frankenstein.txt"
    text = open_file(book_path)
    num_words = count_words(text)
    num_chars = count_chars(text.lower())
    sorted_chars = create_sorted_list(num_chars)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_chars:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def count_words(source):
    return len(source.split())

def count_chars(source):
    output = {}
    relevant_chars = "abcdefghijklmnopqrstuvwxyz"
    for char in source:
        if char in output:
            output[char] += 1
        elif char in relevant_chars:
            output[char] = 1
        else:
            pass

    return output

def sort_on(d):
    return d["num"]

def create_sorted_list(chars_dict):
    sorted_list = []
    for i in chars_dict:
        sorted_list.append({"char": i, "num": chars_dict[i]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def open_file(path):
    with open(path) as f:
        return f.read()
            
main()