'''
    Generate a random text from a dictionary of word pairs using Markov chains
'''

import json
import random
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Generate a random text from a \
                                                  dictionary of word pairs \
                                                  using Markov chains')
    parser.add_argument('-wp', '--wordpair',
                        metavar='word',
                        required=True,
                        nargs=2, help='A pair of two words to use as a starting \
                                       point for the text. Example: \'-wp The \
                                       President\'')
    parser.add_argument('-l', '--length',
                        metavar='length',
                        default=15,
                        type=int,
                        help='The max length of the required text, in the number of \
                              words')

    parser.add_argument('-d', '--dict',
                        metavar='dictionary file',
                        default='dict.json',
                        help='The JSON dictionairy with word pairs to use for the \
                              text, defaults to dict.json')

    args = parser.parse_args()

    file_dict = args.dict
    word_1 = args.wordpair[0]
    word_2 = args.wordpair[1]
    length = args.length

    text = '%s %s' % (word_1, word_2)

    with open(file_dict, "r") as infile:
        wp_dict = json.load(infile)
    for i in range(0, length - 2):
        key = '%s,%s' % (word_1, word_2)
        if key in wp_dict:
            word_3 = random.choice(wp_dict[key])
            text = '%s %s' % (text, word_3.encode('utf8'))
            word_1 = word_2
            word_2 = word_3
        else:
            break

    if i == 0:
        print 'Could not generate text based on word pair "%s, %s"' % (word_1, word_2)
    else:
        print text
