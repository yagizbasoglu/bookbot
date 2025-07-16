def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def number_words(text):
    words = text.split()
    return (len(words))


def count_characters(text):
    
    words={}

    for character in text:
        character = character.lower()
        
        if character not in words:
            words[character] = 1 
        
        else:
            words[character] += 1 
    
    return words 


