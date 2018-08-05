import pandas as pd

def cleanData(file):
	df=pd.read_csv('Data/DirtyData/'+file+'Dirty'+'.csv', sep=',',header=None)
	df.iloc[1:,4:10].fillna(value=-1,inplace=True)
	df.iloc[1:,12].fillna(value='Undrafted',inplace=True)
	df.iloc[1:,13:].fillna(value='-1',inplace=True)
	df.to_csv('Data/CleanedData/'+file+'Clean'+'.csv',header=False,index=False)

cleanData(file='CombinePlayersTrain')
cleanData(file='CombinePlayersTest')