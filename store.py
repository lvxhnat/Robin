def sigmoid(p): 
    return 1 / (1 + np.e ** -p)

def logit(p): 
    return np.log(p / (1 - p))