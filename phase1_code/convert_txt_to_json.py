import json
import io
js_corpus = open('./../training_data/js_corpus.txt', 'r')

js_corpus = js_corpus.readlines()

index = 1

js_list = []

for line in js_corpus:
    js_list.append({"iIndex": index, "sQuestion": line, "iClass": 0})
    index += 1

with io.open('./../training_data/js_corpus.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(js_list, indent=4, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    outfile.write(str_)
# with open('./../training_data/compare_corpus.txt') as compare_corpus:
#    compare_corpus = compare_corpus.read()

