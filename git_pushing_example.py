from git import Repo

repo_dir = 'emotion_reader'
repo = Repo(repo_dir)
file_list = [
    'captured_image.jpg'
]
commit_message = 'Uploads image'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()