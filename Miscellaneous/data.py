import pandas as pd

# Read the csv file in
df = pd.read_csv(r"C:\Users\jlper\Web\Web-Design-Challenge\Resources\cities.csv", delimiter=",")

df.reset_index(inplace=True)
df.drop(['index'], axis=1, inplace=True)

#print(df.columns)

# Save to file
df.to_html('data_table.html', index=False)

# Assign to string
#table = df.to_html()
#print(table)
