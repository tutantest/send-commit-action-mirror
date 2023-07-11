FROM python:3
 
COPY . .

RUN pip3 install PyGithub
RUN pip install github_token
RUN pip install requests
RUN pip install shutil
CMD ["python", "./src/main.py"]
