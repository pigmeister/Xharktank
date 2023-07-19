import requests
import json
import os

# added commment

response = requests.post(
    url=f'https://api.github.com/repos/pigmeister/Xharktank/issues/{os.environ["PR_NUMBER"]}/comments',
    headers={
        'Authorization': 'Bearer {token}'.format(token=os.environ['ACCESS_TOKEN']),
        'Content-Type': 'application/vnd.github+json'
    },
    data=json.dumps({
        'body': 'This is a test comment to {env}'.format(env=os.environ['ENV'])
    })
)