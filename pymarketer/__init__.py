# import requests
import pandas as pd
import numpy as np
import chardet
import ftfy
from wordcloud import WordCloud


def http_template():
    """Accepts http request info, formats as generic requests code.
    This request can be called:
    import requests
    r = requests.request(url=""...
    print(r.text)
    
    docs: https://requests.readthedocs.io/en/latest/api/#requests.request
    """
    endpoint = input("enter endpoint url, ex. https://yourapi.com/stuff\n")
    method = input("enter method: GET,PATCH,POST,DELETE\n")
    headers = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
    http_code = (
        f'r = requests.request(url="{endpoint}", method="{method}", headers={headers})'
    )
    return http_code


def http_auth_template():
    endpoint = input("enter endpoint url, ex. https://yourapi.com/stuff\n")
    method = input("enter method: GET,PATCH,POST,DELETE\n")
    headers = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
    http_code = (
        f'r = requests.request(url="{endpoint}", method="{method}", headers={headers}, auth=("password","any text"))'
    )
    return http_code


def analyze_csv(csv):
    """
    Display basic csv attributes.
    csv name:   'data.csv'
    encoding:   'utf-8'
    rows:       10
    columns:    5
    duplicates: 20
    """
    # Use chardet to read csv encoding.
    with open(csv, "rb") as fhand:
        csv_type = chardet.detect(fhand.read())
        encoding = csv_type["encoding"]
    # Use pandas to get row + column stats.
    df = pd.read_csv(csv, encoding=encoding)
    rows = df.index.size
    dupe_rows = rows - df.drop_duplicates().index.size
    summary = f"""
    csv name:   '{csv}'
    encoding:   '{encoding}'
    rows:       {rows}
    columns:    {len(df.columns)}
    duplicates: {dupe_rows}
    """
    return summary


def fix_mojibake(text):
    """Use ftfy library as mojibake fixing function.
    ftfy docs: https://ftfy.readthedocs.io/en/latest/"""
    clean_text = ftfy.fix_text(text)
    return clean_text


def csv_merge(csvs):
    """
    Accepts: list of csvs
    read to dfs --> single dataframe
    Returns: pandas dataframe
    """
    dfs = [pd.read_csv(csv) for csv in csvs]
    df = pd.concat(dfs)
    return df


def csv_split(csv):
    """Use chardet to read csv encoding,
    then split the dataframe w/ numpy.array_split().
    
    docs:
    https://chardet.readthedocs.io/en/latest/_modules/chardet.html#detect
    https://numpy.org/doc/stable/reference/generated/numpy.array_split.html
    """
    with open(csv, "rb") as fhand:
        csv_type = chardet.detect(fhand.read())
        encoding = csv_type["encoding"]
    df = pd.read_csv(csv, encoding=encoding)
    split_num = int(input("enter desired number of splits\n"))
    dfs = np.array_split(df, split_num)
    return dfs


def merge_tabs(xl_name):
    """Merge each tab of data in xl into single dataframe."""
    xl = pd.ExcelFile(xl_name)
    dfs = [xl.parse(sheet) for sheet in xl.sheet_names]
    all_tabs_df = pd.concat(dfs)
    return all_tabs_df


def word_cloud(df):
    """
    Generate a word cloud from dataframe.
    Docs: http://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html#wordcloud.WordCloud
    """
    text = df.fillna("").to_string()
    wordcloud = WordCloud().generate(text)
    return wordcloud
