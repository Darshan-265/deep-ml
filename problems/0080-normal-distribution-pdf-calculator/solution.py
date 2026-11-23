import math
import numpy as np

def normal_pdf(x, mean, std_dev):
    

    val = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5*((x-mean)/std_dev)**2)
    return round(val,5)