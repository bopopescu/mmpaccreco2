import win32com.client
from Saludo import Saludo 
import pandas as pd
from openpyxl import load_workbook  #no me ha servido
from win32com.client import Dispatch

'''
outlook = win32com.client.Dispatch("Outlook.Application")
mapi = outlook.GetNamespace("MAPI")
your_folder = mapi.Folders['Outlook_Mails'].Folders['Inbox'].Folders['All Mailboxes']
for message in your_folder.Items:
    print(message.Subject)
'''
'''
# get the Namespace / Session object
namespace = outlook.Session
 
# get Inbox Folders' name
inboxfolder = namespace.Folders.Folders('Inbox')
 
# get messages on Inbox folder
messages = inboxfolder.Items
'''
'''
#ASÍ OBTENGO ACCESO A BANDEJA DE ENTRADA DE OUTLOOK
#cuento el número de emails que tengo en bandeja de entrada
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                        # the inbox. You can change that number to reference
                                        # any other folder
messages = inbox.Items
print(len(messages))
'''
'''
#así obtengo las carpetas que existen
for i in range(50):
    try:
        box = outlook.GetDefaultFolder(i)
        name = box.Name
        print(i, name)
    except:
        pass
'''
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items
saludos = []
cont=0

for mensaje in messages:
    #if(mensaje.Body.find("saludo")): 
    #    cont+=1
    #print(type(mensaje.Body))
    if(mensaje.Body.find("saludo")!=-1):
        saludos.append(Saludo(mensaje.Subject, mensaje.CreationTime, mensaje.Sender))
    #    print(mensaje.Subject)
    #    print(mensaje.CreationTime.strftime("%d-%m-%Y\t%H:%M:%S"))   #datetime
    #    print(mensaje.Sender)
#print(cont) #15

#print(len(saludo)
#print("Número de correos con la palabra saludo: ",len(saludos))
#print(saludos[0].asunto)
#print(type(saludos[0].fechaCreacion))   #<class 'pywintypes.datetime'>
#print(type(str(saludos[0].fechaCreacion)))
#print(str(saludos))
'''
for saludo in saludos:
    print(str(saludo))
'''
'''
ESTO LO QUE HACE ES ESCRIBIR CADA OBJETO EN UNA CELDA <---> NECESITO QUE CADA ATRIBUTO VAYA A UNA CELDA
df = pd.DataFrame(saludos)
df.to_excel('saludo.xlsx',sheet_name='Hoja0')
'''
#df = pd.DataFrame(saludos)
##print(df)#
#print(str(saludos))
#ASÍ ESCRIBO CADA ATRIBUTO DEL OBJETO EN UNA CELDA
ruta="C:\\Users\\j.e.garcia.rodriguez\\Desktop\\pyexcel\\saludo2.xlsx"
xlApp = Dispatch("Excel.Application")
xlApp.Visible = 1
xlApp.Workbooks.Add()
#xlApp.ActiveSheet.Cells(1,1).Value = "hola mundo"  #FUNCIONA. HA ESCRITO EN LA PRIMERA CELDA
xlApp.ActiveSheet.Cells(1,1).Value = "ASUNTO";
xlApp.ActiveSheet.Cells(1,2).Value = "FECHA RECEPCIÓN";
xlApp.ActiveSheet.Cells(1,3).Value = "REMITENTE";

i=2;
for saludo in saludos:
    xlApp.ActiveSheet.Cells(i,1).Value=saludo.asunto;
    xlApp.ActiveSheet.Cells(i,2).Value=saludo.fechaCreacion;
    xlApp.ActiveSheet.Cells(i,3).Value=saludo.remitente;
    i+=1;

xlApp.ActiveSheet.SaveAs(ruta)

'''
libro = load_workbook(ruta)
celda = libro.active

for saludo in saludos:
    celda.append(saludo)
    


libro.save(ruta)
'''