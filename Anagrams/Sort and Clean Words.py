file = open("word", "r")
wordlist = file.readlines()
# new_words = sorted(list(set([entry.strip().lower() for entry in open("word", "r")])))
# print(new_words)
print(wordlist)
wordclean = [entry.strip().lower() for entry in wordlist]
print(wordclean)
# print(sorted("lives"))
# unique_word = list(set(clean_words))
# unique_word.sort()
# print(unique_word)

#
# def alphabetical_order(words):
#     return "".join(sorted(words))
#
#
# print(alphabetical_order("baced"))

