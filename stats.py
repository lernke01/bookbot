def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_counts= {}
    for i in text:
        lower = i.lower()
        if lower in char_counts:
            char_counts[lower] += 1
        else:
            char_counts[lower] = 1
    return char_counts

def sorted_characters(char_counts):
    char_list = []  
    for char, count in char_counts.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)
    def sort_on(d):
        return d["num"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    
