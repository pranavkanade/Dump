# Tutorial link : http://nicschrading.com/project/Intro-to-NLP-with-spaCy/

from spacy.en import English

# from nltk.stem import WordNetLemmatizer
# wordnet_lemmatizer = WordNetLemmatizer()
# arr = ['Playing', 'Watching', 'LOL', 'Learning']

# for m in arr:
#     print(wordnet_lemmatizer.lemmatize(m), " : " , m)
#     print('---------------------------')

parcer = English()

# Test Data
# multiSentence = "Hello!! there I am Pranav and I am gr8ful to this life. I rly don't waana miss any beautiful moments in my life. This is all I have and so it is precious."
multiSentence = "A writing workshop enrolls novelists and poets in a ratio of 5 to 3. There are 24 people at the workshop. How many novelists are there? How many poets are there?"

## ******************* To parse the data
parsedData = parcer(multiSentence)

# Iterate through parsedData
# Each token is an object with lots of different properties
# A property with an underscore at the end returns the string representation of result
# * while a property without the underscore returns an index (int) into spaCy's vocabulary
# The probability estimate is based on counts from a 3 billion word
# corpus, smoothed using the Simple Good-Turing method.

# for i, token in enumerate(parsedData):
#     print("Original : ", token.orth, token.orth_)
#     print("lemma : ", token.lemma, token.lemma_)
#     print("shape : ", token.shape, token.shape_)
#     print("prefix : ", token.prefix, token.prefix_)
#     print("suffix : ", token.suffix, token.suffix_)
#     print("log probability : ", token.prob)
#     print("Brown cluster id : ", token.cluster)
#     print("---------------------------------")




# ## ************Sentence generation
# sents = []
# for span in parsedData.sents:
#     sent = ''.join(parsedData[i].string for i in range(span.start, span.end)).strip()
#     sents.append(sent)

# for sentence in sents:
#     print(sentence)



## ***************Part Of Speech Tagging
# for span in parsedData.sents:
#     sent = [parsedData[i] for i in range(span.start, span.end)]
#     break

# for token in sent:
#     print(token.orth_, token.pos_)
##         ------ OR ---------
# for i, token in enumerate(parsedData):
#     print(token.orth_, token.pos_)



## ***************** Dependencies example
# follows the pattern =>
# original token, dependency tag, head word, left dependencies, right dependencies
for token in parsedData:
    print(token.orth_, token.dep_, token.head.orth_, [t.orth_ for t in token.lefts], [t.orth_ for t in token.rights])



## ***************** Named Entity Recognition
# for token in parsedData:
#     print(token.orth_, token.ent_type_ if token.ent_type_ != "" else "(not an entity)")

# # only entities
# print("\n--------Entities only ------------")
# ents = list(parsedData.ents)
# for entity in ents:
#     print(entity.label, entity.label_, ' '.join(t.orth_ for t in entity))
# print(ents)



## ****************** handling messy data including slang and emoticons
# for token in parsedData:
#     print(token.orth_, token.pos_, token.lemma_)
