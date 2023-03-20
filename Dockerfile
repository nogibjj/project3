# FROM public.ecr.aws/lambda/python:3.8
# WORKDIR /tool
# COPY . /tool
# RUN pip install -r requirements.txt
# EXPOSE 8080
# CMD [ "fastapi-app.py" ]
# ENTRYPOINT [ "python" ]
FROM public.ecr.aws/lambda/python:3.8
WORKDIR /tool/app
COPY . /tool
RUN pip install -r ./../requirements.txt
EXPOSE 8080
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]