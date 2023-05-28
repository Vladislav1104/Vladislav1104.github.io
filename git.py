from git import repo

repo = repo('')
repo.git.add('file.txt')
repo.index.commit('commit message')
origin = master
repo.remote(name='origin')
origin.push()