'''
    Create a dictionary of word pairs from a (collection of) Twitter JSON
    file(s). This example uses the tweets from Donald Trump (@realdonaldtrump),
    which were downloaded from here:

    https://github.com/bpb27/trump-tweet-archive/tree/master/data/realdonaldtrump

    Files need to be stored in the 'tweets' subfolder.
'''

import json
import glob

wp_dict = dict()


def load_tweets():
    for file in glob.glob('tweets/*.json'):

        print 'Processing: %s' % file
        with open(file, "r") as tweet_file:
            tweets = json.load(tweet_file)

            for tweet in tweets:

                # Exclude retweets (Trump sometimes retweets by using double quotes)
                if tweet['is_retweet'] == False and tweet['text'][0] != '"':
                    text = tweet['text'].replace('.', '').replace(',', '').replace('!', '').replace('&amp;', '&')

                    words = text.split()

                    if len(words) >= 3:
                        for i in range(len(words) - 2):
                            word_1 = words[i]
                            word_2 = words[i+1]
                            word_3 = words[i+2]

                            key = '%s,%s' % (word_1, word_2)

                            if (key) in wp_dict:
                                wp_dict[key].append(word_3)
                            else:
                                wp_dict[key] = [word_3]

    with open('dict.json', 'w') as outfile:
        json.dump(wp_dict, outfile)


if __name__ == "__main__":
    load_tweets()
