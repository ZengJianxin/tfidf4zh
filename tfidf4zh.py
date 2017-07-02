from collections import Counter
import math

import jieba


class TFIDF:

    def __init__(self, corpus, userdict=None):
        self.corpus = corpus
        self.cutted_corpus = []
        self.userdict = userdict

    def analyze(self):
        if self.userdict:
            jieba.load_userdict(self.userdict)
        for article in self.corpus:
            c = Counter()
            for word in jieba.cut(article):
                c[word] += 1
            self.cutted_corpus.append(c)

    def keywords(self, article, num=5):
        word_counter = Counter()
        for word in jieba.cut(article):
            word_counter[word] += 1
        word_num = sum(word_counter.values())
        tfidf = []
        for key, value in word_counter.items():
            tf = value / word_num
            c = 1
            for article in self.cutted_corpus:
                if key in article:
                    c += 1
            idf = math.log(len(self.cutted_corpus) / c)
            tfidf.append((key, tf * idf))
            tfidf.sort(key=lambda x: x[1], reverse=True)
        return [x[0] for x in tfidf[:num]]

    def similar_articles(self, article, similarity):
        similar_articles = []
        word_counter = Counter()
        for word in jieba.cut(article):
            word_counter[word] += 1
        for i in range(len(self.cutted_corpus)):
            words = set(word_counter.keys()).union(self.cutted_corpus[i].keys())
            numerator, denominator = 0, 0
            for word in words:
                numerator += word_counter[word] * self.cutted_corpus[i][word]
                denominator += word_counter[word]**2 + self.cutted_corpus[i][word]**2
            if numerator / denominator >= similarity:
                similar_articles.append(self.corpus[i])
        return similar_articles

    def summarize(self, article, keywords_num=3, puns = '。！？'):
        summary = []
        keywords = self.keywords(article, keywords_num)
        start = 0
        sentences = []
        for i in range(len(article)):
            if article[i] in puns:
                sentences.append(article[start:i+1])
                start = i + 1
        sentences.append(article[start:])
        for sentence in sentences:
            if len(keywords) == 0:
                break
            for keyword in keywords:
                if keyword in jieba.lcut(sentence):
                    if sentence not in summary:
                        summary.append(sentence)
                    keywords.remove(keyword)
        return ''.join(summary)
        

__version__ = 0.01
