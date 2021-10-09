try :
    import numpy as np
    import pandas as pd

    from sklearn.impute import SimpleImputer
    from sklearn.preprocessing import MinMaxScaler

    from sklearn.pipeline import Pipeline
    from sklearn.compose import ColumnTransformer

    from sklearn.linear_model import LinearRegression

    printing = True

    train = pd.read_csv("train.csv")

    print(train.head(), train.shape, train.nunique()) if printing == True else None
except:
    print("some issue")