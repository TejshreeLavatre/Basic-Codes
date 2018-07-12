"""
This program finds anagrams from a pre-existing list of 1934 Webster's dictionary words(stored in a file named "word")
Comprehension is used to reduce the lines of codes.
Can use following lines of code instead of the above comprehension:
openfile = open("word", "r")
read_file = openfile.readlines() #Returns a list of all the lines in the file
clean_file = [entry.strip().lower() for entry in read_file] #strip and lower are string methods
new_list = sorted(list(set(clean_file)))
Line 8 removes duplicate entries by converting list to set since sets can have only one entry of an instance.
Then  converts it back to list again and sorts the list in order.
"""

import collections
new_list = sorted(list(set([entry.lower().strip() for entry in open("word", "r")])))


def join_sorted_word(abc):
    return "".join(sorted(abc))


"""
def anagram(entry):
    return [word for word in new_list if join_sorted_word(word) == join_sorted_word(entry)]
This process takes longer, hence built a dictionary instead.
Here the keys are the sorted entries (join_sorted_word) and the values are its anagrams.
"""

words_by_signature = collections.defaultdict(list)

for i in new_list:
    words_by_signature[join_sorted_word(i)].append(i)


def anagrams_fast(entry):
    return words_by_signature[join_sorted_word(entry)]


all_anagrams = {value: anagrams_fast(value) for value in new_list if len(anagrams_fast(value)) > 1}
#discards trivial entries such as words that are anagrams of themselves

get_anagram = input("Enter the word whose anagrams you want to list: ")
print(anagrams_fast(get_anagram))
