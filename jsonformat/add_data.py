import json
import datetime

# now datetime
def now_in_jst():
    jst = datetime.timezone(datetime.timedelta(hours=9))
    return datetime.datetime.now(jst).isoformat(timespec='seconds')

# open file
with open('./jsonformat/data/data.json') as rf:
    df = json.load(rf)

df.update(now=now_in_jst())

with open('./jsonformat/data/data.json', mode='w') as wf:
    wf.write(json.dumps(df))

