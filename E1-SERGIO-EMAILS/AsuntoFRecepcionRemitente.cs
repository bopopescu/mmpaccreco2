using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace E1_SERGIO_EMAILS
{
    class AsuntoFRecepcionRemitente
    {
        #region atributos
        public string Asunto { get; set; }
        public DateTime FechaRecepcion { get; set; }
        public string Remitente { get; set; }
        #endregion
        #region constructor
        public AsuntoFRecepcionRemitente(string Asunto, DateTime FechaRecepcion, string Remitente)
        {
            this.Asunto = Asunto;
            this.FechaRecepcion = FechaRecepcion;
            this.Remitente = Remitente;
        }
        #endregion
    }
}
