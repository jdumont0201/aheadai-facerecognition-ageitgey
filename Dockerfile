FROM python:3.7.1-alpine3.8
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev cmake gcc g++
RUN pip3 install japronto
EXPOSE 3012


RUN pip3 install face_recognition
RUN mkdir /ai && mkdir /ai/src && mkdir /ai/auth
ADD src  /ai/src
CMD chmod -r 777 /ai/src

CMD ["python3","/ai/src/scripts/main.py"]
