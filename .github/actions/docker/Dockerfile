FROM python:3
 
COPY . .

RUN pip3 install PyGithub
RUN pip install github_token
RUN pip install requests
CMD ["python", "./src/main.py"]
