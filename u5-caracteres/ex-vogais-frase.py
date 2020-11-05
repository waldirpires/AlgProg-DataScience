a_string = "Abcde"
lowercase = a_string.lower()
# Convert to lowercase

vowel_counts = {}

for vowel in "aeiou":
    count = lowercase.count(vowel)
# Count vowels

    vowel_counts[vowel] = count
# Add to dictionary


print(vowel_counts)


#usando map
print(*map(lowercase.lower().count, "aeiou"))


#usando função
def countvowels(string):
    num_vowels=0
    for char in string:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels



sentence = 'this is a sentence'
# counts = {i:0 for i in 'aeiouAEIOU'}
counts= {}.fromkeys('aeiouAEIOU',0)
for char in sentence:
    if char in counts:
        counts[char] += 1

for k,v in counts.items():
    print(k, v)


data = "Please type a sentence: "
vowels = "aeiou"
for v in vowels:
    print(v, data.lower().count(v))


print('==============')
string = "aswdrtio"
res = [string.lower().count(x) for x in "aeiou"]
print(res)