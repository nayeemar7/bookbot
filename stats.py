def get_num_words(content):
    words = content.split()
    return len(words)

def get_num_characters(content):
    dictionary = {}
    for character in content:
        char = character.lower()
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    return dictionary

def sort_on(sorted_dict):
    return sorted_dict["num"]
    
def sorted_dictionaries(num_characters):
    sorted_list = []
    for char,count in num_characters.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


