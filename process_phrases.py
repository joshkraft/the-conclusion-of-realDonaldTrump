import pandas as pd
import itertools
import json

phrase_file = pd.read_json('data/raw_phrase_extraction')

phrases = phrase_file['KeyPhrases']

phrase_dict = {}

for line in phrases:
    phrase = line['Text'].lower()
    phrase_dict[phrase] = phrase_dict.get(phrase, 0) + 1

sorted_phrase_dict = dict(sorted(phrase_dict.items(), key = lambda item: item[1], reverse=True))

top_20_phrases = dict(itertools.islice(sorted_phrase_dict.items(), 20))

json = json.dumps(top_20_phrases)
f = open("data/top_20_phrases.json","w")
f.write(json)
f.close()