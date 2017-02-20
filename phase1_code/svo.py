from spacy.en import English
from nltk.stem.wordnet import WordNetLemmatizer

SUBJ = ["nsubj", "nsubjpass", "csubj", "csubjpass", "agent", "expl"]
OBJ = ["dobj", "dative", "attr", "oprd"]

print("hello, world")

def get_all_subs(verb):

    pass


def find_svo_s(toks):
    svos = []
    verbs = [tok for tok in toks if tok.pos_ == "VERB" and tok.dep_ != "aux"]
    for v in verbs:
        subs, verbNegated = get_all_subs(v)
        """If no subjects found then don't examine verb any longer"""
        if len(subs) > 0:
            pass
    return svos


def print_dep_s(toks):
    for tok in toks:
        print(tok.orth_, tok.dep_, tok.pos_, tok.head.orth_, [t.orth_ for t in tok.lefts], [t.orth_ for t in tok.rights])
    """EOF"""


def test_svo_s():
    nlp = English()
    tok = nlp("For Halloween Debby and her sister "
              "combined the candy they received. "
              "Debby had 32 pieces of candy while her sister"
              " had 42. If they ate 35 pieces the first night, how many pieces do they have left?")
    svos = find_svo_s(tok)
    print_dep_s(tok)          # prints dependencies
    print(svos)
    """EOF"""


def main():
    test_svo_s()

if __name__ == "__main__":
    main()
