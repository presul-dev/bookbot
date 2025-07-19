def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = 0
    unique_char = {}
    for char in text.lower():
        if char in unique_char:
            unique_char[char] +=1
        else:
            unique_char.update({char: 1})
    return unique_char

def get_sorted_counts(items):
    char_count_list = []
    char_count_dict = {}
    for item in items.items():
        if item[0].isalpha():
            char_count_dict={"char": item[0], "num":item[1]}
            char_count_list.append(char_count_dict)
    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list

def sort_on(items):
    return items["num"]