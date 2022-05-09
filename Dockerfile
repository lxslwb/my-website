FROM python:3.9-buster
WORKDIR /app
COPY . .
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
&& pip install -r requirements.txt
