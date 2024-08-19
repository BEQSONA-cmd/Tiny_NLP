import re
from stopwords import expand_contractions, CUSTOM_STOPWORDS, categorize_tokens

def porter_stemmer(word):
    if word.endswith('ed') or word.endswith('ing'):
        word = re.sub(r'(ed|ing)$', '', word)

    if word.endswith('y'):
        word = re.sub(r'y$', 'i', word)

    if word.endswith('s') and not word.endswith('ss'):
        word = re.sub(r's$', '', word)

    if word.endswith('er'):
        word = re.sub(r'er$', '', word)
    elif word.endswith('ly'):
        word = re.sub(r'ly$', '', word)

    if word.endswith('ness'):
        word = re.sub(r'ness$', '', word)
    elif word.endswith('ful'):
        word = re.sub(r'ful$', '', word)
    elif word.endswith('ment'):
        word = re.sub(r'ment$', '', word)
    elif word.endswith('ive'):
        word = re.sub(r'ive$', '', word)
    return word

    for category, keywords in category_keywords.items():
        for token in tokens:
            if token in keywords:
                return category

    return 'unknown'

def tokenize(text, remove_stopwords=True):
    text = expand_contractions(text.lower())
    text = re.sub(r'[^\w\s]', '', text)
    tokens = re.findall(r'\b\w+\b', text)
    
    if remove_stopwords:
        tokens = [word for word in tokens if word not in CUSTOM_STOPWORDS]
    
    tokens = [porter_stemmer(token) for token in tokens]

    category = categorize_tokens(tokens)
    
    return category
