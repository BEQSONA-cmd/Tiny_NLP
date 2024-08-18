import re
from stopwords import CUSTOM_STOPWORDS, expand_contractions, CATEGORY_SYNONYMS

def map_to_category(tokens):
    tokens = ' '.join(tokens)
    
    for category, synonyms in CATEGORY_SYNONYMS.items():
        for synonym in synonyms:
            if synonym in tokens:
                return [category]
    return tokens



def tokenize(text, remove_stopwords=True):
    text = expand_contractions(text.lower())
    text = re.sub(r'[^\w\s]', '', text)
    tokens = re.findall(r'\b\w+\b', text)

    # if remove_stopwords:
    #     tokens = [token for token in tokens if token not in CUSTOM_STOPWORDS or token in CATEGORY_SYNONYMS]

    print(f"Tokens after stopword removal: {tokens}")

    tokens = map_to_category(tokens)
    
    return tokens

# text = "I'm testing the tokenizer and It's working well!"
# tokens = tokenize(text)
# print(tokens)