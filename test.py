import engine.data_processing.extract_question as qe

q_extract = qe.QuestionExtraction("js_corpus.json")

training_corpus = q_extract.extract_training_corpus()

question = q_extract.extract_question(training_corpus, 0)

print(question)

