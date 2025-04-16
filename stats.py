import string

lowercase_alphabet = string.ascii_lowercase + 'æ' + 'â'+'ê'+'ë'+'ô'

def num_words(s):
    return len(s.split())

'''
Add a new function to your stats.py file that takes the text from the book as a string, 
and returns the number of times each character, (including symbols and spaces), appears in the string.
Convert any character to lowercase using the .lower() method, we don't want duplicates.
Use a dictionary of String -> Integer. The returned dictionary should look something like this:
{'p': 6121, 'r': 20818, 'o': 25225, ...
'''

def num_word_usage(s):
    dict_usage = {}
    specials = {}
    text_lower = s.lower()
    for l in lowercase_alphabet:
        dict_usage[l] = 0
    for s in text_lower:
        try:
            if s in specials:
                specials[s] +=1
            else:
                dict_usage[s] +=1
        except KeyError as e:
            specials[s] = 1
    # print(specials)
    return dict_usage