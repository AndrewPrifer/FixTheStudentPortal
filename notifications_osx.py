# Dependencies:
# https://github.com/julienXX/terminal-notifier
# https://github.com/kennethreitz/requests

import requests
import os

# Configuration constants:
MESSAGE_LIMIT = 5
SENDERS = {'FWN'}  # LET, FMW, FEB, FRG, GGW, FRW, UCG, GMW, FWN, etc...
USER_NAME = 'your_user_name'
PASS = 'your_password'


def notify(title, subtitle, message, open):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    o = '-open {!r}'.format(open)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s, o])))

TARGET = 'https://student.portal.rug.nl:443/infonet/studenten/portal/needtoknow!json'

payload = {'option': 'credential',
           'target': TARGET,
           'Ecom_User_ID': USER_NAME,
           'Ecom_Password': PASS}

login = requests.post('https://signon.rug.nl/nidp/idff/sso?sid=0', payload)
notifs = requests.get(TARGET, cookies=login.cookies, allow_redirects=True).json()['Items']

open('needtoknow.log', 'a').close()

with open('needtoknow.log', 'r') as f:
    tag = f.readline()

new = []
for notif in notifs:
    if notif['ETag'] != tag:
        new.append(notif)
    else:
        break

if len(new) != 0:
    tag = new[0]['ETag']

with open('needtoknow.log', 'w') as f:
    f.write(tag)

for notif in reversed(list(filter(lambda x: x['Sender'] in SENDERS, new))[0:MESSAGE_LIMIT]):
    notify('Student Portal - Need to Know', 'From ' + notif['Sender'], notif['Title'], notif['Source'])
