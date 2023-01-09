import pymarketer as pm

# Get basic stats about your csv.
csv = "https://raw.githubusercontent.com/erickbytes/pymarketer/main/Stars.csv"
summary = pm.analyze_csv(csv)
print(summary)

# Use a template to make requests http code.
http_code = pm.http_template()
print(f"Generated requests module http code:\n {http_code}")

# Split csvs equally into a list of dataframes.
dfs = pm.csv_split(csv)
 
# Merge a list of csvs into one dataframe.
csvs = ["Cats.csv","Dogs.csv","Humans.csv"]
df = pm.csv_merge(csvs)

# Merge multiple Excel tabs into a single dataframe.
repo = "https://github.com/erickbytes/pymarketer"
xl = f"{repo}/blob/main/Chicago%20Breweries.xlsx?raw=true"
df = pm.merge_tabs(xl)
df.to_csv("Merged Tabs.csv")

# Use ftfy library to smooth data mojibake issues.
text = "your dirty text"
clean_text = pm.fix_mojibake(text)

# Make a wordcloud from a pandas dataframe.
wordcloud = pm.word_cloud(df)
wordcloud.to_file("Text Word Cloud Visualization.jpg")