import re

def word_count(s):
    # Your code here
    words = {}
    punctuation_to_ignore = '''":;,.-+=/\|[]{}()*^&'''


################### With Python ###################
    # for character in s:
    #     if character in punctuation_to_ignore:
    #         s = s.replace(character, "")

    lowercase_string = s.lower()
    print(lowercase_string)

    
    for character in lowercase_string:
        if character in punctuation_to_ignore:
            lowercase_string = lowercase_string.replace(character, "")

    print(lowercase_string)

    split_string = lowercase_string.split()

    # for word in split_string:
    #     for character in word:
    #         if character in punctuation_to_ignore:
    #             word = word.replace(character, "")


################### With Regex ###################

    # split_string = re.findall(r'\w+', s)




    print(split_string)

    


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))