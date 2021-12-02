def countVowels(word):
    print("given word :", word)
    word = word.lower()
    return {v:word.count(v) for v in 'aeiou'}
    
word = input("Enter the word")
print(countVowels(word))