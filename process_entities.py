import pandas as pd
import itertools
import json


def extract_top_20_people(input):
    person_dict = {}

    for line in input:
        if line['Type'] == 'PERSON' and "@" not in line['Text']:
            person = line['Text']
            person_dict[person] = person_dict.get(person, 0) + 1
        
    sorted_person_dict = dict(sorted(person_dict.items(), key = lambda item: item[1], reverse=True))

    return dict(itertools.islice(sorted_person_dict.items(), 20))


def extract_top_20_locations(input):
    location_dict = {}

    for line in input:
        if line['Type'] == 'LOCATION':
            location = line['Text']
            location_dict[location] = location_dict.get(location, 0) + 1
        
    sorted_location_dict = dict(sorted(location_dict.items(), key = lambda item: item[1], reverse=True))

    return dict(itertools.islice(sorted_location_dict.items(), 20))


def extract_top_20_organizations(input):
    organization_dict = {}

    for line in input:
        if line['Type'] == 'ORGANIZATION':
            organization = line['Text']
            organization_dict[organization] = organization_dict.get(organization, 0) + 1

    sorted_organization_dict = dict(sorted(organization_dict.items(), key = lambda item: item[1], reverse=True))

    return dict(itertools.islice(sorted_organization_dict.items(), 20))

def dump_to_json(data, filepath):
    json_dump = json.dumps(data)
    f = open(filepath, "w")
    f.write(json_dump)
    f.close()

def main():
    input_file = pd.read_json('data/entities.json')
    input = input_file['Entities']
    top_20_people = extract_top_20_people(input)
    top_20_locations = extract_top_20_locations(input)
    top_20_organizations = extract_top_20_organizations(input)

    dump_to_json(top_20_people, "data/top_20_people.json")
    dump_to_json(top_20_locations, "data/top_20_locations.json")
    dump_to_json(top_20_organizations, "data/top_20_organizations.json")

    

if __name__ == '__main__':
    main()