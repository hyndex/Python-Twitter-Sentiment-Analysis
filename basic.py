from textblob import TextBlob
random_text=TextBlob("jyotisman is very very angry that, he gets a new girlfriend every week...")
print('Sentence = jyotisman is very very angry that, he gets a new girlfriend every week...')

print('lexicon =>',random_text.pos_tags)

print('words => ',random_text.words)

print('Result =>',random_text.sentiment.polarity)
