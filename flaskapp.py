from flask import Flask,render_template,request,jsonify
from werkzeug.utils import secure_filename
import os,pefileparser,win32apiparser,itwordparser
import requests
app=Flask(__name__)

uploadFolder='./templates/uploads'
ALLOWED_EXTENSIONS=set(['exe','dll'])
app.config['UPLOAD_FOLDER']=uploadFolder


def allowedFile(fileName):
    return '.' in fileName and fileName.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload_exe',methods=['GET','POST'])
def uploadEXE():
    fileUploaded=request.files['resume']
    if fileUploaded.filename=='':
        return jsonify('{"error":"No file Selected"}')   
    if fileUploaded and allowedFile(fileUploaded.filename):
        fileUploaded.save(os.path.join(app.config['UPLOAD_FOLDER'],fileUploaded.filename))
        #return jsonify('{"Success":"File Uploaded"}')
        exportData=pefileparser.parsePEFile(app.config['UPLOAD_FOLDER']+'/'+fileUploaded.filename)
        return jsonify(exportData)
    return 'Nothing Happens' 

@app.route('/get_function_desc',methods=['GET','POST']) 
def getFuncDesc():
    data = request.form.to_dict(flat=False)
    print (request.args.get("func"))
    errorDescript,funcDetail=win32apiparser.getFunctionDetail(request.args.get("func"))
    print(funcDetail)
    try:
     if 'Error Found:' in errorDescript:
        return  jsonify({"error":errorDescript});   
     else:   
      return jsonify(funcDetail) 
    except:
        return jsonify({"error":"No Data Return"})

@app.route('/get_itfunc',methods=['GET','POST'])
def getITFuncDesc():
    funcName=request.args.get("func")
    if funcName.endswith('A'):
        funcName=funcName.replace(funcName[len(funcName)-1],'')
    if funcName.endswith('W'):
        funcName=funcName.replace(funcName[len(funcName)-1],'')    
    function=itwordparser.getFunctionName(funcName)
    functionListData={}
    functionListData['funcName']=function
    functionListData['funcLink']="http://www.it-word.net/api/capi/en-us/"+function+'.html'
    r=requests.get("http://www.it-word.net/api/capi/en-us/"+function+'.html')
    print (r.content)    
    return r.content



if __name__=='__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
