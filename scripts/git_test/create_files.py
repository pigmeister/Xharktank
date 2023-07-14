import os
import git
from git import Repo
import json
import requests

repo_path = os.getcwd() + '/.scripts/node-weather-website'

Repo.clone_from(url='git@github.com:pigmeister/node-weather-website.git', to_path=repo_path, branch='test-base')

repo = Repo(path='.scripts/node-weather-website')

repo.git.checkout('test-head')


query1lines = ['hello', 'me', 'nipun']
query1 = '\n'.join(query1lines)

query2lines = ['sup', 'is', 'me']
query2 = '\n'.join(query2lines)

file1dir = '/.scripts/node-weather-website/' + 'file1'
if not os.path.isdir(file1dir):
    os.mkdir(file1dir)
file1path = file1dir + '/file1.sql'
with open(file1path, 'w+') as file1:
    file1.write(query1)

file2dir = '/.scripts/node-weather-website/' + 'file2'
if not os.path.isdir(file2dir):
    os.mkdir(file2dir)
file2path = file2dir + '/file2.sql'
with open(file2path, 'w+') as file2:
    file2.write(query2)


repo.config_writer().set_value("user", "name", "pigmeister-app[bot]").release()
repo.config_writer().set_value("user", "email", "pigmeister-app[bot]@users.noreply.github.com").release()

repo.git.add(repo_path)

repo.git.commit('-m', 'Test commit')

repo.git.push('origin', 'test-head')

response = requests.post(
    url=f'https://api.github.com/repos/pigmeister/node-weather-website/pulls',
    headers={
        'Authorization': 'Bearer %s' % os.environ.get('BRANCH'),
        'Content-Type': 'application/json'
    },
    data=json.dumps({
        'title': os.environ.get('BRANCH'),
        'head': 'test-head',
        'base': 'test-base'
    })
)

print(response.json())