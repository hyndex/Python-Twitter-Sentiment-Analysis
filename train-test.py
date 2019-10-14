from textblob import TextBlob

train = [('I love this sandwich.', 'pos'),
         ('this is an amazing place!', 'pos'),
         ('I feel very good about these beers.', 'pos'),
         ('this is my best work.', 'pos'),
         ("what an awesome view", 'pos'),
         ('I do not like this restaurant', 'neg'),
         ('I am tired of this stuff.', 'neg'),
         ("I can't deal with this", 'neg'),
         ('he is my sworn enemy!', 'neg'),
         ('my boss is horrible.', 'neg')
    ]
tests = [('the beer was good.', 'pos'),
         ('I do not enjoy my job', 'neg'),
         ("I ain't feeling dandy today.", 'neg'),
         ("I feel amazing!", 'pos'),
         ('Gary is a friend of mine.', 'pos'),
         ("I can't believe I'm doing this.", 'neg')
    ]
    
    
from textblob.classifiers import NaiveBayesClassifier
cl = NaiveBayesClassifier(train)

print("original test data => ",tests,"\n\n\n")
for test in tests:
    print(test[0],'=>',cl.classify(test[0]))
