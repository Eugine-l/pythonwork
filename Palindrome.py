def is_palindrome(word):
    Word = word.lower()
    reversed_word = word[::-1]
    return word == reversed_word

# Example usage:
word = input("Enter a word: ")

if is_palindrome(word):
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
