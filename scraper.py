import praw
import json
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()
db = {}


def prepare_word(word):
    word = word.lower()
    word = ''.join([char for char in word if char.isalpha() or char == ' '])
    word = ''.join([word + ' ' for word in word.split() if word not in stopwords.words('english')])[:-1]
    word = lemmatizer.lemmatize(word)
    return word


def scrape(number_of_subreddits=100):
    reddit = praw.Reddit(client_id='', client_secret='',
                         user_agent='', username='',
                         password='')
    top_subreddits = reddit.subreddits.popular(limit=number_of_subreddits)
    for subreddit, i in zip(top_subreddits, range(number_of_subreddits)):
        subreddit_name = ''.join([char for char in subreddit.title if char.isalpha() or char == ' '])
        print(subreddit_name + '(' + str(i + 1) + '):')
        db[subreddit.title] = []
        top_posts = list(subreddit.top(limit=None))
        number_of_posts = len(top_posts)
        for post, _ in zip(top_posts, range(number_of_posts)):
            try:
                title = prepare_word(post.title)
                db[subreddit.title].append(title)
                print(_ + 1, 'out of', number_of_posts)
            except:
                pass
    file = open('full_db.json', 'w')
    json.dump(db, file)
    file.close()





