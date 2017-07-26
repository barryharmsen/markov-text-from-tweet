# markov-text-from-tweet
Generate random texts based on a collection of tweets, using Markov Chains. This example uses tweets from Donald Trump (@realdonaldtrump), which were downloaded from [here](https://github.com/bpb27/trump-tweet-archive/tree/master/data/realdonaldtrump)

Files need to be stored in the 'tweets' subfolder.

# Usage

### Building the dictionary ###
Run generate_dict.py to generate the dictionary of word pairs

### Generate a random text ###
Run random_text.py using the following parameters:

-wp or --wordpair, a pair of words to using as the starting point for the text. Example: -wp The President

-l or --length, the max number of words that should be generated

-d or --dict, the dictionary file to use. Defaults to dict.json

# Example

__Input__: python random_text.py -wp President Obama -l 25

__Result__: >President Obama & Democrat leaders did a nasty cartoon attacking @tedcruz kids Bad
