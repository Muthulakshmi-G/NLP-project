filename="metamorphosis_clean.txt"

file=open(filename,'r')
text=file.read()

file.close()
words=text.split()#spliting words by space
word=[word.lower() for word in words]
print(words[:100]


