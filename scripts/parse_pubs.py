import re
from pprint import pprint as pp
import json
from codecs import decode


pattern = r"(?P<authors>.*)\"(?P<paper_name>.*)[\"'], (?P<conf>.*)(?= \[PDF\])"
with open('conf.txt', 'r', encoding='utf-8') as file:
    data = file.read()

matches = re.finditer(pattern, data, re.MULTILINE)
result = []

for match in matches:
    authors = str(match['authors'].strip())
    paper_name = str(match['paper_name'].strip())
    conference = str(match['conf'].strip())
    paper_dict = {'authors': authors, 'paper_name': paper_name, 'conference': conference}
    result.append(paper_dict)


with open('conf.json', 'w') as file:
    json.dump(result, file, indent=4)

# pp(result)

print(len(result))