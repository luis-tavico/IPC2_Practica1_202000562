import os

class Graficar:
    def __init__(self):
        self.grafico = ""
        self.txt = ''

    def graficarOrdenes(self, ordenes):
        self.grafico += """digraph ORDENES {
            graph [label="ORDENES"
                labelloc="t"
                fontname="Helvetica,Arial,sans-serif"]\n"""
        self.graficar(ordenes)
        pdf = 'ordenes.pdf'
        os.system("dot.exe -Tpdf " + self.txt + " -o " + pdf)
        os.system(pdf)

    def graficarOrdenTerminada(self, ordenes):
        self.grafico += """digraph ORDEN {
            graph [label="ORDEN TERMINADA"
                labelloc="t"
                fontname="Helvetica,Arial,sans-serif"]\n"""
        self.graficar(ordenes)
        pdf = 'ordenTerminada.pdf'
        os.system("dot.exe -Tpdf " + self.txt + " -o " + pdf)
        os.system(pdf)

    def graficar(self, ordenes):
        posicion = 0
        self.grafico += """            node [fontname="Helvetica,Arial,sans-serif"
                shape=record
                style=filled
                fillcolor=gray95]
            edge [dir="none"]\n"""
        while ordenes != None:
            posicion += 1
            self.grafico += '            posicion'+str(posicion)+'[label = <{<b>Orden '+str(ordenes.dato.getNumero())
            self.grafico += '</b> |Nombre: '+ordenes.dato.getNombreCliente()+'  <br align="center"/>Cantidad de shucos: '+str(ordenes.dato.getCantidadShucos())+'  <br align="center"/>|'
            shucosDelCliente = ordenes.dato.getShucos().values()
            while shucosDelCliente != None:
                self.grafico +='Ingrediente: '+shucosDelCliente.dato.getIngrediente()+' ~ Tiempo: '+shucosDelCliente.dato.getTiempo()+'<br align="center"/>'
                shucosDelCliente = shucosDelCliente.siguiente
            self.grafico += '|Tiempo Total: '+ordenes.dato.getTiempoTotal()+'<br align="center"/>'
            self.grafico += 'Tiempo en cola: '+ordenes.dato.getTiempoEnCola()+' minutos<br align="center"/>'
            self.grafico += '}>]\n'
            ordenes = ordenes.siguiente
        self.grafico += "posicion1"
        numero = 1
        while posicion > 1:
            numero += 1 
            self.grafico += "->posicion"+str(numero)
            posicion -= 1
        self.grafico += '\n}'
        self.txt = 'ordenes.txt'
        with open(self.txt, 'w') as grafica:
            grafica.write(self.grafico)