# 1.1 Dockerfile の作成

# ベースとするDockerイメージを指定
FROM python:3.7-alpine                       

# 構築担当者をラベル付け
LABEL architecture="Your Name"               

# リアルタイムでログを見れるように環境変数を指定
ENV PYTHONUNBUFFERD 1                        

# ローカルのrequirements.txtをコンテナにコピー
# COPY ./requirements.txt /requirements.txt    

# requirements.txtに従ってパッケージを一括でインストール
# RUN pip install -r /requirements.txt         

# Djangoプロジェクトを置くディレクトリをコンテナ上に作成
RUN mkdir /django-api                        

# コンテナ上の作業ディレクトリを変更
WORKDIR /django-api                          

# ローカルのdjango-apiディレクトリをコンテナにコピー
COPY ./django-api /django-api                

# アプリケーションを実行するためのユーザを作成する
RUN adduser -D user                          

# ユーザをrootから変更
USER user                                    

# Heroku
RUN python3 manage.py collectstatic --noinput
CMD gunicorn --bind 0.0.0.0:$PORT app.wsgi
