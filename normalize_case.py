filename='metamorphosis_clean.txt'
file=open(filename,'rt')
text=file.read()
file.close()
words=text.split()

words=[word.lower() for word in words]
print(words[:100])
