# Developed by pragtheesvaran ab
# reference no 21003592
# To write a program for getting the word count from a file...

num_of_words = 0 
file = open('text.txt')
text = file.read()
words = text.split()
num_of_words = len(words)
print("Number of words = ",num_of_words)    