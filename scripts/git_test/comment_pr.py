import requests
import json
import os

VIEW_ONLY = os.environ.get('VIEW_ONLY', False)
NOOP_MODE = os.environ.get('NOOP_MODE', True)

def create_pr(message: str) -> requests.Response:
    response = requests.post(
        url=f'https://api.github.com/repos/pigmeister/Xharktank/issues/{os.environ["PR_NUMBER"]}/comments',
        headers={
            'Authorization': 'Bearer {token}'.format(token=os.environ['ACCESS_TOKEN']),
            'Content-Type': 'application/vnd.github+json'
        },
        data=json.dumps({
            'body': message
        })
    )

    return response

data = {
    "tbl_tbl1": [
        "CREATE TABLE tbl1;",
        "COMMENT;"
    ],
    "vw_tbl1": [
        "CREATE view tbl1;"
    ]
}

message = 'Previewing commands:\n```' if NOOP_MODE else 'Deploying commands:\n```'

for key, value in data:
    if VIEW_ONLY and 'vw_' not in key:
        continue
    message += '\n' + value.join('\n') + '\n'

create_pr(message=message)