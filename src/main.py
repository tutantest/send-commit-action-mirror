import os

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

  github = Github(token="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")
  repo = github.get_repo("tutantest/back-mirror-test", lazy=False)

  pr = repo.get_pull(1)

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
