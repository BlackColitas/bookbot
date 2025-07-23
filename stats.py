def text_split(book):
    book_words = book.split()
    num_words = len(book_words)
    return num_words

def character_count(book):
    char_count = {}
    for c in book.lower():
        if c not in char_count:
            char_count[c] = 1 
        elif c in char_count:
            char_count[c] += 1
    # If wishing to sort them aplphabetically.        
    # sort_char = dict(sorted(char_count.items()))         
    return char_count


def sort_on(item):
    return item["num"]

def sort_dic(char_count):
    result = []
    for key, value in char_count.items():
        result.append({"char":key, "num":value})
    result.sort(reverse=True, key=sort_on)
    
    return result

        





