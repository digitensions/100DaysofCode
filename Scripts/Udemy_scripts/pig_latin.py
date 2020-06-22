# get sentence from user
original = input("Please provide a sentence to convert to pig latin: ").strip().lower()
#split sentence into words
words = original.split()
#loop through words and convert to pig latin
new_words = []
for w in words:
    if w[0] in "aeiou":
        new_word = w + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in w:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = w[:vowel_pos]
        the_rest = w[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

out = " ".join(new_words)
print(out)