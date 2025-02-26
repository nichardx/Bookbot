file_contents = ""

def get_book_text(filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

def main():
       contents = get_book_text("/home/nichard/projects/Bookbot/books/frankenstein.txt")
       print(contents)
main()