import engine.data_processing.extract_question as qe

q_extract = qe.QuestionExtraction("js_corpus.json")

training_corpus = q_extract.extract_training_corpus()

question = q_extract.extract_question(training_corpus, 0)

print(question)


# http://localhost:8888/tree?token=6de971b592cc72617deb72912a546e45fda94f9d4a37af06#notebooks
