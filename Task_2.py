#Reversing words in the string
def reverse_words_in_string(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
        
print(reverse_words_in_string('The Tests Given in the Instructions'))
print(reverse_words_in_string('Hello World'))
print(reverse_words_in_string('Hi There.'))
