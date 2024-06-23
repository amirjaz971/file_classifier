from tkinter.filedialog import askdirectory
from tkinter import messagebox
import logging
import os
import shutil

def log_and_move_file(directory,folder_name,file):
    file_path = os.path.join(directory, file)
    folder_path = os.path.join(directory, f'{folder_name}s')        
    logging.info(f'{file}   {folder_name}    {os.path.getsize(file_path)/1024} KB')
    if not os.path.exists(folder_path):
        os.mkdir(directory+f'/{folder_name}s')
    try:
        shutil.move(file_path,folder_path)    
    except Exception as E:
        logging.exception(f'Error:{E}')

def file_classifier(directory):
    f=0
    datas_lst=os.listdir(directory)
    if len(datas_lst)==0:
        logging.error(f'{directory} is empty!')
        messagebox.showerror('Error','The folder is empty!')
        return 0
    logging.info(f'"{directory}" contains: {datas_lst}')
    logging.info('File name   File Type     Size')
    for file in datas_lst:
        if file.endswith('txt'):
            log_and_move_file(directory,'Text file',file) 
            f+=1
        elif file.endswith(('xlsx','xls')):
            log_and_move_file(directory,'Excel file',file)
            f+=1
        elif file.endswith(('docx','doc')):
            log_and_move_file(directory,'Word file',file)
            f+=1
        elif file.endswith('pdf'):
            log_and_move_file(directory,'PDF file',file)
            f+=1
        elif file.endswith(('jpg','jpeg','png')):
            log_and_move_file(directory,'Image file',file)
            f+=1
        elif file.endswith(('.pptx', '.ppt')):
            log_and_move_file(directory, 'Presentation file', file)
            f+=1             
        elif file.endswith(('.db', '.sql', '.mdb')):
            log_and_move_file(directory, 'Database file', file)
            f+=1
        elif file.endswith(('.py', '.js', '.html', '.css', '.java', '.c', '.cpp', '.php')):
            log_and_move_file(directory, 'Script or Code file', file)
            f+=1
        elif file not in ('Text files','Excel files','Word files','PDF files','Image files'
                          ,'Presentation files','Database files','Script or Code files','Other files'):             
            log_and_move_file(directory,'Other file',file)
            f+=1
    return f    

if __name__=='__main__':
    try:
        logging.basicConfig(filename='File_Classifier.log',level=logging.DEBUG,format='%(asctime)s,%(levelname)s,%(message)s',datefmt='%Y/%m/%d %H:%M:%S')
        logging.critical('Start of program')
        directory=askdirectory(title="Please select a folder to classify its files")
        logging.info(f'User has selected "{directory}" as directory')
        actions=file_classifier(directory)
        if actions==0:
            messagebox.showinfo('File classifier','Nothing has been changed')
            logging.info('Nothing has been changed')
        else:
            if actions==1:
                messagebox.showinfo('File classifier','One file has been classified')    
            else:
                messagebox.showinfo('File classifier',f'{actions} files have been classified in total')   
            logging.info(f'Number of files which have been classified: {actions}')     
        logging.critical('End of program')
    except Exception as E:
        logging.exception(f'Error:{E}')