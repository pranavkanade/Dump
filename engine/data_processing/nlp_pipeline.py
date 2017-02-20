"""
This is to load the nlp pipeline from spacy.io library
This may parse the input question and store the object gained from it
"""
import spacy
#import engine.data_processing.extract_question as qe


class NlpPipe:
    def __init__(self):
        self.nlp = spacy.load('en')

    @staticmethod
    def clean_string(question_=""):
        return question_.strip()

    def load_pipeline(self, question_):
        """
        This loads the pipeline and parses the whole string.
        It will annotate the input question string
        :param question_:
        :return: doc
        """
        doc = self.nlp(question_)
        return doc

    def list_sentences(self, question_=""):
        """
        Returns the list of sentences in question string
        :param question_:
        :return list_question_sentences:
        """
        question_ = self.clean_string(question_=question_)
        doc_question_ = self.nlp(question_)
        list_question_sentence = []
        for span in doc_question_.sents:
            sent = ''.join(doc_question_[i].string for i in range(span.start, span.end)).strip()
            list_question_sentence.append(sent)
        return list_question_sentence

# if __name__ == "__main__":
#     q_extract = qe.QuestionExtraction("js_corpus.json")
#
#     training_corpus = q_extract.extract_training_corpus()
#
#     question = q_extract.extract_question(training_corpus, 0)
#
#     print(question)
#     print('***************')
#     print(NlpPipe.clean_string(question_=question))
#     print('***************')
#     print(NlpPipe().list_sentences(question_=question))
