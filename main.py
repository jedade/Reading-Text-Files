# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    lines = ''
    with open("story.txt") as file:
        lines = file.read()
    return lines


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    result = {}
    for i in text.replace(',', '').replace('.', '').replace('?', '').split():
        result.update({ i : text.count(i)})
    return result