# tfidf4zh
中文TF-IDF算法实现，具有提取关键字、摘要、找相似文章的功能
使用前需要提前准备好语料库corpus，语料库是string组成的list
导入模块
import tfidf4zh
新建一个tfidf对象
t = tfidf4zh.TFIDF(corpus)
然后对语料库进行分析
t.analyze()
导入文章article提取关键字，关键字个数num默认为5
t.keywords(article, num=5)
提取摘要
t.summarize(article)
找出语料库中相似度大于similarity的文章
t.similar_articles(article, similarity)
