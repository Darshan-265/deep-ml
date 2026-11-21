# --- cell 1 ---
import numpy as np

def normalize(x):
    
    
    rms = np.sqrt(np.mean(x**2, axis=-1, keepdims=True) + 1e-8)
    return x / np.sqrt(rms + 1e-8)