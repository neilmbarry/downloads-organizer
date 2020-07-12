#! /usr/bin/env python3
#! Downloads_Organizer.py - A program that organizes your downloads folder
# by grouping file types in to subfolders

import os, shutil

def folderOrganize(path):

    absPath = os.path.abspath(path)
    documents = ('.pdf','.docx','.xls','.xlsb','.xlsx','.txt')
    videos = ('.mkv','.mp4','.webm','.avi')
    pics = ('.png','.jpg','.jpeg')
    compressed = ('.zip')
    programs = ('.dmg')
    python = ('.py')
    music = ('.mp3','.wav')
    
    for folders,subfolders,items in os.walk(path):

        for item in items:
             
            if item.lower().endswith(documents):
                if not os.path.exists(os.path.join(path,'Documents')):
                    os.mkdir(os.path.join(path,'Documents'))
                print(f'Copying {item}...')  
                shutil.move(os.path.join(folders,item),os.path.join(absPath,'Documents',item))
                   
            elif item.lower().endswith(videos):
                
                if not os.path.exists(os.path.join(path,'Videos')):
                    os.mkdir(os.path.join(path,'Videos'))
                print(f'Copying {item}...') 
                shutil.move(os.path.join(folders,item),os.path.join(absPath,'Videos',item))
                   
            elif item.lower().endswith(pics):
                if not os.path.exists(os.path.join(path,'Pictures')):
                    os.mkdir(os.path.join(path,'Pictures'))
                print(f'Copying {item}...') 
                shutil.move(os.path.join(folders,item),os.path.join(absPath,'Pictures',item))
                   
            elif item.lower().endswith(compressed):
                if not os.path.exists(os.path.join(path,'Compressed')):
                    os.mkdir(os.path.join(path,'Compressed'))
                print(f'Copying {item}...') 
                shutil.move(os.path.join(folders,item),os.path.join(absPath,'Compressed',item))

            elif item.lower().endswith(programs):
                if not os.path.exists(os.path.join(path,'Programs')):
                    os.mkdir(os.path.join(path,'Programs'))
                print(f'Copying {item}...') 
                shutil.move(os.path.join(folders,item),os.path.join(absPath,'Programs',item))

            elif item.lower().endswith(python):
                if not os.path.exists(os.path.join(path,'Python Scripts')):
                    os.mkdir(os.path.join(path,'Python Scripts'))
                print(f'Copying {item}...') 
                shutil.move(os.path.join(folders,item),os.path.join(absPath,'Python Scripts',item))

            elif item.lower().endswith(music):
                if not os.path.exists(os.path.join(path,'Music')):
                    os.mkdir(os.path.join(path,'Music'))
                print(f'Copying {item}...') 
                shutil.move(os.path.join(folders,item),os.path.join(absPath,'Music',item))

            else:
                if not os.path.exists(os.path.join(path,'Misc.')):
                    os.mkdir(os.path.join(path,'Misc.'))
                print(f'Copying {item}...') 
                shutil.move(os.path.join(folders,item),os.path.join(absPath,'Misc.',item))

      #  for subfolder in subfolders:
       #     if len(os.listdir(os.path.join(folders,subfolder)))==0:
       #         print('Removing empty folders...')
        #        os.rmdir(os.path.join(folders,subfolder))

     
