def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_counter(file_contents)

def word_counter(whole_string):
    count = 0
    words = whole_string.split()
    for i in range(0,len(words)):
        count += 1
    print(count)

main()
