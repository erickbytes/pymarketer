# pymarketer
An HTTP + spreadsheet toolset

Install this Python library from this repo with pip:
<pre><code>python -m pip install git+https://github.com/erickbytes/pymarketer.git</code></pre>

Install Python library dependencies

<pre><code>pip install chardet
pip install ftfy
pip install numpy
pip install pandas
pip install wordcloud
</code></pre>

Refer to [pymarketer_examples.py](https://github.com/erickbytes/pymarketer/blob/main/pymarketer_examples.py) to see the functions for:
- show csv basic stats summary
- merging + splitting csv files
- merging the tabs of an xlsx file into a pandas dataframe
- HTTP requests code generator
- clean text with ftfy
- make a word cloud visualization from pandas dataframe

Check out the [__init__.py](https://github.com/erickbytes/pymarketer/blob/main/pymarketer/__init__.py) file to see the function implementations.

basic csv analysis summary

<pre><code>import pymarketer as pm
# Get basic stats about your csv.
csv = "Stars.csv"
summary = pm.analyze_csv(csv)
print(summary)
>>> csv name:   'Stars.csv'
    encoding:   'ascii'
    rows:       8
    columns:    2
    duplicates: 0
</code></pre>

requests http template code generator

<pre><code>http_code = pm.http_template()
print(f"Generated requests module http code:\n {http_code}")
>>> Generated requests module http code:
r = requests.request(
    url="https://yourapi.com/stuff?drink=tea",
    method="GET",
    headers={"Content-Type": "application/json", "Cache-Control": "no-cache"},
)
# Note: this example is after formatting the generated code with black.
</code></pre>

merge xlsx excel spreadsheet tabs

<pre><code># Merge multiple Excel tabs into a single dataframe.
repo = "https://github.com/erickbytes/pymarketer"
xl = f"{repo}/blob/main/Chicago%20Breweries.xlsx?raw=true"
df = pm.merge_tabs(xl)
df.to_csv("Merged Tabs.csv", index=False)
</code></pre>

word cloud generation

<pre><code># Make a wordcloud from a pandas dataframe.
wordcloud = pm.word_cloud(df)
wordcloud.to_file("Text Word Cloud Visualization.jpg")
</code></pre>

![example python world cloud](https://github.com/erickbytes/pymarketer/blob/main/Text%20Word%20Cloud%20Visualization.jpg)

additional recommended python libraries
- ruff: linter
- black: code formatter
- sqlfluff: SQL linter
- pelican: static site generator
- pyautogui: user interface automation
- pytrends: search engine research