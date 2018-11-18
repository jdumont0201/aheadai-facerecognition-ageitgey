


import face_recognition
import sys
########################################
#PARAMS
########################################
PORT =8080


########################################
#JOB
########################################
def runTask(input):
    print("runTask")
    imagePath=input["path"]
    image=face_recognition.load_image_file(imagePath)
    face_locations=face_recognition.face_locations(image)
    return  face_locations
    
    
    
    
    
    
    
########################################
#SERVER
########################################
 
import simplejson
from japronto import Application
import os, uuid


def run(request):
    print("POST /run")
    print(request)
    print(request.headers)
    contentType=request.headers.get('Content-Type')
    print("Content-Type: "+contentType)
    contentLength=request.headers.get('Content-Length')
    files=request.files;
    
    print("Nb files:"+str(len(files)))
    if(contentType[:19]=="multipart/form-data"):
        fileinfo=files["file"]
        fname = fileinfo.name
        print("FILE_NAME : "+fname)
        extn = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + extn
        print("FILE_UNIQUE_NAME : "+cname)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        saveFilePath = dir_path+"/../data/input/" + cname
        print("SAVE_FILE_PATH",saveFilePath)
        fh = open(saveFilePath, 'wb')
        fh.write(fileinfo.body)
        input={'path':saveFilePath,'mode':'MULTIPART'}
        output=runTask(input)
        js=simplejson.dumps(output)
        result={"success":"true","result":js}
        print(result)
        return request.Response(
        mime_type='application/json; charset="utf-8"',
        json=result)
    else:
        print("Unknown Content-Type. Should be multipart/form-data")
        return request.Response(
        mime_type='application/json; charset="utf-8"',
        json={"success:":"false","error":"Wrong Content-Type"})
    
    



#START SERVER
app = Application()
router = app.router
router.add_route('/run', run,'POST')
app.run()