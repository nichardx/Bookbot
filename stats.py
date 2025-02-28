

file_contents = ""

def get_book_text(filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

def main():
       contents = get_book_text(filepath)
       split_words = contents.split()
       total_words = len(split_words)
       print(f"{total_words} words found in the document")

def get_num_words(file_contents):
       contents = file_contents
       split_words = contents.split()
       total_words = len(split_words)
       return total_words

def number_characters(text):
    the_letters = {}
    lowered = text.lower()
    for letters in lowered:
        if letters in the_letters:
            the_letters[letters] +=1
        else:
            the_letters[letters] = 1
    return the_letters

def char_report(text):
    alpha = {}
    the_letters = {}
    lowered = text.lower()
    for letters in lowered:
        if letters in the_letters:
            the_letters[letters] +=1
        else:
            the_letters[letters] = 1      
    for key, value in the_letters.items():
        if key.isalpha() == True:
            alpha[key] = value
        else:
            pass
    def sort_on(dict):
        return dict["count"]
    
    char_list = []
    for char, count in alpha.items():
        char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=sort_on)

    return char_list