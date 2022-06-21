#A library (or dependency) is a prewritten code focused on certain tasks
#Pandas is a popular library for data analysis
#To work with Pandas, first install the Pip package installer for Python
#Run these 3 steps for Linux terminal:
#sudo apt update
#sudo apt install python3-pip
#pip install pandas
#Now, import the Pandas library in Python:
import pandas as pd
#'as' keyword gives an alias
#Pandas generally provide two data structures for manipulating data:
#-DataFrame, a two-dimensional data structure with rows and columns
#-Series, a one-dimensional array of indexed data with actual data and indexes
#A series as a one-dimensional dataframe
#To read a csv file, pandas.read_csv():
csv_path='file.csv'
data=pd.read_csv(csv_path)
#This stores the csv file to a dataframe
type(data) #<class 'pandas.core.frame.DataFrame'>
#To display the first five rows of the dataframe, .head():
data.head()
#To read an Excel file, pandas.read_excel():
xlsx_path='file.xlsx'
data=pd.read_excel(xlsx_path)
#If an ImportError occurs, run this in the Linux terminal:
#pip install openpyxl
#Now, return to Python and execute the code again
type(data) #<class 'pandas.core.frame.DataFrame'>
data.head()
#The dataframe is comprised of rows and columns
#To create a dataframe out of a dictionary, pandas.DataFrame():
teams={'peru':['universitario','binacional'],'españa':['real madrid','espanyol']}
d_teams=pd.DataFrame(teams)
d_teams
#            peru       españa
#0  universitario  real madrid
#1     binacional     espanyol
#To select only a column:
a_teams=d_teams[['peru']]
a_teams
#            peru
#0  universitario
#1     binacional
#To select multiple columns:
b_teams=d_teams[['peru','españa']]
b_teams
#            peru       españa
#0  universitario  real madrid
#1     binacional     espanyol
#To select a specific row and column by their labels, .loc[]:
d_teams.loc[0,'peru'] #'universitario'
#To select a specific row and column by their indexes, .iloc[]:
d_teams.iloc[0,1] #'real madrid'
#To slicing with .loc():
d_teams.loc[0:1,'peru':'españa']
#            peru       españa
#0  universitario  real madrid
#1     binacional     espanyol
#To slicing with .iloc():
d_teams.iloc[0:2,0:1]
#            peru
#0  universitario
#1     binacional
#Note that the last index is not taken into account in .iloc[],
#otherwise it's taken into account in .loc[]
#To view the column as a series, just use one bracket:
c_teams=d_teams['peru']
c_teams
#0    universitario
#1       binacional
#Name: peru, dtype: object
type(c_teams) #<class 'pandas.core.series.Series'>
