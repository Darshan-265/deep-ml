# --- cell 1 ---
import numpy as np
# You can use sklearn! For example:
from sklearn.decomposition import PCA
from sklearn.random_projection import GaussianRandomProjection

class MyReducer:

    
    
    def __init__(self):
        self.n_components = 10
        self.reducer= PCA(n_components=self.n_components,svd_solver="full" )

    
    def fit(self, X):
        
        self.reducer.fit(X)
        
        # TODO: Fit your dimensionality reduction
        return self
    
    def transform(self, X):
        return self.reducer.transform(X)
        
    def fit_transform(self, X):
        return self.reducer.fit_transform(X)