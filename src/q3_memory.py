from typing import List, Tuple

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    
    # Inicializar el contador de menciones
    mention_counts = {}
    
    # Procesar el archivo en chunks
    chunksize = 100000
    for chunk in pd.read_json(file_path, lines=True, chunksize=chunksize):
        mentions = chunk['text'].str.extractall(r'(@\w+)')[0]
        
        for mention in mentions:
            mention_counts[mention] = mention_counts.get(mention, 0) + 1
    
    
    return sorted(mention_counts.items(), key=lambda x: x[1], reverse=True)[:10]