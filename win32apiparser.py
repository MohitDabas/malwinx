import json

def getFunctionDetail(funcName):
  if funcName.endswith("A"):
    funcName=funcName.replace(funcName[len(funcName)-1],'')
  if funcName.endswith("W"):
    funcName=funcName.replace(funcName[len(funcName)-1],'')  
  funcDetails={}
  print (funcName)
  with open('collectiveWINAPIJson.json') as fp:
      jsonData=json.load(fp)
  try:
    for index in range(0,len(jsonData)):
      
     if jsonData[index]['name']==funcName: 
      funcDetails['name']=jsonData[index]['name']
      funcDetails['description']=jsonData[index]['arguments'][0]['description']
      funcDetails['category']=jsonData[index]['name']
      funcDetails['arguments']=jsonData[index]['arguments']
      funcDetails['return_value']=jsonData[index]['return_value']
      funcDetails['return_type']=jsonData[index]['return_type']
      funcDetails['remarks']=jsonData[index]['remarks']
      funcDetails['header']=jsonData[index]['header']
      return "No Error",funcDetails
  except Exception as e:
      print (str(e))
      return "Error Found:"+str(e),[]
     


