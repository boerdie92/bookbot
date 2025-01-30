filename = "books/frankenstein.txt"

def main():
    with open(filename) as f:
        file_contents = f.read()
    words_counted = word_counter(file_contents)
    letters_returned = letter_counter(file_contents)
    sorted_chars = count_sorter(letters_returned)
    print_results(words_counted, sorted_chars)

def word_counter(whole_string):
    return len(whole_string.split())

def letter_counter(whole_string):
    letters = {}
    lowered = whole_string.lower()
    for letter in lowered:
        if letter in letters:
            letters[letter] = letters[letter] + 1
        else:
            letters[letter]= 1
    return letters

def count_sorter(counted_chars):
    alphabet = []
    for entry in counted_chars:
        if entry.isalpha() == True:
            whole = {}
            whole["chars"] = entry
            whole["count"] = counted_chars[entry]
            alphabet.append(whole)
    alphabet.sort(reverse=True, key=lambda x: x["count"])
    return alphabet

def print_results(n_words, chars_):
    print(f"--- Begin report of {filename} ---")
    print(f"{n_words} words found in the document")
    print("")
    for entry in chars_:
        print(f"The '{entry["chars"]}' character was found {entry["count"]} times")
    print("--- End report ---")

main()
