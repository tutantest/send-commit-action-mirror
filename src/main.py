import os
import shutil
from github import Github
import requests
#import github_token
#from github_token import GITHUB_TOKEN, user, password


def main():
  #Get inputs values
  #commits-author
  #source-repo-pull-request
  #target-repo
  author = os.environ["INPUT_COMMITS-AUTHOR"]
  source_repo = os.environ["INPUT_SOURCE-REPO-PULL-REQUEST"]
  target_repo = os.environ["INPUT_TARGET-REPO"]
  usuario = os.environ["INPUT_USUARIO"]
  pull_number = os.environ["INPUT_PULL-NUMBER"]
  print(pull_number)
  print("USUARIO: " + usuario)
  result = ""
  result = author + " - " + source_repo + " - " + target_repo
  print("Conectando al repo...")

  # using an access token
  g = Github(usuario)
    
  #g = Github(GITHUB_TOKEN)
  #g = Github(usuario, user_pass)
  user = g.get_user()
  repositories = user.get_repos()
  repos_id_list=[]
  for repo in repositories:
    print("repo: " + repo.name)
    repos_id_list.append(repo.id)
  
  #Get repositories for an organization
  #org = g1.get_organization('tutantest')
  #repos = org.get_repos()
  #repos_id_list=[]
  #for repo in repos:
  #  print("repo: " + repo.id)
  #  repos_id_list.append(repo.id)
  
  #github = Github(login_or_token="TOKEN")
  source_repository = user.get_repo(source_repo)
  target_repository = user.get_repo(target_repo)
  #print("Cargando pull requests...")
  #pulls = repo.get_pulls()
  #pulls_numbers_list = []
  #for pull in pulls:
  #  print("current pull: " + str(pull.number))
  #  pulls_numbers_list.append(pull.number)

  #print("Pulls: " + str(len(pulls_numbers_list)))
  #print("Recuperando Pull Request " + str(pull_number))
  #pr = repo.get_pull(pull_number)
  pr = source_repository.get_pull(int(pull_number))
  

  commits = pr.get_commits()

  #for commit in commits:
  #  files = commit.files
  #  for file in files:
  #      filename = file.filename
  #      print("nombre fichero: " + filename)
  #      content = source_repository.get_contents(filename, ref=commit.sha).decoded_content
  #      print("contenido: " + content.decode("utf-8"))
  #      print(content)
  #  print("No hay más ficheros")
  #print("No hay más commits")
  url = f'https://api.github.com/repos/{source_repository.full_name}/pulls/{pull_number}/files'
  print(url)
  headers = {'Authorization':f'token {usuario}'}
  print(headers)
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    archivos = response.json()
    if archivos:
      print("Archivos de la Pull Request:")
      for archivo in archivos:
        ruta_completa = archivo['filename']
        print("Ruta Completa: ", ruta_completa)
        print("Estado fichero: ", archivo['status'])
    else:
      print("No hay archivos modificados en la Pull Request")
  else:
    print("Error al obtener los archivos de la Pull Request: ", response.status_code)

  if len(archivos) != 0:
    os.mkdir("../../commits_files")
    for archivo in archivos:
        nombre_archivo = ""
        ruta_completa = archivo['filename']
        if "/" in ruta_completa:
          trozos = ruta_completa.split("/")
          nombre_archivo = trozos[-1]
        else:
          nombre_archivo = ruta_completa
        shutil.copy(ruta_completa,"../../commits_files/"+nombre_archivo)

  #Set the output value
  print(f"::set-output name=result::{result}")

if __name__ == "__main__":
  main()
