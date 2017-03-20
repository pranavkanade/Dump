import engine.data_processing.nlp_pipeline as pipe


class DataExtract:
    def __init__(self):
        self.nlp_pipe = pipe.NlpPipe()
        self.nouns = ["NOUN", "PROPN", "PRON"]
        self.punctuations = ["DET", "PUNCT"]
        self.adjective_tag = ["PRP$", "WP$"]

    def data_preprocess(self, question_):
        question_ = self.nlp_pipe.clean_string(question_)
        doc_question = self.nlp_pipe.load_pipeline(question_)
        return doc_question

    # TODO : this needs to be reviewed
    def extract_list_of_tokens(self, question_):
        list_of_required_tokens_in_question = []
        doc_question = self.data_preprocess(question_)

        """
        Check if the token is in the list of above categories,
        if they are then they are not relevant to the classification
        """
        # TODO: This function needs improvement as many irrelevant words are popping up in it
        for token in doc_question:
            if (token.pos_ not in self.nouns and token.pos_ not in self.punctuations) \
                    and (token.tag_ not in self.adjective_tag):
                list_of_required_tokens_in_question.append(token.orth_)

        return list_of_required_tokens_in_question