import re
from stopwords import expand_contractions

CUSTOM_STOPWORDS = {
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves',
    'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their',
    'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
    'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an',
    'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
    'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 
    'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when',
    'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor',
    'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should',
    'now'
}

CATEGORY_SYNONYMS = {
    'greeting': ['hello', 'hi', 'greetings', 'hey', 'good morning', 'good evening'],
    'status': ['how are you', 'how do you do', 'what’s up', 'what is your status', 'how are you doing'],
    'goodbye': ['bye', 'goodbye', 'see you', 'farewell', 'ciao'],
    'introduction': ['who are you', 'introduce yourself', 'tell me about yourself', 'what is your name'],
    'capability': ['what can you do', 'what are your capabilities', 'what are you capable of', 'tell me what you can do'],
    'thanks': ['thank you', 'thanks', 'much appreciated', 'thankful', 'grateful'],
    'ai': ['artificial intelligence', 'ai', 'robot', 'machine learning'],
    'weather': ['what is the weather', 'weather', 'forecast', 'is it raining', 'temperature'],
    'joke': ['tell me a joke', 'joke', 'make me laugh', 'something funny'],
    'recommendation': ['recommend', 'suggest', 'what should I do', 'what do you recommend'],
    'apology': ['sorry', 'apologize', 'my apologies', 'forgive me'],
    'affirmation': ['yes', 'correct', 'absolutely', 'sure', 'definitely'],
    'negation': ['no', 'not at all', 'no way', 'negative'],
    'time': ['what time is it', 'time', 'current time', 'tell me the time'],
    'location': ['where am I', 'location', 'current location', 'where is it'],
    'humor': ['tell me something funny', 'humor', 'joke', 'make me laugh'],
    'news': ['what is the news', 'news', 'headlines', 'breaking news'],
    'motivation': ['motivate me', 'inspire me', 'motivation', 'encouragement'],
    'personal_opinion': ['what do you think', 'your opinion', 'do you agree', 'your thoughts'],
    'correction': ['correction', 'fix', 'amend', 'rectify']
}

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

    tokens = map_to_category(tokens)
    
    return tokens

# text = "I'm testing the tokenizer and It's working well!"
# tokens = tokenize(text)
# print(tokens)