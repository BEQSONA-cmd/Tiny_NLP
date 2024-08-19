import re

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

patterns = {
    'greeting': [
        'hello', 'hi', 'hey', 'greetings', 'hiya', 'howdy', 'sup', 'good morning', 'good afternoon', 
        'good evening', 'yo', 'what’s up', 'whats up', 'how’s it going', 'how are you'
    ],
    'status': [
        'how are you', 'how do you do', 'what’s up', 'how’s it going', 'how are things', 'how have you been',
        'are you okay', 'how do you feel', 'what’s your status', 'how are you doing', 'are you doing well'
    ],
    'goodbye': [
        'bye', 'goodbye', 'see you', 'farewell', 'ciao', 'later', 'see ya', 'take care', 'catch you later',
        'adios', 'au revoir', 'bye bye', 'see you later', 'good night', 'peace out', 'talk to you later'
    ],
    'introduction': [
        'who are you', 'introduce yourself', 'tell me about yourself', 'what is your name', 'who am i talking to',
        'what are you', 'who is this', 'what’s your name', 'what do i call you', 'who is this', 'who’s speaking'
    ],
    'capability': [
        'what can you do', 'what are your capabilities', 'what are you capable of', 'tell me what you can do',
        'how can you help me', 'what skills do you have', 'what’s your functionality', 'what’s your purpose',
        'what are your functions'
    ],
    'thanks': [
        'thank you', 'thanks', 'much appreciated', 'thankful', 'grateful', 'thanks a lot', 'thanks so much', 
        'cheers', 'thanks a million', 'thanks a ton', 'thank you very much', 'thanks a bunch', 'many thanks'
    ],
    'ai': [
        'artificial intelligence', 'ai', 'robot', 'machine learning', 'are you an ai', 'are you a robot', 
        'are you an artificial intelligence', 'are you human', 'what is ai', 'what is artificial intelligence'
    ],
    'weather': [
        'what is the weather', 'weather', 'forecast', 'is it raining', 'temperature', 'how’s the weather', 
        'what’s the weather like', 'is it sunny', 'what’s the forecast', 'current weather', 'weather outside'
    ],
    'joke': [
        'tell me a joke', 'joke', 'make me laugh', 'something funny', 'crack a joke', 'funny stuff', 'humor me',
        'give me a joke', 'tell a joke', 'make me giggle', 'funny', 'tell me something funny'
    ],
    'recommendation': [
        'recommend', 'suggest', 'what should I do', 'what do you recommend', 'give me advice', 'any suggestions',
        'should i', 'what do you think i should do', 'can you suggest', 'what’s your recommendation', 
        'what’s your suggestion', 'advice please'
    ],
    'apology': [
        'sorry', 'apologize', 'my apologies', 'forgive me', 'pardon me', 'excuse me', 'i apologize', 
        'i’m sorry', 'oops', 'my bad', 'please forgive', 'i regret', 'my mistake', 'i didn’t mean to'
    ],
    'affirmation': [
        'yes', 'yeah', 'yep', 'absolutely', 'definitely', 'sure', 'of course', 'certainly', 
        'correct', 'you bet', 'indeed', 'right', 'affirmative', 'totally', 'i agree', 'exactly', 'that’s right'
    ],
    'negation': [
        'no', 'nope', 'nah', 'not at all', 'no way', 'negative', 'absolutely not', 'i don’t think so', 
        'no chance', 'i disagree', 'never', 'not really', 'no thank you', 'not interested'
    ],
    'time': [
        'what time is it', 'time', 'current time', 'tell me the time', 'what’s the time', 'do you have the time', 
        'can you tell me the time', 'time check', 'clock', 'current time please', 'what’s the clock say'
    ],
    'location': [
        'where am I', 'location', 'current location', 'where is it', 'where is this', 'my location', 
        'where are we', 'where is this place', 'where am I located', 'can you find my location', 
        'where are you', 'where are you located'
    ],
    'humor': [
        'tell me something funny', 'humor', 'joke', 'make me laugh', 'funny stuff', 'something amusing', 
        'make me smile', 'make me giggle', 'give me some humor', 'crack a joke', 'funny', 'entertain me'
    ],
    'news': [
        'what is the news', 'news', 'headlines', 'breaking news', 'latest news', 'what’s happening', 
        'what’s in the news', 'any news', 'current events', 'what’s going on', 'today’s news', 'news update'
    ],
    'motivation': [
        'motivate me', 'inspire me', 'motivation', 'encouragement', 'give me motivation', 'i need inspiration', 
        'encourage me', 'help me stay motivated', 'give me some motivation', 'inspire me to', 
        'how can i stay motivated', 'what motivates you'
    ],
    'personal_opinion': [
        'what do you think', 'your opinion', 'do you agree', 'your thoughts', 'what’s your take', 
        'how do you feel about it', 'do you think so', 'what’s your view', 'what do you believe', 
        'what do you feel about', 'what do you say'
    ],
    'correction': [
        'correction', 'fix', 'amend', 'rectify', 'correct this', 'correct me', 'please fix this', 
        'i need a correction', 'can you correct', 'how to fix', 'can you amend this', 'rectification', 
        'adjust', 'can you fix it'
    ]
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

def categorize_tokens(tokens):
    category_keywords = {
        'greeting': ['hello', 'hi', 'greet', 'hey', 'morning', 'evening'],
        'goodbye': ['bye', 'farewell', 'ciao', 'see'],
        'status': ['how', 'status', 'doing', 'up'],
        'introduction': ['who', 'introduce', 'name'],
        'capability': ['can', 'do', 'capable', 'ability'],
        'thanks': ['thank', 'appreciate', 'grateful'],
        'ai': ['ai', 'robot', 'machine', 'intelligence'],
        'weather': ['weather', 'forecast', 'rain', 'temperature'],
        'joke': ['joke', 'laugh', 'funny'],
        'recommendation': ['recommend', 'suggest'],
        'apology': ['sorry', 'apologize', 'forgive'],
        'affirmation': ['yes', 'correct', 'sure', 'definitely'],
        'negation': ['no', 'not', 'negative'],
        'time': ['time', 'clock'],
        'location': ['where', 'location'],
        'humor': ['humor', 'joke'],
        'news': ['news', 'headline'],
        'motivation': ['motivate', 'inspire'],
        'personal_opinion': ['think', 'opinion', 'thoughts'],
        'correction': ['correct', 'fix', 'amend'],
    }

    for contraction, expansion in CONTRACTIONS.items():
        text = text.replace(contraction, expansion)
    return text