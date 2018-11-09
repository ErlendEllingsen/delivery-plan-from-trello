import csv
import json

# Get inputs 
source = input("Input file name (JSON) (source.json): ")
target = input("Output file name (CSV) (target.csv): ")

field_done = input("Include done field (y): ")
field_person = input("Include person field (y): ")
field_date = input("Include date field (y): ")

# Set default values 
if source is None or source is '':
  source = 'source.json'

if target is None or target is '':
  target = 'target.csv'

if field_done is None or field_done is '':
  field_done = 'y'

if field_person is None or field_person is '':
  field_person = 'y'

if field_date is None or field_date is '':
  field_date = 'y'

# Read file and start parsing

f = open(source, 'r').read()

board = json.loads(f)

# Map lists 
lists = board['lists']
lists_id_name = {}
for k, v in enumerate(lists):
  lists_id_name[v['id']] = v['name']

# Map cards 
cards = board['cards']
cards_done = []
for k, v in enumerate(cards):
  new_object = {
    'id': v['id'],
    'name': v['name'],
    'category': lists_id_name[v['idList']],
    'desc': v['desc'],
    'url': v['url']
  }

  if field_done.lower() != 'n':
    new_object['done'] = False

  if field_person.lower() != 'n':
    new_object['person'] = False

  if field_date.lower() != 'n':
    new_object['date'] = False
  
  cards_done.append(new_object)

# Convert to csv
keys = cards_done[0].keys()
with open(target, 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(cards_done)