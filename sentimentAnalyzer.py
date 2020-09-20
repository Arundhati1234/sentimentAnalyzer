
'''
Data provided:
1. project_twitter_data.csv has the text of a tweet, the number of retweets of that tweet,  and the number of replies to
that tweet
2. words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt

Task: Build a sentiment classifier, which will detect how positive or negative each tweet is.
Create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score
(which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet),
and the Net Score for each tweet. '''

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(st):
    for i in range(0, len(st)):
        if st[i] in punctuation_chars:
            st = st.replace(st[i], ' ')
    return st


def get_pos(st):
    new_st = strip_punctuation(st).lower().split()
    count = 0
    for word in new_st:
        if word in positive_words:
            count = count + 1
    return count


def get_neg(st):
    new_st = strip_punctuation(st).lower().split()
    count = 0
    for word in new_st:
        if word in negative_words:
            count = count + 1
    return count


# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

init_data = open("project_twitter_data.csv", 'r')
twitter_data = init_data.readlines()

final_data = open("resulting_data.csv", 'w')
final_data.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
final_data.write('\n')

for lines in twitter_data[1:]:
    each_line = lines.split(',')
    c_pos = get_pos(each_line[0])
    c_neg = get_neg(each_line[0])
    c_net = c_pos - c_neg
    final_data.write('{},{},{},{},{}'.format(each_line[1], each_line[2].strip('\n'), c_pos, c_neg, c_net))
    final_data.write('\n')

init_data.close()
final_data.close()



