import pandas as pd

# Variables for read_csv
original_table = '../databases/Summer-Olympic-medals-1976-to-2008.csv'
original_cols = ['Year','Discipline', 'Country', 'Medal']
encoding='latin-1'

# Reading the csv data
original_csv_df = pd.read_csv(original_table, usecols=original_cols, encoding=encoding )

# Filtering data to only contain rows from Beijiing 2008 Olympics
beijing_data = original_csv_df[original_csv_df['Year'] == 2008]

# Grouping the rows so we can get a count of medals for each country by each discipline
beijing_data_country_sum = beijing_data.groupby(by=['Discipline','Country'])["Medal"].count().reset_index()

# for index, row in beijing_data_country_sum.iterrows():