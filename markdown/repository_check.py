import csv
import datetime
import markdown
import pandas as pd
import re
import urllib.request


def markdown_to_html(input: str):
    return markdown.markdown(
        input,
        extensions=['markdown.extensions.tables']
    )

def now_in_jst():
    jst = datetime.timezone(datetime.timedelta(hours=9))
    return datetime.datetime.now(jst).isoformat(timespec='seconds')

MD_PATH: str = 'MY_REPOSITORY.md'

with open(MD_PATH, 'r', encoding='utf-8') as f:
    md: str = f.read()

df = pd.read_html(markdown_to_html(md))

repos: list = [
    {
        'url': url,
        'active': None,
        'time': None
    }
    for url in df[0]['url']
]

for repo in repos:
    req = urllib.request.Request(
        repo['url'],
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
        }
    )

    try:
        with urllib.request.urlopen(req) as r:
            repo['active'] = True
    except urllib.error.HTTPError as e:
        repo['active'] = False
    except urllib.error.URLError as e:
        repo['active'] = False
    finally:
        repo['time'] = now_in_jst()

active_repos: list = [
    repo for repo in repos if repo['active'] is True
]

if len(active_repos) > 0:
    for active_repo in active_repos:
        row_find: str = r'(\n\| *\d* *\| *\S* *\| *' + active_repo['url'] + r' *\|) *non-active *(\|) *\S* *(\|)'
        row_replace: str = r'\1 active \2 ' + now_in_jst() + r' \3'
        md = re.sub(row_find, row_replace, md)

non_active_repos: list = [
    repo for repo in repos if repo['active'] is False
]

if len(non_active_repos) > 0:
    for non_active_repo in non_active_repos:
        row_find: str = r'(\n\| *\d* *\| *\S* *\| *' + non_active_repo['url'] + r' *\|) *active *(\|) *\S* *(\|)'
        row_replace: str = r'\1 non-active \2 ' + now_in_jst() + r' \3'
        md = re.sub(row_find, row_replace, md)

with open(MD_PATH, 'w', encoding='utf-8', newline='\n') as f:
    f.write(md)