# tfidf4zh
中文TF-IDF算法实现，具有提取关键字、摘要、找相似文章的功能,使用Python编写 </br>
本模块依赖jieba分词工具，请提前安装 pip install jieba </br>
使用前需要提前准备好语料库corpus，语料库是string组成的list </br>
导入模块 </br>
import tfidf4zh </br>
新建一个tfidf对象，可添加自己建立的词典 </br>
t = tfidf4zh.TFIDF(corpus, userdict=None) </br>
然后对语料库进行分析 </br>
t.analyze() </br>
导入文章article提取关键字，关键字个数num默认为5 </br>
t.keywords(article, num=5) </br>
提取摘要 </br>
t.summarize(article) </br>
找出语料库中相似度大于similarity的文章 </br>
t.similar_articles(article, similarity)
