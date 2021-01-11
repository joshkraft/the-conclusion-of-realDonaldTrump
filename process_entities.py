import pandas as pd
import itertools
import json

entities_file = pd.read_json('data/entities.json')
entities = entities_file['Entities']

entities_dict = {}
types_dict = {}

for line in entities:
    entity = line['Text']
    entity_type = line['Type']
    types_dict[entity_type] = types_dict.get(entity_type, 0) + 1
    entities_dict[entity] = entities_dict.get(entity, 0) + 1
    
sorted_entities_dict = dict(sorted(entities_dict.items(), key = lambda item: item[1], reverse=True))

sorted_types_dict = dict(sorted(types_dict.items(), key = lambda item: item[1], reverse=True))

top_20_entities = dict(itertools.islice(sorted_entities_dict.items(), 20))



#=======================================================

person_dict = {}

for line in entities:
    if line['Type'] == 'PERSON' and "@" not in line['Text']:
        person = line['Text']
        person_dict[person] = person_dict.get(person, 0) + 1
    
print(dict(sorted(person_dict.items(), key = lambda item: item[1], reverse=True)))




organization_dict = {}

for line in entities:
    if line['Type'] == 'ORGANIZATION':
        organization = line['Text']
        organization_dict[organization] = organization_dict.get(organization, 0) + 1
    
#print(dict(sorted(organization_dict.items(), key = lambda item: item[1], reverse=True)))

"""
event_dict = {}

for line in entities:
    if line['Type'] == 'EVENT':
        event = line['Text']
        event_dict[event] = event_dict.get(event, 0) + 1
    
print(dict(sorted(event_dict.items(), key = lambda item: item[1], reverse=True)))

"""


