import datetime
import re

def now_in_jst():
    jst = datetime.timezone(datetime.timedelta(hours=9))
    return datetime.datetime.now(jst).isoformat(timespec='seconds')

find = r'(^\| *\d* *\| *\S* *\| *http\S* *\| *)active( *\|) *\S*( *\|)'
#find = r'(^\| *\d* *\| *\S* *\| *http\S* *\| *)non-active( *\|) *\S*( *\|)'
#str = '| 1 | aws-server-less | https://github.com/osaguild/aws-server-less | non-active | aa |'
str = '| 1 | aws-server-less | https://github.com/osaguild/aws-server-less | active | 2022-03-10T23:51:30+09:00 |'
replace = r'\1non-active\2 ' + now_in_jst() + r'\3'
#replace = r'\1active\2 ' + now_in_jst() + r'\3'
match = re.match(find, str) is not None

print('match:', match)

sub = re.sub(find, replace, str)

print('sub:', sub)