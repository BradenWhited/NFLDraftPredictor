import pandas as pd
from sklearn.model_selection import train_test_split

# Reads in cleaned data and separates X and Y Values
df = pd.read_csv('Data/CleanedData/CombinePlayersTrainClean.csv', header=None)
X = df.iloc[1:,:11].values
Y = df.iloc[1:,13].values

# Separate X and Y values into a train and a validation set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

print(X_train)
print(X_test)