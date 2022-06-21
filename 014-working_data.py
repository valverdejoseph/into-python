import pandas as pd
teams={'peru':['universitario','binacional'],'españa':['real madrid','espanyol'],'portugal':['porto','porto']}
data=pd.DataFrame(teams)
#To determine the unique items in a column, .unique():
data['portugal'].unique() #array(['porto'], dtype=object)
data['peru'].unique() #array(['universitario', 'binacional'], dtype=object)
#Dataframes can be manipulated with boolean operations:
data['españa']=='porto'
#0    False
#1    False
#Name: españa, dtype: bool
data['portugal']=='porto'
#0    True
#1    True
#Name: portugal, dtype: bool
#To select the specified rows in a line:
por=data[data['portugal']=='porto']
por
#            peru       españa portugal
#0  universitario  real madrid    porto
#1     binacional     espanyol    porto
por=data[data['portugal']=='por']
por
#Empty DataFrame
#Columns: [peru, españa, portugal]
#Index: []
#To save the dataframe in a csv file, .to_csv():
csv_path='Documents/the_dataframe.csv'
data.to_csv(csv_path)
