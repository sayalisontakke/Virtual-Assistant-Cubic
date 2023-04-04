import numpy as np      #pip install numpy
import nltk     #pip install nltk
from nltk.stem.porter import PorterStemmer

Stemmer = PorterStemmer()

#Ana Order = "hello", "hellos"

def tokenize(sentence):
    return nltk.word_tokenize(sentence)
#hello Ana = ['hello', 'Ana']

def stem(word):
    return Stemmer.stem(word.lower())
#hello Ana = ['hello', 'ana']

def bag_of_words(tokenized_sentence, words):
    sentence_word = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
#hello Ana = ['h e l l o', 'a n a']

    
    for idx, w in enumerate(words):
        if w in sentence_word:
            bag[idx] =1
            
    return bag

