
import pefile
#dll_file='F.dll'
def parsePEFile(fileName):
  pe = pefile.PE(fileName)
  exeImportData={}
  print("[*] Listing imported DLLs...")
  for entry in pe.DIRECTORY_ENTRY_IMPORT:
    exeImportData[entry.dll.decode('utf-8')]=[] 
    
    for func in entry.imports:
            tempDict={} 
            tempDict[func.name.decode('utf-8')]=func.address
            #exeImportData[entry.dll.decode('utf-8')].append(func.name.decode('utf-8'))
            #exeImportData[entry.dll.decode('utf-8')].append(func.address)
         
            exeImportData[entry.dll.decode('utf-8')].append(tempDict)
        
  return exeImportData

