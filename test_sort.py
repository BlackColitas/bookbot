def sort_on(item):
    return item["num"]

def sort_dic(char_count):
    result = []
    for key, value in char_count.items():
        result.append({"char":key, "num":value})
    result.sort(reverse=True, key=sort_on)
    
    return result

my_counts = {"d": 1, "c": 7, "a": 4}
sorted_list = sort_dic(my_counts)
print(sorted_list)