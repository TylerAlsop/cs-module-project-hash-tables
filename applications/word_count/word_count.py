import re

def word_count(s):
    # Your code here
    words = {}
    punctuation_to_ignore = '''":;,.-+=/\|[]{}()*^&'''


################### With Python ###################

    lowercase_string = s.lower()

    
    for character in lowercase_string:
        if character in punctuation_to_ignore:
            lowercase_string = lowercase_string.replace(character, "")


    split_string = lowercase_string.split()



################### With Regex ###################

    # split_string = re.findall(r'\w+', s)

##################################################



    print(split_string)

    


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))