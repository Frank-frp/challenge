from typing import List, Tuple
import pandas as pd
import re

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    
    # Leer el archivo de datos
    data = pd.read_json(file_path, lines=True)
    
    # Extraer los emojis de los textos de los tweets
    emoji_pattern = re.compile("[\U00010000-\U0010FFFF]", flags=re.UNICODE)
    data['emojis'] = data['text'].apply(lambda x: emoji_pattern.findall(x))
    
    # Contar los emojis
    emoji_counts = data['emojis'].explode().value_counts().head(10)
    
    return list(emoji_counts.items())

    