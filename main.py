def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #word_counter(file_contents)
    result = letter_counter(file_contents)
    print(result)

#commented out since not needed for task!
def word_counter(whole_string):
    count = 0
    words = whole_string.split()
    for i in range(0,len(words)):
        count += 1
    print(count)

def letter_counter(whole_string):
    letters = {}
    lowered = whole_string.lower()
    for letter in lowered:
        if letter in letters:
            letters[letter] = letters[letter] + 1
        else:
            letters[letter]= 1
    return letters

main()
