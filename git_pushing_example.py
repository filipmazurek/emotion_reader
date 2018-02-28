from git import Repo

# Dependencies
# pip install gitpython

repo_dir = 'emotion_reader'  # repository name
repo = Repo("/Users/filipmazurek/Desktop/emotion_reader")  # path to the repository
file_list = ['captured_image.jpg']  # list of files to push
commit_message = 'Uploads image'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()
