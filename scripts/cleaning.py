import json
import pandas as pd

# first few characters ("XYZ = ") manually deleted
with open('tweet.js') as f:
    raw_data = json.load(f)

cleaned_data = [{'id': int(x['id_str']), 
          'created_at': x['created_at'],
          'retweets': int(x['retweet_count']),
          'favorites': int(x['favorite_count']),
          'images': len(x['entities']['media']) if 'entities' in x and 'media' in x['entities'] else 0,
          'urls': len(x['entities']['urls']) if 'entities' in x and 'urls' in x['entities'] else 0,
          'hashtags': len(x['entities']['hashtags']) if 'entities' in x and 'hashtags' in x['entities'] else 0,
          'users_mentioned': len(x['entities']['user_mentions']) if 'entities' in x and 'user_mentions' in x['entities'] else 0,
          'display_text_length': int(x['display_text_range'][1]) - int(x['display_text_range'][0]),
          'full_text_lines': x['full_text'].count('\n') + 1,
          'full_text': x['full_text'],
          'source': "https://twitter.com/python_tip/status/" + x['id_str'],
          'raw_data_position': i
          } 
         for i,x in enumerate(data) if 'in_reply_to_status_id' not in x and x['retweeted'] is False]

cleaned_df = pd.DataFrame(cleaned_data, columns=cleaned_data[0].keys())
cleaned_df.to_csv("tweet_cleaned.csv", index=False)


