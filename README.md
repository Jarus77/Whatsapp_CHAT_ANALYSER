# WhatsApp Chat Analyzer

WhatsApp Chat Analyzer is a Python application designed to provide insights and analysis of WhatsApp chat data. This README will guide you through the project's structure, features, and usage.

## Project Structure

The project comprises three main Python files:

1. **app.py**: The core application file that utilizes Streamlit to create an intuitive user interface for WhatsApp chat data analysis.

2. **helper.py**: A utility module containing functions tailored for data analysis, statistics calculation, and visualization generation.

3. **preprocessor.py**: This module handles the preprocessing of raw WhatsApp chat data, converting it into a structured DataFrame for analysis.

## Features

WhatsApp Chat Analyzer offers a range of features for gaining valuable insights from WhatsApp chat data:

1. **Data Upload**: Users can easily upload their WhatsApp chat data, typically in plain text format.

2. **Data Preprocessing**: The application processes the uploaded chat data to extract user names, message content, and timestamp information.

3. **User Selection**: Users have the option to focus the analysis on a specific user or gain insights from the entire group chat.

4. **Statistics**: WhatsApp Chat Analyzer provides essential statistics, including message counts, total word usage, media attachment frequency, and shared link tracking.

5. **Timelines**: Users can visualize message activity over time, exploring monthly and daily message trends through interactive line charts.

6. **Most Active Users**: The application identifies and showcases the most active users within the chat, aiding in understanding the chat's dynamics.

7. **Word Clouds**: Users can explore visually captivating word cloud representations that highlight the most frequently used words within the chat.

8. **Most Common Words**: A chart displays the top-ranking words in terms of frequency of usage, offering valuable insights into common chat topics.

9. **Activity Map**: The application reveals key insights such as the most active day, the most active month, and a heatmap illustrating message activity throughout the week.

## Usage

To harness the power of WhatsApp Chat Analyzer, follow these steps:

1. Install the required libraries using the command: `pip install streamlit matplotlib pandas seaborn wordcloud`.

2. Execute the application by running the following command: `streamlit run app.py`.

3. Once the application interface loads, upload your WhatsApp chat data file.

4. Select a specific user for analysis or opt for the "Overall" option to analyze the entire chat.

5. Click the "Show Analysis" button to trigger the generation of insights and visualizations.

# WhatsApp Chat Analyzer - Helper Module (helper.py)

The `helper.py` module is an integral part of the WhatsApp Chat Analyzer project. It contains a set of functions designed to assist in various data analysis tasks when working with WhatsApp chat data. This README will provide an overview of the module's purpose, functions, and how to use them effectively.

## Purpose

The primary purpose of the `helper.py` module is to streamline the analysis and visualization of WhatsApp chat data. It offers a collection of functions that perform tasks such as statistical analysis, data preprocessing, and visualization generation. These functions help users gain meaningful insights from their chat data with minimal effort.

## Functions

Here is a breakdown of the key functions available in the `helper.py` module and their respective purposes:

1. **stats_data(df, selected_user)**:
   - **Purpose**: Calculates and returns statistics about the chat data, including the number of messages, total words, media (e.g., images), and links shared.
   - **Parameters**: `df` (DataFrame) - WhatsApp chat data, `selected_user` (str) - User name for whom to calculate statistics.
   - **Usage**: Used to generate statistical insights for a selected user or the entire chat.

2. **monthly_timeline(selected_user, df)**:
   - **Purpose**: Generates a timeline of message activity on a monthly basis.
   - **Parameters**: `selected_user` (str) - User name for whom to generate the timeline, `df` (DataFrame) - WhatsApp chat data.
   - **Usage**: Provides a visual representation of message activity trends over months.

3. **daily_timeline(selected_user, df)**:
   - **Purpose**: Generates a timeline of message activity on a daily basis.
   - **Parameters**: `selected_user` (str) - User name for whom to generate the timeline, `df` (DataFrame) - WhatsApp chat data.
   - **Usage**: Offers insights into daily patterns of message activity.

4. **most_busy_users(df, selected_users)**:
   - **Purpose**: Identifies and returns the most active users in the chat.
   - **Parameters**: `df` (DataFrame) - WhatsApp chat data, `selected_users` (str) - User name for whom to identify active users.
   - **Usage**: Helps understand which users are most engaged in the conversation.

