import os
import git
from git import Repo

repo_path = os.getcwd() + '/.scripts/node-weather-website'

Repo.clone_from(url='git@github.com:pigmeister/node-weather-website.git', to_path=repo_path, branch='test-base')

repo = Repo(path=repo_path)

new_branch = repo.create_head('test-head')

new_branch.checkout()


query1lines = ['hello', 'me', 'nipun']
query1 = '\n'.join(query1lines)

query2lines = ['sup', 'is', 'me']
query2 = '\n'.join(query2lines)

file1dir = repo_path + 'file1'
if not os.path.isdir(file1dir):
    os.mkdir(file1dir)
file1path = repo_path + 'file1/' + 'file5.sql'
with open(file1path, 'w+') as file1:
    file1.write(query1)

file2dir = repo_path + 'file2'
if not os.path.isdir(file2dir):
    os.mkdir(file2dir)
file2path = repo_path + 'file2/' + 'file6.sql'
with open(file2path, 'w+') as file2:
    file2.write(query2)


repo.git.add(repo_path)

repo.git.commit('-m', 'Test commit')

repo.git.push('origin', 'test-base')