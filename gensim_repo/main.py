# this file is to test if the gensim can provide the text to vector format

# from gensim import corpora
import engine.data_processing.extract_data_for_classification as dfc
import engine.data_processing.extract_question as qe
# from collections import defaultdict
# from pprint import pprint
import pickle

if __name__ == "__main__":
    training_corpus = qe.QuestionExtraction("js_corpus.json")
    training_corpus_json = training_corpus.extract_training_corpus()


    # Extracting 10 questions from js_corpus in list
    questions = [training_corpus.extract_question(training_corpus_json, i) for i in range(len(training_corpus_json))]

    list_list_processed_tokens = [dfc.DataExtract().extract_list_of_tokens(questions[i]) for i in range(len(questions))]

    processed_tokens_pickled = open('processed_tokens.pkl', 'wb')
    pickle.dump(list_list_processed_tokens, processed_tokens_pickled)

    # frequency = defaultdict(int)
    # for list_token in list_list_processed_tokens:
    #     for token in list_token:
    #         frequency[token] += 1
    #
    # list_list_processed_tokens = [[token for token in list_token if frequency[token] > 1] for list_token in list_list_processed_tokens]
    # pprint(list_list_processed_tokens)
    #
