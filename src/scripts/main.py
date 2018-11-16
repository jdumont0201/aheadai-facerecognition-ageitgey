


import face_recognition
import sys
########################################
#PARAMS
########################################
PORT =3012


########################################
#JOB
########################################
def run(input):
    print("run"+input["mode"])
    if input["mode"]=='LOCAL':
        imagePath=input["path"]
        image=face_recognition.load_image_file(imagePath)
    elif input["mode"]=='MULTIPART':
        imagePath=input["path"]
        image=face_recognition.load_image_file(imagePath)
    elif input["mode"]=='UPLOAD':
        image=input["file"]
    face_locations=face_recognition.face_locations(image)
    print(face_locations)
    return  face_locations
    
    
    
    
    
    
    
########################################
#SERVER
########################################
 
import simplejson
import tornado.ioloop
import tornado.web

import os, uuid
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        print("POST")
        contentType=self.request.headers.get('Content-Type')
        print(self.request.headers)
        print("Content-Type: "+contentType)

        contentLength=self.request.headers.get('Content-Length')
        print("Content-Length: "+contentLength)
        files=self.request.files;
        
        print("Nb files:"+str(len(files)))
        if(contentType[:19]=="multipart/form-data"):
            fileinfo=files["file"][0]

            fname = fileinfo['filename']
            print("File name"+fname)
            extn = os.path.splitext(fname)[1]
            cname = str(uuid.uuid4()) + extn
            print("File name"+cname)
            fh = open("./data" + cname, 'wb')
            fh.write(fileinfo['body'])
            input={'path':"./data/input/" + cname,'mode':'MULTIPART'}
        elif(contentType=="application/json"):
            data = tornado.escape.json_decode(self.request.body)
            print(data)
            input={'path':data["path"],'mode':'LOCAL'}
        else:
            print("Unknown Content-Type")
        #else:
         #   input={'mode':'UPLOAD','file':self.request.body}
        output=run(input)
        js=simplejson.dumps(output)
        self.set_header('Content-Type', 'application/json; charset="utf-8"')
        self.write("{\"result\":"+js+"}")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
