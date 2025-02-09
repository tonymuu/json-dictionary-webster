import re
import json

data = ''

with open('dict.txt') as f:
    data = f.read()

lines = data.split('\n\n\n')

dict_str = lines[2] + '\n' + lines[3]

pattern = r'\n\n[A-Z]+\n'

words = re.findall(pattern, dict_str)
defs = re.split(pattern, dict_str)
defs = defs[1:]


# for each defs, split by \n\n
# items[0] is metadata about word i.e. etymology
# if line match ^[0-9]. , merge with next line

dict_out = {}

for w, d in zip(words, defs):
    w = w.strip()

    items = d.split('\n\n')

    metadata = items[0]
    word_defs = []

    n = len(items)
    for i in range(1, n):
        if re.match(r'^[0-9]. ', items[i]) and i < n - 1 and not re.match(r'^[0-9]. ', items[i + 1]):
            word_defs.append(items[i] + items[i + 1])
            i += 1
        else:
            word_defs.append(items[i])

    dict_out[w] = {
        'meta': metadata,
        'definitions': word_defs
    }

json_out = json.dumps(dict_out)

with open('dict.json', 'w') as f:
    f.write(json_out)


