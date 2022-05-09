FROM python:3.9.10-slim
COPY . /app
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean
WORKDIR app
RUN pip install --user -r requirements.txt
ENTRYPOINT uvicorn main:app --reload --host 0.0.0.0 --port 8080