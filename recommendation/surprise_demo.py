from surprise import SVD
from surprise import Dataset
from surprise.model_selection import cross_validate
import pandas as pd
data = Dataset.load_builtin('ml-100k')
import rpy2
data.df