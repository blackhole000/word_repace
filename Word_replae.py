# Use method : Replace


def replace_word():
    my_str = "I am Hatice and I love AI and data visualization"
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(my_str.replace(word_to_replace, word_replacement))


replace_word()