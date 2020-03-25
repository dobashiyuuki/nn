# -*- coding: utf-8 -*-
# from . import helpers
from sklearn.datasets import load_iris

def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())

# load datasets
iris_data = load_iris()
print(iris_data)
