from typing import List, Tuple
from datetime import datetime
import pandas as pd

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:

    date_counts = {}
    user_counts = {}
    chunksize = 100000
    for chunk in pd.read_json(file_path, lines=True, chunksize=chunksize):
        chunk['date'] = pd.to_datetime(chunk['date'])
        chunk['date_only'] = chunk['date'].dt.date
        
        for date, group in chunk.groupby('date_only'):
            date_counts[date] = date_counts.get(date, 0) + len(group)
            user_counts[date] = user_counts.get(date, {})
            
            for user in group['user'].apply(lambda x: x['username']):
                user_counts[date][user] = user_counts[date].get(user, 0) + 1
    
    top_dates = sorted(date_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    
    result = []
    for date, _ in top_dates:
        top_user = max(user_counts[date].items(), key=lambda x: x[1])[0]
        result.append((date, top_user))
    
    return result


