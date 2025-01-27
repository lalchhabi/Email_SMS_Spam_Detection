import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def text_preprocessing(text:str)->str:
    """
    Proprocessing the text for NLP model
    Args:
        text: Input raw text
    Outputs:
        text: Preprocessed text
    """
    text = text.lower() #### Lowercase the text
    text = nltk.word_tokenize(text) #### Tokenize the text
    converted  = []
    for i in text:
        if i.isalpha():
            converted.append(i) ##### Remove special characters
            
    ### Now remove the stopwords and punctuations
    new_text = converted[:] ### clone or copy the list
    converted.clear()
    
    for i in new_text:
        if i not in stopwords.words("english") and i not in string.punctuation:
            converted.append(i)

    latest_text = converted[:]
    converted.clear()
    for i in latest_text:
        converted.append(ps.stem(i)) #### stemming
        
    return " ".join(converted)