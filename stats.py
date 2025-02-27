

file_contents = ""

def get_book_text(filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

def main():
       contents = get_book_text("/home/nichard/projects/Bookbot/books/frankenstein.txt")
       split_words = contents.split()
       total_words = len(split_words)
       print(f"{total_words} words found in the document")

def get_num_words():
       contents = get_book_text("/home/nichard/projects/Bookbot/books/frankenstein.txt")
       split_words = contents.split()
       total_words = len(split_words)
       print(f"{total_words} words found in the document")

main()