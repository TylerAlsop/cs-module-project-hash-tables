def word_count(s):
    # Your code here
    words = {}
    punctuation_to_ignore = '''":;,.-+=/\|[]{}()*^&'''
    # punctuation_count = 0


################### With Python ###################
    # for character in s:
    #     if character in punctuation_to_ignore:
    #         punctuation_count += 1
    
    # if punctuation_count == 0:
    #     return {}

    # if (punctuation in punctuation_to_ignore) not in s:
    #     return {}

    lowercase_string = s.lower()

    
    for character in lowercase_string:
        if character in punctuation_to_ignore:
            lowercase_string = lowercase_string.replace(character, "")


    split_string = lowercase_string.split()

    for word in split_string:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

    return words



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))