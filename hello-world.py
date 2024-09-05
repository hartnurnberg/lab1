def main():
    word = input('Enter a string: ')
    new_word = ''

    for char in word:
        if 'a' <= char <= 'z':
            new_word += chr(ord(char)-32)
        else:
            new_word += char

    print('The capitalized word is:', new_word)

    rev_word = ''
    for char in new_word[::-1]:
        rev_word += char

    print('The reversed word is:', rev_word)

main()