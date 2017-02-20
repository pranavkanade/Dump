import json


class QuestionExtraction:
    def __init__(self, data_file):
        self.data_file = data_file

    def extract_training_corpus(self):
        # This function returns the corpus as json object(list of dictionaries)
        # this path has to be absolute
        with open('./../../training_data/'+self.data_file, "r") as training_corpus:
            training_corpus = training_corpus.read()
        training_corpus_json = json.loads(training_corpus)
        return training_corpus_json

    def extract_question_with_class(self, training_corpus_json, index):
        question = training_corpus_json[index]
        return question['sQuestion'], question['iClass']

    def extract_question(self, training_corpus_json, index):
        return training_corpus_json[index]['sQuestion']

