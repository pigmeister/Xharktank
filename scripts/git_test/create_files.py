import os

path = '../dest/dump'

query1lines = ['hello', 'me', 'nipun']
query1 = '\n'.join(query1lines)

query2lines = ['sup', 'is', 'me']
query2 = '\n'.join(query2lines)

file1dir = path + 'file1'
os.mkdir(file1dir)
file1path = path + 'file1/' + 'file3.sql'
with open(file1path, 'w+') as file1:
    file1.write(query1)

file2dir = path + 'file2'
os.mkdir(file2dir)
file2path = path + 'file2/' + 'file4.sql'
with open(file2path, 'w+') as file2:
    file2.write(query2)