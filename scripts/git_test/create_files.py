import os

path = '../dest/dump'

query1lines = ['hello', 'me', 'nipun']
query1 = '\n'.join(query1lines)

query2lines = ['sup', 'is', 'me']
query2 = '\n'.join(query2lines)

file1dir = path + 'file1'
if not os.path.isdir(file1dir):
    os.mkdir(file1dir)
file1path = path + 'file1/' + 'file5.sql'
with open(file1path, 'w+') as file1:
    file1.write(query1)

file2dir = path + 'file2'
if not os.path.isdir(file2dir):
    os.mkdir(file2dir)
file2path = path + 'file2/' + 'file6.sql'
with open(file2path, 'w+') as file2:
    file2.write(query2)