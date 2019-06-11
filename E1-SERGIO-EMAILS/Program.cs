using Microsoft.Office.Interop.Outlook;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Outlook = Microsoft.Office.Interop.Outlook;
using Excel = Microsoft.Office.Interop.Excel;
using System.Runtime.InteropServices;

namespace E1_SERGIO_EMAILS
{
    class Program
    {
        static void Main(string[] args)
        {
            //obtener los emails de outlook
            Outlook.Application app = new Outlook.Application();
            Application outlookApplication = new Application();
            NameSpace outlookNamespace = outlookApplication.GetNamespace("MAPI");
            MAPIFolder inboxFolder = outlookNamespace.GetDefaultFolder(OlDefaultFolders.olFolderInbox);
            Items mailItems = inboxFolder.Items;           
       
            //AsuntoFRecepcionRemitente es una clase cuyos atributos son asunto, fecha, remitente
            List<AsuntoFRecepcionRemitente> emailsFiltrados = new List<AsuntoFRecepcionRemitente>();
            AsuntoFRecepcionRemitente emailFiltrado = null;
            foreach (MailItem mailItem in mailItems)
            {
                //    Console.WriteLine(mailItem.ReceivedTime);
                if (mailItem.Body.Contains("saludo"))
                {
                    emailFiltrado = new AsuntoFRecepcionRemitente(mailItem.Subject, mailItem.ReceivedTime, mailItem.SenderName);
                    emailsFiltrados.Add(emailFiltrado);
                }
            }
            //es para comprobar los emails
            
            int i = 0;

            foreach (AsuntoFRecepcionRemitente correo in emailsFiltrados)
            {
                Console.WriteLine("Mensaje " + i);
                Console.WriteLine(correo.Asunto);
                Console.WriteLine(correo.FechaRecepcion.ToString("dd-MM-yyyy"));
                Console.WriteLine(correo.Remitente);
                Console.WriteLine();
                i++;
            }
            
            var xlApp = new Excel.Application();
            //esto abre, no crea
            //    Excel.Workbook xlWorkbook = xlApp.Workbooks.Open("C:\\ejercicio1\\ejemplo1.xlsx");
            //la hoja de trabajo tiene únicamente una pestaña
            Excel.Workbook xlWorkbook = xlApp.Workbooks.Add(1);
            //selecciona pestaña 1 del libro de trabajo
            Excel.Worksheet xlWorkSheet = xlWorkbook.Sheets[1];
            //uso todo el rango
            Excel.Range xlRange = xlWorkSheet.UsedRange;
            //lo hago visible
            xlApp.Visible = true;
            //introduzco datos
            xlWorkSheet.Cells[1, 1] = "ASUNTO";
            xlWorkSheet.Cells[1, 2] = "FECHA RECEPCIÓN";
            xlWorkSheet.Cells[1, 3] = "REMITENTE";
            //int j;
            int numCorreos = emailsFiltrados.Count;
            i=2;
            foreach  (AsuntoFRecepcionRemitente correo in emailsFiltrados)
            {
                xlWorkSheet.Cells[i, 1] = correo.Asunto;
                xlWorkSheet.Cells[i, 2] = correo.FechaRecepcion;
                xlWorkSheet.Cells[i, 3] = correo.Remitente;
                i++;
            }
            /*
            for (i = 2; i <= 5; i++)
            {
                for (j = 1; j <= 3; j++)
                {
                    if (j == 1)
                    {
                        Console.Write("\r\n");
                    }
                    if (xlRange.Cells[i, j] != null && xlRange.Cells[i, j] != null)
                    {
                        xlWorkSheet.Cells[i, j] = emailsFiltrados.;
                    }
                }
            }
            */
            //guarda la hoja de trabajo en la siguiente ruta
        //    string horaActual = ("" + DateTime.Now.ToLocalTime()).Replace('/','X');
        //    horaActual = horaActual.Replace(' ', 'X');

        //    String ruta= "C:\\ejercicio1\\ejemplo1"+horaActual+".xlsx";
        //    xlWorkbook.SaveAs("C:\\ejercicio1\\ejemplo1" + horaActual + ".xlsx");
        xlWorkbook.SaveAs("C:\\ejercicio1\\ejemplo1.xlsx");
            xlWorkbook.Close(0);
            xlApp.Quit();
            Marshal.ReleaseComObject(xlWorkSheet);
            Marshal.ReleaseComObject(xlWorkbook);
            Marshal.ReleaseComObject(xlApp);

        }
    }
}
