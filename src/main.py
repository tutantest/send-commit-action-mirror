import os

#Get inputs values
#commits-author
#source-repo-pull-request
#target-repo
author = os.environ["INPUT_COMMITS-AUTHOR"]
source_repo = os.environ["INPUT_SOURCE-REPO-PULL-REQUEST"]
target_repo = os.environ["INPUT_TARGET-REPO"]

result = ""
result = author + " - " + source_repo + " - " + target_repo

#Set the output value
print(f"::set-output name=result::{result}")
