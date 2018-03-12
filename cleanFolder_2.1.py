# The application copies files to current folders.
# Purpose - folder download
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.INFO) #turn off logging
import os
import shutil
import pprint

# print('pwd>>>', os.getcwd())
#
def viewsFile():
    listsDic = {}
    for x in os.listdir(): #list elements in folder
        if os.path.isfile(x): #only files
            format = (x[x.rfind('.'):len(x)]) # We find .txt or .pdf
            if (len(format)>1): # i avoided example :  _text_nname.....
                listsDic.setdefault(format, 0)  #Add new name in dictionary
                listsDic[format] = listsDic[format] + 1 #counts
                logging.debug(listsDic)
    return listsDic

def createFolders(listsDic):
    for k,v in listsDic.items():
        print (k[1:],v)
        if int(v)>0: #if v more than 0 will create folder
            if not os.path.exists(k[1:]): #if not exist folder about name file without '.'
                logging.debug(os.mkdir(k[1:]))
                os.mkdir(k[1:]) #create folder


createFolders(viewsFile())

def copyFiles(listsDic):
    for x in os.listdir():
        format = (x[x.rfind('.'):len(x)]) #format is name ( for '.' to end string )
        # print (x.endswith(format[1:]))
        if os.path.exists(format[1:]) and x !='cleanFolder_2.1.py': #We cannot delete clenFolder_2.1
            #if os.path.getsize(x) > 1024000 : You will make zip files  more then 1 GB

            try:
                #todo it
                ## You will make zip files  more then 1 GB
                ## zipfile.ZipFile('test.zip', 'r')
                shutil.move(x, format[1:]) #copy file
                print ('Copy:',x,' into ',format[1:])
            except:
                print ('File of name',x,' exist in ',format[1:])
                xSize = (os.path.getsize(x))
                os.chdir(format[1:])
                if xSize == os.path.getsize(x): #verification files - size
                    print ('Files have same size.')
                    # os.unlink(file_path)  You can delete file if files are same
                else:
                    print('!x' * 50)
                    print ('Files have not size.')
                    print (x)
                    #todo it
                    #If Program copy file about same name and diffrent getsize, The Program will have to copy the file with a different name.
                    print('!x' * 50)
                os.chdir("../")
                # Files are the same.

copyFiles(viewsFile())

