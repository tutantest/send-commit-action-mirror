import os
from github import Github

def main():
  #Get inputs values
  #commits-author
  #source-repo-pull-request
  #target-repo
  author = os.environ["INPUT_COMMITS-AUTHOR"]
  source_repo = os.environ["INPUT_SOURCE-REPO-PULL-REQUEST"]
  target_repo = os.environ["INPUT_TARGET-REPO"]
  result = ""
  result = author + " - " + source_repo + " - " + target_repo
  print("Conectando al repo...")
  github = Github(login_or_token="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")
  repo = github.get_repo("tutantest/back-mirror-test", lazy=False)
  print("Cargando pull requests...")
  pulls = repo.get_pulls()
  pulls_numbers_list = []
  for pull in pulls:
    print("current pull: " + pull.number)
    pulls_numbers_list.append(pull.number)
    
  pr = repo.get_pull(pulls_numbers_list[0])

  commits = pr.get_commits()

  for commit in commits:
    files = commit.files
    for file in files:
        filename = file.filename
        print("nombre fichero: " + filename)
        contents = repo.get_contents(filename, ref=commit.sha).decoded_content
        print("contenido: " + contents)

  #Set the output value
  print(f"::set-output name=result::{result}")

if __name__ == "__main__":
  main()
