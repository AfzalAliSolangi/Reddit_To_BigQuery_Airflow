import pandas as pd
from reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_tsv

CLIENT_ID = 'RxWhNdPbPyGQB1FAxOlT7g'
SECRET = 'kimgRV1argok5ZKZ59WBU8JsMv4Srg'
OUTPUT_PATH = '/home/afzal' 
file_name = 'Reddit_pulled'
subreddit = 'GTA6'


def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    # connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Afzal_030828 Agent')
    # extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    # transformation
    post_df = transform_data(post_df)
    # loading to csv
    file_path = f'{OUTPUT_PATH}/{file_name}.tsv'
    load_data_to_tsv(post_df, file_path)

    return file_path

reddit_pipeline(file_name,subreddit)