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



def sort_on(items):
    return items["num"]


def sorting(characters):
    char_dicts_list=[]
    
    for char, count in characters.items():
        if char.isalpha():
            new_item_dict = {"char": char, "num": count}
            char_dicts_list.append(new_item_dict) 
        
        else:
            pass
        
    char_dicts_list.sort(reverse=True, key=sort_on)

    return char_dicts_list



