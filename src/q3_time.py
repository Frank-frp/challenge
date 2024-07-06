from typing import List, Tuple
import pandas as pd

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    
    # Leer el archivo de datos
    data = pd.read_json(file_path, lines=True)
    
    # Contar las menciones de usuarios
    mention_counts = data['text'].str.extractall(r'(@\w+)')[0].value_counts().head(10)
    
    return list(mention_counts.items())