from typing import List, Tuple
from datetime import datetime
import pandas as pd

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:

    data = pd.read_json(file_path, lines=True)
    data['date'] = pd.to_datetime(data['date'])
    data['date_only'] = data['date'].dt.date
    tweet_counts = data['date_only'].value_counts().head(10)
    
    for date in tweet_counts.index:
        daily_tweets = data[data['date_only'] == date]
        top_user = daily_tweets['user'].apply(lambda x: x['username']).value_counts().idxmax()
        ([]).append((date, top_user))
    
    return []

