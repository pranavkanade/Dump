import engine.data_processing.extract_data_for_classification as dfc
import engine.data_processing.extract_question as qe

if __name__ == "__main__":
    index = 1   # index of the question which you want to extract
    training_corpus = qe.QuestionExtraction("js_corpus.json")
    training_corpus_json = training_corpus.extract_training_corpus()

    # This question var contains the raw string that is pulled from corpus
    question = training_corpus.extract_question(training_corpus_json, index)

    # This call will automatically returns the list of processed tokens from the question
    # doc_question will contain the process 'DOC' object of the question string.
    list_of_processed_tokens, doc_question = dfc.DataExtract().extract_list_of_tokens(question)

    print(list_of_processed_tokens)