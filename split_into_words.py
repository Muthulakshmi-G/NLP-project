filename='metamorphosis_clean.txt'
file=open(filename,'rt')
text=file.read()
file.close()

from nltk.tokenize import word_tokenize
tokens=word_tokenize(text)

print(tokens[:100])
