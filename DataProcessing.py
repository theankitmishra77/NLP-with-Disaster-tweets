import nltk,re
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

def get_tags(text, tag):
    '''
    Extracts the given tag type from the text.
    
    Parameters :
        text (string) : Input Text
        tag (string) : Tag type like , #,@ etc.
    '''
    hash_tags = []
    tokens = text.split()
    for token in tokens:
        #print(token)
        if token.startswith(tag):
            hash_tags.append(token[1:])
    
    return ','.join(hash_tags)


def remove_tags(text, tag):
    '''
    Remove the given tags from the text.
    
    Parameters :
        text (string) : Input Text
        tag (string) : Tag Type like #,@.
    '''
    tokens = text.split()
    for token in tokens:
        if token.startswith(tag):
            text = text.replace(token, token[1:])
    
    return text

def remove_irrelevent_words(text):
    '''
    Remove the irrelevent words like tokens of length less than 2.
    
    Parameters :
        text (string) : Input text
    '''
    tokens = nltk.word_tokenize(text)
    #print(tokens)
    for token in tokens:
        if(len(token)<=2):
            text = text.replace(token, '')
    return text

import string
PUNCT_TO_REMOVE = string.punctuation
def remove_punctuation(text):
    '''
    Removes the punctuations from the text.
    
    Parameters :
        text (string) : Input Text
    '''
    return text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))

def is_string_alnum(s):
    '''
    Check if the input string is alpha-numeric.
    
    Parameters :
        s (string) : String Value
    '''
    letter_flag = False
    number_flag = False
    for i in s:
        if i.isalpha():
            letter_flag = True
        if i.isdigit():
            number_flag = True
    return letter_flag and number_flag

def remove_alphanumeric_string(text):
    '''
    Removes the alpha-numeric token from the text.
    
    Parameters :
        text (string) : Input Text
    '''
    tokens = nltk.word_tokenize(text)
    #print(tokens)
    for token in tokens:
        if re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', token) or str.isdigit(token) or is_string_alnum(token):
            text = text.replace(token, '')
    return text

lemmatizer = WordNetLemmatizer()
wordnet_map = {"N":wordnet.NOUN, "V":wordnet.VERB, "J":wordnet.ADJ, "R":wordnet.ADV}
def lemmatize_words(text):
    '''
    Lemmatize the text with root token words.
    
    Parameters :
        text (string) : Input Text
    '''
    pos_tagged_text = nltk.pos_tag(text.split())
    return " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])          

from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('english'))
def remove_stopwords(text):
    '''
    Removes the stop words from the text.
    
    Parameters :
        text (string) : Input Text
    '''
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

def get_cleaned_text(text):
    '''
    Returns the cleaned text after removing punctuations, irrelevant words.
    
    Parameters :
        text (string) : Input Text
    '''
    text = text.lower()
    text = remove_tags(text, '#')
    text = remove_tags(text, '@')
    text = remove_punctuation(text)
    text = remove_stopwords(text)
    text = remove_irrelevent_words(text)
    text = remove_alphanumeric_string(text)
    text = lemmatize_words(text)
    
    return text

remove_tags('There is an earthquake in Delhi. #Disaster', '#')