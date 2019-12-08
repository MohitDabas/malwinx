import re
def parseHTMLFileOnce():
    fileData=open('winapiindex.html').read()
    regex = r">.*<\/a>"
    matches = re.finditer(regex, fileData)
    functionList=[]
    for matchNum, match in enumerate(matches, start=1):
          functionNameFromHTMLFile=match.group()
          functionNameFromHTMLFile=functionNameFromHTMLFile.replace(':sample code</a>','')
          functionNameFromHTMLFile=functionNameFromHTMLFile.replace('>','')
          functionList.append(functionNameFromHTMLFile+'\n')
    dumpFunctionToFile(functionList)      


def dumpFunctionToFile(functionList):
    fileWrite=open('functionList.txt','w')
    fileWrite.writelines(functionList)
    fileWrite.close()


def getFunctionName(functionToSearch):
 
     functionPattern='.*'+functionToSearch+'.*'
      
     matches = re.finditer(re.compile(functionPattern).pattern, open('functionList.txt').read(), re.IGNORECASE)
     functionList=[]
     for matchNum, match in enumerate(matches, start=1):
        functionList.append(match.group())
     if functionToSearch in functionList:   
          return functionToSearch
     

print (getFunctionName('LoadLibrary'))



          
#parseHTMLFileOnce()   