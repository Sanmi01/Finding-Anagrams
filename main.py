# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if type(word) != str or type(anagram) != str:
        return "Not a string"
    else:
        return (sorted(word.replace(" ", "").lower())==sorted(anagram.replace(" ", "").lower()))

print(find_anagram("h e y br o t h e r", "hey bother r")) # --> True
print(find_anagram("mite", "tiMe")) # --> True
print(find_anagram("cheap", "peach")) # --> True
print(find_anagram("Hello", "Dinner")) # --> False
print(find_anagram(12, 21)) # --> Not a string
print(find_anagram(['a', 'b'], ['a','b'])) # --> Not a string

