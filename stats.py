import sys

def get_num_words():
    with open(sys.argv[1]) as f:
        book = f.read()
        words = book.split()
        i = 0
        number_words = 0
        for word in words:
            i += 1
        number_words = i
        return number_words

def count_characters():
    list1 = []
    dictionary = {}
    with open(sys.argv[1]) as f:
        books = f.read()
        paragraph = books.lower()
        for letter in paragraph:
            if letter not in list1:
                list1.append(letter)
        #print(list1)
        for i in range(len(list1)):
            dictionary[list1[i]] = 0 #*
        #print(dict)
        for letter in paragraph:
            for item in dictionary:
                if letter == item:
                    dictionary[item] += 1
        return dictionary

def sort_on(dict):
    return dict["num"]

def sorting_dictionary():
    dict = count_characters()
    list1 = []
    list2 = []
    d = {}

    for item in dict:
        number = dict[item]
        list1.append({"char" : item, "num" : number})

    list1.sort(reverse=True, key=sort_on)

    for i in range(0,len(list1)):
        if list1[i]["char"].isalpha():
            list2.append(list1[i]["char"])

    for i in list2:
        if i in dict:
            d[i] = dict[i]
    return d


