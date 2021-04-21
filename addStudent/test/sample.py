from collections import Counter

string = "abcabc"

list_a=string.split(" ")

for i in range(0, len(list_a)):
    string[i]="".join(string[i])

    dict=Counter(string)

    " ".join(dict.keys())