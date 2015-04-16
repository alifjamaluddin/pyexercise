

__author__ = 'Alif'

# Write a class/function to return True if 2 input strings are anagram to each other. string1 is an
# anagram of string2 if string2 can be obtained by rearranging the characters in string1. Example:

string1 = "smart"
string2 = "marts"


def isAnagram(text1,text2):
    a = list(text1).sort()
    b = list(text2).sort()

    if a == b :
        return True
    else:
        return False

print isAnagram(string1,string2)

