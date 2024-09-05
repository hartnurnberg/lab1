def main():
    word = input('Enter a string: ') #User enters initial word
    new_word = ''

    for char in word: #Capitalize word, store in new string
        if 'a' <= char <= 'z':
            new_word += chr(ord(char)-32)
        else:
            new_word += char

    print('The capitalized word is:', new_word)

    rev_word = ''
    for char in new_word[::-1]: #Reverse word, store in new string
        rev_word += char

    print('The reversed word is:', rev_word)

main()