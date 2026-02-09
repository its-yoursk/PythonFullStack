def Vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count
input_word = input("Enter a word: ")
vowel_count = Vowels(input_word)

print(f"The number of vowels in '{input_word}' is: {vowel_count}")
