import numpy as np      #pip install numpy
import nltk     #pip install nltk
from nltk.stem.porter import PorterStemmer

Stemmer = PorterStemmer()

#Cubic Order = "hello", "hellos"

def tokenize(sentence):
    return nltk.word_tokenize(sentence)
#hello Cubic = ['hello', 'Cubic']

def stem(word):
    return Stemmer.stem(word.lower())
#hello Cubic = ['hello', 'Cubic']

def bag_of_words(tokenized_sentence, words):
    sentence_word = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
#hello Cubic = ['h e l l o', 'c u b i c']

    
    for idx, w in enumerate(words):
        if w in sentence_word:
            bag[idx] =1
            
    return bag

