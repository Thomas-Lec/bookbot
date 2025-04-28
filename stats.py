def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_char(text):
    dict_char = {}
    text = text.lower()
    for character in text:
        if character in dict_char:
            dict_char[character] += 1
        else:
            dict_char[character] = 1
    return dict_char

def sort_dict(dictionary):
    new_dict = {}
    result_list = []

    for i in dictionary.keys():
        if i.isalpha():
            new_dict = {"char": i, "num": dictionary[i]}
            result_list.append(new_dict)

    result_list.sort(reverse=True, key=lambda dict: dict["num"])


    return result_list

