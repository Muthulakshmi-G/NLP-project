filename='metamorphosis_clean.txt'
file=open(filename,'rt')
text=file.read()
file.close()

#split into words

from nltk import sent_tokenize
import tokenize
sentences=sent_tokenize(text)
print(sentences[0])




