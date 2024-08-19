import re


def expand_contractions(text):
    CONTRACTIONS = {
        "don't": "do not",
        "won't": "will not",
        "i'm": "i am",
        "can't": "cannot",
        "it's": "it is",
        "he's": "he is",
        "she's": "she is",
        "that's": "that is",
        "what's": "what is",
        "let's": "let us",
        "you're": "you are",
        "we're": "we are",
        "they're": "they are",
        "i've": "i have",
        "you've": "you have",
        "we've": "we have",
        "they've": "they have",
        "i'd": "i would",
        "you'd": "you would",
        "he'd": "he would",
        "she'd": "she would",
        "we'd": "we would",
        "they'd": "they would",
        "isn't": "is not",
        "aren't": "are not",
        "wasn't": "was not",
        "weren't": "were not",
        "hasn't": "has not",
        "haven't": "have not",
        "hadn't": "had not",
        "doesn't": "does not",
        "didn't": "did not",
        "shouldn't": "should not",
        "wouldn't": "would not",
        "couldn't": "could not",
        "mustn't": "must not"
    }

    for contraction, expansion in CONTRACTIONS.items():
        text = text.replace(contraction, expansion)
    return text