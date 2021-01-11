import pandas as pd
import itertools
import json

data = pd.read_json('data/entities.json')
data = data['Entities']

frequency_dict = {}

for row in data:
    entity = row['Text']
    frequency_dict[entity] = frequency_dict.get(entity, 0) + 1
    
print(frequency_dict)

print(dict(sorted(frequency_dict.items(), key = lambda item: item[1])))
