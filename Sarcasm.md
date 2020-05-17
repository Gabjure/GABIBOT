# Sarcasm

>Sarcasm is "a sharp, bitter, or cutting expression or remark; a bitter gibe or taunt". Sarcasm may employ ambivalence, although sarcasm is not necessarily ironic Most noticeable in spoken word, sarcasm is mainly distinguished by the inflection with which it is spoken and is largely context-dependent. [Wikipedia]https://en.wikipedia.org/wiki/Sarcasm (29 April 2020)

>**Sarcasm** noun <br>1.a sharp and often satirical or ironic utterance designed to cut or give pain<br>2. a mode of satirical wit depending for its effect on bitter, caustic, and often ironic language that is usually directed against an individual. [Merriam-Webster]

## Sarcasm Identification

Sarcasm is processed in a part of the brain that not all humans develop. That is the reason why some people understand it faster and/or easiert than others. (https://pubmed.ncbi.nlm.nih.gov/15910115/)

At the same time, sarcasm is cultural which means it varies depending on the country (sarcasm will not be the same in UK than in US or in Barcelona than in Madrid. 

>A French company has developed an analytics tool that claims to have up to 80% accuracy in identifying sarcastic comments posted online.( Kleinman, Zoe (2013-07-03). "Authorities 'use analytics tool that recognises sarcasm'". BBC News. Retrieved July 4, 2013)

Sarcasm detector! I’m really excited!
https://www.washingtonpost.com/blogs/compost/wp/2013/07/11/sarcasm-detector-im-really-excited/ (July 11, 2013)

"According to the BBC, a French company called Spotter has designed a sarcasm detector. It relies on an algorithm and, if Spotter’s estimates are correct, is capable of picking up on about 80 percent of sarcasm. That’s GREAT!"

Authorities 'use analytics tool that recognises sarcasm' (3 July 2013)
https://www.bbc.com/news/technology-23160583
"Its proprietary software uses a combination of linguistics, semantics and heuristics to create algorithms that generate reports about online reputation. It says it is able to identify sentiment with up to an 80% accuracy rate."


https://www.rawstory.com/2013/07/data-analytics-firm-spotter-launches-social-media-sarcasm-detector/amp/

-----------

>In June 2014, the United States Secret Service requested bids for software that would identify sarcasm in tweets.( Pauli, Darren (4 Jun 2014). "Oh, wow. US Secret Service wants a Twitter sarcasm-spotter". Retrieved 2014-06-04.)

Oh, wow. US Secret Service wants a Twitter sarcasm-spotter
https://www.theregister.co.uk/2014/06/04/secret_service_wants_twitter_sarcasm_radar/
"The US Secret Service wants to identify sarcastic tweeters from the serious in a bid that will surely cause its software to sink and buckle.

A tender issued by the security agency sought a way to determine sentiment, identify influencers and section off those exercising the lowest form of wit across the twitter sphere.
[...]
The agency already uses the Federal Emergency Management Agency's Twitter analysis platform but the new system would be a step up."

---------------

https://github.com/MathieuCliche/Sarcasm_detector

http://www.thesarcasmdetector.com/


NLP project for the U.S.S.S: Website that "detects" sarcasm based on **Supervised** training of Classification. 

- Getting DATA

Creator used the Twitter API (https://developer.twitter.com/en) and collected 20K clean sarcastic TW and 100k clean non-sacastic TW for 3 weeks. He further explains the issues he had with the tweets in the website and I could go back for reference in case I end up using the Twitter API.

- DATA Preprocess
Discards:
  tweets with http addresses or that start with @.
  Non-english
Removal of NON-ASCII, hashtags and tags, mentions and duplicates

- Feature engineering

After Cross-Validation most important features were:
  
  n-grams (unigrams & bigrams) important to tokenized, stemmed, uncapitalize begore adding to binary feature dictionary (in this case) 
 
 sentiments (starts positive ends negative: I love being cheated on) he split in 2-3 parts and did sentiment analysis with SentiWordNet (gives a positive and a negative sentiment score to each word of the English language) other library (python built-in) is TextBlob
 
 topics: To learn the topics, I used the python library gensim which implements topic modeling using latent Dirichlet allocation (LDA). We first feed all the tweets to the topic modeler which learns the topics. Then each tweet can be decomposed as a sum of topics, which we use as features.

- Classifier:
  
  Given that's a sparse matrix with a large number of nominal features from the n-grams its critical that's encoded in a sparse matrx. He tried naives Bayes, Logistic Regression and SVM (with linear kernel). Best result in CrossVal came from SVM with an euclidean regularization coefficient of 0.1.
  
  The metric used was **_F-Score**_, (mean of precision and recall.) because there was 5to1 non-sarc tweets. Using _accuracy_ would have been misleading, because it would have been correct predictions / total data. Using _prediction_ would have been correctly identified / total data classified as sarcastic and _recall_ would have been correctly identified / total of sarcastic data in the cross validation set.
  
 -Results and Insights:
 
  Sentiment Analysis: Sarcastic tweets are overall slightly more positive than non-sarcastic tweets and that the first half of a sarcastic tweet is more often positive while the last half of a sarcastic tweet is more often negative. Subjectivity is importat, it's measured by Textblolb (sarcastic tweets are more about expressing feelings, either positive or negative, than non-sarcastic tweets)
  
 - Improvements: 
 
  Incorporate a spell check for the tweets - (I did some preliminary experiments with the spell check of the library Textblob but I did not get any improvements using it, perhaps a better spell checker would do better)
  
 - Back end: Python with Numpy, Scipy, Scikit-learn, NLTK, gensim, Textblob and tweepy.

---------------

**Github Sarcasm detection Repos**

https://github.com/topics/sarcasm-detection?l=python

---------------

Detecting Sarcasm with Deep Convolutional Neural Networks

https://medium.com/dair-ai/detecting-sarcasm-with-deep-convolutional-neural-networks-4a0657f79e80 (Apr 30, 2018)

Medium article on a paper that addresses a key NLP problem known as sarcasm detection using a combination of models based on convolutional neural networks (CNNs). (paper uploaded: A Deeper Look into Sarcastic Tweets Using Deep Convolutional Neural Networks) REPO: https://github.com/SenticNet/CASCADE



