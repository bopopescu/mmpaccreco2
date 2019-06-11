using ExcelDataReader;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace edr_linq
{
    class Program
    {
        static void Main(string[] args)
        {
            string ruta = @"C:\edr-linq\Metabot SAP Template Configuration v10.1.xlsm";
            string clave = "FI";
            string PATTERNS = "Patterns";
            var stream = File.Open(ruta, FileMode.Open, FileAccess.Read);
            //    Console.WriteLine(stream.Name);
            var chorizo = ExcelReaderFactory.CreateReader(stream).AsDataSet().Tables["Patterns"].AsEnumerable();

            var filasChorizo = from chori in chorizo
                               where chori.ItemArray[0].ToString().Contains("FI")
                               select chori;

            var reader = ExcelReaderFactory.CreateReader(stream);
            var dataset = reader.AsDataSet();
            var dtPatterns = reader.AsDataSet().Tables["Patterns"];
            var filasDTPatterns = dtPatterns.Rows;

            var dtpe = dtPatterns.AsEnumerable();
            var res = from f in dtpe
                      where f.ItemArray[0].ToString().Contains("FI")
                      select f;
            //ASÍ FUNCIONA, PERO HAY QUE HACERLO CON DATATABLE
            var filas3 = from DataRow f in filasDTPatterns
                         where f.ItemArray[0].ToString().Contains("FI")
                         select f;
            /*
            var columnasDTPatterns = dtPatterns.Columns;
            int i, j;
            /*
            for(i=0; i<filasDTPatterns.Count; i++)
            {
                Console.WriteLine(filasDTPatterns[i][0]);
            }
            */
            /*
            for (i = 0; i < dtPatterns.Rows.Count; i++)
            {
                Console.WriteLine(dtPatterns.Rows[i].ItemArray.ToString());
            }
            */
            /*
            for (i = 0, j = 0; i < filasDTPatterns.Count; i++)
            {
                for (j = 0; j < columnasDTPatterns.Count; j++)
                {
                    if (filasDTPatterns[i][0].ToString().Contains("FI"))
                    {
                        Console.Write(filasDTPatterns[i][j]+" ");
                    }
                }
                Console.WriteLine();
            }
            */
            /*
            for (i = 1, j = 0; i < filasDTPatterns.Count; i++)
            {
                if (filasDTPatterns[i][0].ToString().Contains("FI"))
                {
                    //    Console.WriteLine(filasDTPatterns[i]);
                    j++;
                }
            }
            Console.WriteLine(j);
            var filasFI = filasDTPatterns.AsEnumerable();
            filasFI = from fil in filasFI
                       //   where fil.ToString().Contains("FI")
                          select fil;
            Console.WriteLine();
            
            //    Console.WriteLine(filasDTPatterns[i][0].ToString().Contains("FI"));

            /*
            Console.WriteLine("---------------");
            for(j=0; j<columnasDTPatterns.Count; j++)
            {
                Console.Write(filasDTPatterns[6][j] + " ");
            }
            */
            Console.WriteLine();
            Console.WriteLine("---------------");
            //for(i=0; i<filasDTPatterns.Count; i++)
            //{
            //    Console.WriteLine(columnasDTPatterns[0].ColumnName);
            //}
            /*
            int i;
            int j;
            int numTablas = dataset.Tables.Count;
            Console.WriteLine(numTablas);
            for(i=0, j=0; i < numTablas; i++, j++)
            {
                //    if(dataset.Tables[i].TableName.Contains(clave))
                //    Console.WriteLine(dataset.Tables[i].TableName);   //así muestro las pestañas
                //    Console.WriteLine(dataset.Tables[i].TableName.Contains(clave));
                if (dataset.Tables[i].TableName.Equals(PATTERNS))
                {
                    break;
                }
            }
            Console.WriteLine("j: " + j);   //j vale 2 ~~ es la tercera pestaña
            var sheetPatterns = dataset.Tables[2];
            int pCols = sheetPatterns.Columns.Count;
            int pRows = sheetPatterns.Rows.Count;
            Console.WriteLine(pCols);
            Console.WriteLine(pRows);

            Console.WriteLine(sheetPatterns.TableName); //Patterns
            var aux = sheetPatterns.Rows;
            var aux7 = aux[7];
            Console.WriteLine(aux7);
            var longitudAux7 = aux7.ItemArray.Length;
            var auxaux7 = aux7.ItemArray;
            Console.WriteLine("Excel - Columna 8 de Patterns");
            for(i=0; i<longitudAux7; i++)
            {
                Console.Write(auxaux7[i]+" ");
            }
            */
            Console.WriteLine();
            /*
            for(i=0, j=0; i<pRows; i++)
            {
                for(j=0; j<pCols; j++)
                {
                    Console.Write(sheetPatterns.Rows[i][j]+" ");
                }
                Console.WriteLine("\n");
            //    if (sheetPatterns.Rows[i].ItemArray.Contains("FI"))
            //    {
            //        j++;
            //    }
            }
            //Console.WriteLine("número de FI -> " + j);
        //    for(i=0; i<pRows; i++)
        //    {
        //        Console.WriteLine(sheetPatters.Columns[i].ColumnName[i]);
        //    }
        */
            /*
            var datatable = dataset.Tables[0];
            Console.WriteLine(dataset.Tables[0].Rows.Count);
            Console.WriteLine(datatable.Rows.Count);
            for (i = 0; i < dataset.Tables[0].Rows.Count; i++)
            {
                //    Console.WriteLine(dataset.Tables[0].Rows);
                Console.WriteLine(datatable.Rows[i][7]);
            }
            Console.WriteLine(dataset.Tables[0].Columns.Count);
            reader.Close();
            //var res = from r in result
            //          select new { result.Tables[0].ToString() };
            */
            Console.ReadKey();
        }
    }
}
