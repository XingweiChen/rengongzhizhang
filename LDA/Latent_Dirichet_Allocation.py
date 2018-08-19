from gensim.models import LdaModel
from gensim.models import TfidfModel
from gensim.corpora import Dictionary


documents = [   "I ate a banana and spinach smoothie for breakfast",
                "I like to eat broccoli and bananas",
                "Chinchillas and kittens are cute",
                "My sister adopted a kitten yesterday",
                "Look at this cute hamster munching on a piece of broccoli"]

# preprocessing the input text
corpus = []
for doc in documents:
    corpus.append(doc.lower().strip().split())
# create dictionary for token in corpus
dct = Dictionary(corpus)
# transfer into corpus
corpus = [dct.doc2bow(doc) for doc in corpus]
# train lda model
lda = LdaModel(corpus, num_topics=2, id2word=dct)

# 参数(bow, minimum_probability=None, minimum_phi_value=None, per_word_topics=False)
# Parameters:
#   bow (list) – Bag-of-words representation of the document to get topics for.
#   minimum_probability (float) – Ignore topics with probability below this value (None by default). If set to None, a value of 1e-8 is used to prevent 0s.
#   per_word_topics (bool) – If True, also returns a list of topics, sorted in descending order of most likely topics for that word. It also returns a list of word_ids and each words corresponding topics’ phi_values, multiplied by feature length (i.e, word count).
#   minimum_phi_value (float) – if per_word_topics is True, this represents a lower bound on the term probabilities that are included (None by default). If set to None, a value of 1e-8 is used to prevent 0s.
# Returns:
#   topic distribution for the given document bow, as a list of (topic_id, topic_probability) 2-tuples.
test = dct.doc2bow("I love Kitten".lower().strip().split())
print(lda.get_document_topics(test))
print(lda[test])

# 参数(word_id, minimum_probability=None)
# 关联的topics for the given word.
# Each topic is represented as a tuple of (topic_id, term_probability).
print(lda.get_term_topics(0))

# ----- 输出指定topic的构成 -----
# 参数(word_id, minimum_probability=None)
# 输出形式 list, format: [(word, probability), … ].
print(lda.get_topic_terms(0))
# 参数(topicno, topn=10)
print(lda.show_topic(0))
# 输出形式 String， format: ‘-0.340 * “category” + 0.298 * “$M$” + 0.183 * “algebra” + … ‘.
# 参数(topicno, topn=10)
print(lda.print_topic(0))


# ----- 输出所有topic的构成 -----
# 默认参数(num_topics=10, num_words=10, log=False, formatted=True）
# 输出形式 String， format: [(0, ‘-0.340 * “category” + 0.298 * “$M$” + 0.183 * “algebra” + … ‘), ...]
print(lda.show_topics())
# [num_topics, vocabulary_size] array of floats (self.dtype)
# which represents the term topic matrix learned during inference.
print(lda.get_topics())

# ----- save and load model -----
lda.save(fname="lda_model")
lda.load(fname="lda_model")
print(lda[test])
