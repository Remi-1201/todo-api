FROM python:3.7-alpine                       
# ベースとするDockerイメージを指定
LABEL architecture="Your Name"               
# 構築担当者をラベル付け

ENV PYTHONUNBUFFERD 1                        
# リアルタイムでログを見れるように環境変数を指定

COPY ./requirements.txt /requirements.txt    
# ローカルのrequirements.txtをコンテナにコピー
RUN pip install -r /requirements.txt         
# requirements.txtに従ってパッケージを一括でインストール

RUN mkdir /django-api                        
# Djangoプロジェクトを置くディレクトリをコンテナ上に作成
WORKDIR /django-api                          
# コンテナ上の作業ディレクトリを変更
COPY ./django-api /django-api                
# ローカルのdjango-apiディレクトリをコンテナにコピー

RUN adduser -D user                          
# アプリケーションを実行するためのユーザを作成する
USER user                                    
# ユーザをrootから変更