5. **create_wordcloud(df, selected_user)**:
   - **Purpose**: Generates a word cloud visualization highlighting the most commonly used words.
   - **Parameters**: `df` (DataFrame) - WhatsApp chat data, `selected_user` (str) - User name for whom to create the word cloud.
   - **Usage**: Provides a visual representation of frequently used words within the chat.

6. **most_common_words(df, selected_user)**:
   - **Purpose**: Computes and returns a list of the most frequently used words.
   - **Parameters**: `df` (DataFrame) - WhatsApp chat data, `selected_user` (str) - User name for whom to calculate common words.
   - **Usage**: Helps identify and analyze the most commonly used words in the chat.

7. **week_activity_map(selected_user, df)**:
   - **Purpose**: Provides a count of message activity for each day of the week.
   - **Parameters**: `selected_user` (str) - User name for whom to calculate weekly activity, `df` (DataFrame) - WhatsApp chat data.
   - **Usage**: Reveals patterns in message activity throughout the week.

8. **month_activity_map(selected_user, df)**:
   - **Purpose**: Provides a count of message activity for each month.
   - **Parameters**: `selected_user` (str) - User name for whom to calculate monthly activity, `df` (DataFrame) - WhatsApp chat data.
   - **Usage**: Offers insights into chat activity trends over the months.

9. **activity_heatmap(selected_user, df)**:
   - **Purpose**: Creates a heatmap of message activity for a selected user.
   - **Parameters**: `selected_user` (str) - User name for whom to create the heatmap, `df` (DataFrame) - WhatsApp chat data.
   - **Usage**: Visualizes message distribution throughout the week for the selected user.

## Usage

To use the functions in the `helper.py` module, you need to import them into your analysis script. Here's a basic example of how to use these functions:

```python
import pandas as pd
from helper import stats_data, monthly_timeline, most_busy_users

# Load your WhatsApp chat data into a DataFrame (df)

# Calculate statistics for a specific user
num_of_messages, words, num_media, num_links = stats_data(df, 'User1')

# Generate a monthly timeline for the entire chat
monthly_activity = monthly_timeline('Overall', df)

# Identify the most active users in the chat
active_users, active_users_percent = most_busy_users(df, 'Overall')
```
Certainly, here's a README for the `preprocessor.py` module, explaining its purpose and functions:

# WhatsApp Chat Analyzer - Preprocessor Module (preprocessor.py)

The `preprocessor.py` module is a critical component of the WhatsApp Chat Analyzer project. It focuses on preprocessing raw WhatsApp chat data, transforming it into a structured and usable format. This README provides an overview of the module's purpose, functions, and how to utilize them effectively.

## Purpose

The primary purpose of the `preprocessor.py` module is to facilitate the initial steps of data preparation when dealing with WhatsApp chat data. It parses the raw data, extracts relevant information, and organizes it into a DataFrame for further analysis. This preprocessing is crucial to ensure data consistency and enable downstream analysis.

## Functions

Below are the essential functions available in the `preprocessor.py` module and their respective purposes:

1. **preprocess2(data)**:
   - **Purpose**: This function performs preprocessing on the raw WhatsApp chat data.
   - **Parameters**: `data` (str) - Raw chat data in plain text format.
   - **Usage**: Converts raw data into a structured DataFrame containing columns for user names, message content, and timestamps.

## Usage

To utilize the `preprocess2` function in the `preprocessor.py` module, follow these steps:

1. Import the function into your script:

   ```python
   from preprocessor import preprocess2
   ```

2. Load your WhatsApp chat data (in plain text format) into a string variable, for example:

   ```python
   chat_data = """
   01/01/2022, 14:30 - User1: Hello there!
   01/01/2022, 14:32 - User2: Hi! How are you?
   ...
   """
   ```

3. Call the `preprocess2` function and pass your chat data as an argument:

   ```python
   df = preprocess2(chat_data)
   ```

4. The `df` variable now contains the preprocessed chat data in the form of a pandas DataFrame. You can further analyze, visualize, and gain insights from this structured data.

## Data Privacy

Always exercise caution and respect privacy when working with chat data. Ensure that you have the necessary permissions to use the data for analysis.

## License

This module is licensed under the MIT License. For more information, please refer to the project's [LICENSE](LICENSE) file.

---

Feel free to adapt and customize this README to your specific project's details and requirements.
