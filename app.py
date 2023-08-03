import streamlit as st
from matplotlib import pyplot as plt
from matplotlib.pyplot import subplots
from preprocessor import preprocess2
from helper import stats_data, monthly_timeline, daily_timeline, most_busy_users, create_wordcloud, most_common_words, \
    activity_heatmap, month_activity_map, week_activity_map
import seaborn as sns

st.sidebar.title("Whatsapp Chat Analyser")
uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocess2(data)
    st.dataframe(df)
    # fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.sort()
    # user_list.remove('group_notification')
    user_list.insert(0, "Overall")
    selected_user = st.sidebar.selectbox("Show Analysis Chart", user_list)

    # number of Messages, words lenth,num_media, len(links)
    if st.sidebar.button("Show Analysis"):
        num_of_messages, words, num_media, num_links = stats_data(df, selected_user)
        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Messages")
            st.title(num_of_messages)

        with col2:
            st.header("Words")
            st.title(words)

        with col3:
            st.header("Media")
            st.title(num_media)

        with col4:
            st.header("Links")
            st.title(num_links)

        st.title("Monthly Timeline")
        timeline = monthly_timeline(selected_user, df)
        fig, ax = subplots()
        ax.plot(timeline['time'], timeline['message'], color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        st.title("Daily Timeline")
        timeline = daily_timeline(selected_user, df)
        fig, ax = subplots()
        ax.plot(timeline['only_date'], timeline['message'], color='red')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        ##### MOST BUSY USERS #####

        st.title("Most Busy Users")
        x, new_df = most_busy_users(df, selected_user)

        fig, ax = subplots()
        col1, col2 = st.columns(2)
        with col1:
            ax.bar(x.index, x.values, color='blue')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.dataframe(new_df)
        ###### Word Colud###

        st.title("Word Cloud")
        df_wc = create_wordcloud(df, selected_user)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)



        ##### MOST Common Words####

        st.title('Most Common Words')
        most_common_df = most_common_words(df, selected_user)
        fig, ax = subplots()

        ax.barh(most_common_df[0], most_common_df[1])
        plt.xticks(rotation='vertical')

        st.pyplot(fig)

        ####ACtivity Map#####
        # activity map
        st.title('Activity Map')
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='purple')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        st.title("Weekly Activity Map")
        user_heatmap = activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)
