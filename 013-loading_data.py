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
