from typing import List, Tuple
import pandas as pd
import re

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    
    # Inicializar el contador de emojis
    emoji_counts = {}
    
    # Definir el patrón de emojis
    emoji_pattern = re.compile("[\U00010000-\U0010FFFF]", flags=re.UNICODE)
    
    # Procesar el archivo en chunks
    chunksize = 100000
    for chunk in pd.read_json(file_path, lines=True, chunksize=chunksize):
        chunk['emojis'] = chunk['text'].apply(lambda x: emoji_pattern.findall(x))
        
        for emojis in chunk['emojis']:
            for emoji in emojis:
                emoji_counts[emoji] = emoji_counts.get(emoji, 0) + 1
    
    top_emojis = sorted(emoji_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    
    return top_emojis