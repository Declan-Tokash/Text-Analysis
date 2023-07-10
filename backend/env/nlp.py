import nltk
from pprint import pprint
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import ne_chunk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from googletrans import Translator

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer



sia = SentimentIntensityAnalyzer()


nltk.download([
     "names",
     "stopwords",
     "state_union",
     "twitter_samples",
     "movie_reviews",
     "averaged_perceptron_tagger",
     "vader_lexicon",
     "punkt",
     "words",
     "maxent_ne_chunker"
])

text = """

        World War II, also known as the Second World War, was a global conflict that took place from 1939 to 1945. It involved many 
        nations across different continents, with two major opposing alliances: the Allies and the Axis powers. The war was sparked by 
        the aggressive expansionist policies of Nazi Germany under Adolf Hitler, who sought to dominate Europe. The conflict encompassed 
        significant military campaigns, marked by major battles and strategic maneuvers. It witnessed the use of new technologies and 
        weapons, including aircraft, tanks, and atomic bombs. The war had profound and far-reaching consequences, leading to the loss of 
        millions of lives, widespread destruction, and significant geopolitical shifts. Ultimately, the Allies emerged victorious, but the 
        war left a lasting impact on the world, shaping the post-war era and paving the way for subsequent global developments.

    """

def sentiment_analysis(text):
    res = ""
    x = sia.polarity_scores(text)
    y = sia.polarity_scores(text)["compound"] > 0
    res = "Your text has an overall compound score of " + str(x['compound'])
    return res


def entity_recognition(text):
    sentences = sent_tokenize(text)
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [pos_tag(tokens) for tokens in tokenized_sentences]
    ner_results = [ne_chunk(tagged) for tagged in tagged_sentences]
    return ner_results


def translate(text):
    translator = Translator()
    translation = translator.translate(text, dest='en')
    return translation.text


def frequncy_table(text):
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)
    ps = PorterStemmer()

    freqTable = dict()
    for word in words:
        word = ps.stem(word)
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
            
    return freqTable


def score_sentences(sentences, freqTable):
    sentenceValue = dict()

    for sentence in sentences:
        word_count_in_sentence = (len(word_tokenize(sentence)))
        for wordValue in freqTable:
            if wordValue in sentence.lower():
                if sentence[:10] in sentenceValue:
                    sentenceValue[sentence[:10]] += freqTable[wordValue]
                else:
                    sentenceValue[sentence[:10]] = freqTable[wordValue]
    return sentenceValue

def find_average_score(sentenceValue):
    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]
    average = int(sumValues / len(sentenceValue))
    return average

def generate_summary(sentences, sentenceValue, threshold):
    sentence_count = 0
    summary = ''

    for sentence in sentences:
        if sentence[:10] in sentenceValue and sentenceValue[sentence[:10]] > (threshold):
            summary += " " + sentence
            sentence_count += 1
    return summary



def summary_build(text):
    freq_table = frequncy_table(text)

    sentences = sent_tokenize(text)

    sentence_scores = score_sentences(sentences, freq_table)

    threshold = find_average_score(sentence_scores)


    summary = generate_summary(sentences, sentence_scores, 1.5 * threshold)

    return summary







