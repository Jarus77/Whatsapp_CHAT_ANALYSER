# number of Messages, words lenth,num_media, len(links)
import re
from collections import Counter

from urlextract import URLExtract
from wordcloud import WordCloud
# import emoji
import pandas as pd

extract = URLExtract()
f = open('stop_hinglish.txt')
stop_words = f.read()


def stats_data(df, selected_user):
    unwanted_messages = [
        'This message was deleted',
        'created group',
        'Messages and calls are end-to-end encrypted',
        'Bhushan Khandare added'
    ]
    mask = df['message'].apply(lambda msg: not any(unwanted_mesg in msg for unwanted_mesg in unwanted_messages))
    df = df[mask]

    if selected_user == 'Overall':
        num_of_messages = df.shape[0]

        words = ' '.join(df['message'])
        words = re.findall(r'\b\w+\b', words)
        words = len(words)

        num_media = df[df['message'] == '<Media omitted>\n'].shape[0]
        links = []
        for message in df['message']:
            links.extend(extract.find_urls(message))

    else:
        num_of_messages = df[df['user'] == selected_user].shape[0]
        new_df2 = df[df['user'] == selected_user]
        words = ' '.join(new_df2['message'])
        words = re.findall(r'\b\w+\b', words)
        words = len(words)

        num_media = new_df2[new_df2['message'] == '<Media omitted>\n'].shape[0]

        links = []
        for message in new_df2['message']:
            links.extend(extract.find_urls(message))

    return num_of_messages, words, num_media, len(links)


def monthly_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline


def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline2 = df.groupby(['only_date']).count()['message'].reset_index()
    return timeline2


def most_busy_users(df, selected_users):
    x = df['user'].value_counts().head()
    new_df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percent'})
    return x, new_df


def create_wordcloud(df, selected_user):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    def remove_stop_words(message):
        y = []
        for words in message.lower().split():
            if words not in stop_words:
                y.append(words)
        return " ".join(y)

    temp['message'].apply(remove_stop_words)
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))

    return df_wc

def most_common_words(df, selected_user):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df


def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()


def month_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()


def activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)
    return user_heatmap
