def get_num_words(path):
    with open(path) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
    print (f"Found {num_words} total words")

def get_count(path):
    with open(path) as f:
        file_contents = f.read()
        count = {}
        for letter in file_contents:
            letter = letter.lower()
            if letter.isalpha():
                if letter not in count:
                    count[letter] = 1
                else:
                    count[letter] += 1
    return count

def sort_on(items):
    return items["num"]

def get_sorted_count(path):
    count = get_count(path)
    count_list = [{"char":char, "num":num} for char, num in count.items()]
    count_list.sort(reverse=True, key=sort_on)
    return count_list
    
        
        
    

    