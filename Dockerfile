FROM python:3.7.1-alpine3.8


RUN pip3 install tornado
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
RUN apk add cmake
RUN apk add gcc g++
ENV LIBRARY_PATH=/lib:/usr/lib
RUN pip3 install pillow
RUN pip3 install face_recognition
RUN mkdir /ai && mkdir /ai/src && mkdir /ai/auth
ADD src  /ai/src

EXPOSE 3012



CMD chmod -r 777 /ai/src
CMD ["python","/ai/src/scripts/main.py"]
