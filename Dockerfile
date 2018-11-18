FROM alpine
# INIT
RUN apk add --no-cache python3 ca-certificates
RUN apk add --no-cache py3-pip cmake g++ gcc build-base python3-dev zlib-dev \
    && pip3 --no-cache install https://github.com/squeaky-pl/japronto/archive/master.zip  \

	&& rm -rf /var/cache/apk/*
EXPOSE 8080

#SCRIPT
RUN apk add --no-cache  jpeg-dev
RUN pip3 install face_recognition
RUN mkdir /ai && mkdir /ai/src && mkdir /ai/auth
ADD src  /ai/src
CMD chmod -r 777 /ai/src

#START SERVER
CMD ["python3","/ai/src/scripts/main.py"]
