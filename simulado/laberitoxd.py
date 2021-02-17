import turtle

PARTE_DEL_CAMINO = 'O'
INTENTADO = '.'
OBSTACULO = '+'
CAJELLON_SIN_SALIDA = '-'

class Laberinto:
    def __init__(self,nombreArchivoLaberinto):
        filasEnLaberinto = 0
        columnasEnLaberinto = 0
        self.listaLaberinto = []
        archivoLaberinto = open(nombreArchivoLaberinto,'r')
        filasEnLaberinto = 0
        for linea in archivoLaberinto:
            listaFila = []
            columna = 0
            for caracter in linea[:-1]:
                listaFila.append(caracter)
                if caracter == 'S':
                    self.filaInicio = filasEnLaberinto
                    self.columnaInicio = columna
                columna = columna + 1
            filasEnLaberinto = filasEnLaberinto + 1
            self.listaLaberinto.append(listaFila)
            columnasEnLaberinto = len(listaFila)

        self.filasEnLaberinto = filasEnLaberinto
        self.columnasEnLaberinto = columnasEnLaberinto
        self.xTranslate = -columnasEnLaberinto/2
        self.yTranslate = filasEnLaberinto/2
        self.t = turtle.Turtle()
        self.t.shape('square')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(columnasEnLaberinto-1)/2-.5,-(filasEnLaberinto-1)/2-.5,(columnasEnLaberinto-1)/2+.5,(filasEnLaberinto-1)/2+.5)

    def dibujarLaberinto(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.filasEnLaberinto):
            for x in range(self.columnasEnLaberinto):
                if self.listaLaberinto[y][x] == OBSTACULO:
                    self.dibujarCajaCentrada(x+self.xTranslate,-y+self.yTranslate,'lightblue')
        self.t.color('black')
        self.t.fillcolor('yellow')
        self.wn.update()
        self.wn.tracer(1)

    def dibujarCajaCentrada(self,x,y,color):
        self.t.up()
        self.t.goto(x-.5,y-.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def moverTortuga(self,x,y):
        if self.listaLaberinto[y][x] == OBSTACULO:
            pass
        else:
            self.t.up()
            self.t.setheading(self.t.towards(x+self.xTranslate,-y+self.yTranslate))
            self.t.goto(x+self.xTranslate,-y+self.yTranslate)

    def tirarMigaDePan(self,color):
        self.t.dot(10,color)

    def actualizarPosicion(self,fila,columna,val=None):
        if val:
            self.listaLaberinto[fila][columna] = val
        self.moverTortuga(columna,fila)

        if val == PARTE_DEL_CAMINO:
            color = 'green'
        elif val == OBSTACULO:
            color = 'red'
        elif val == INTENTADO:
            color = 'black'
        elif val == CAJELLON_SIN_SALIDA:
            color = 'red'
        else:
            color = None

        if color:
            self.tirarMigaDePan(color)

    def esSalida(self,fila,columna):
        return (fila == 0 or
                fila == self.filasEnLaberinto-1 or
                columna == 0 or
                columna == self.columnasEnLaberinto-1 )

    def __getitem__(self,indice):
        return self.listaLaberinto[indice]


def buscarDesde(laberinto, filaInicio, columnaInicio):
    laberinto.actualizarPosicion(filaInicio, columnaInicio)
   #  Verificar casos base:
   #  1. Hemos tropezado con un obstáculo, devolver False
    if laberinto[filaInicio][columnaInicio] == OBSTACULO :
        return False
    #  2. Hemos encontrado un cuadrado que ya ha sido explorado
    if laberinto[filaInicio][columnaInicio] == INTENTADO:
        return False
    # 3. Éxito, un borde exterior no ocupado por un obstáculo
    if laberinto.esSalida(filaInicio,columnaInicio):
        laberinto.actualizarPosicion(filaInicio, columnaInicio, PARTE_DEL_CAMINO)
        return True
    laberinto.actualizarPosicion(filaInicio, columnaInicio, INTENTADO)

    # De lo contrario, use cortocircuitos lógicos para probar cada
    # dirección a su vez (si fuera necesario)
    encontrado = buscarDesde(laberinto, filaInicio-1, columnaInicio) or \
            buscarDesde(laberinto, filaInicio+1, columnaInicio) or \
            buscarDesde(laberinto, filaInicio, columnaInicio-1) or \
            buscarDesde(laberinto, filaInicio, columnaInicio+1)

    return encontrado

miLaberinto = Laberinto('laberinto2.txt')
miLaberinto.dibujarLaberinto()
miLaberinto.actualizarPosicion(miLaberinto.filaInicio,miLaberinto.columnaInicio)

buscarDesde(miLaberinto, miLaberinto.filaInicio, miLaberinto.columnaInicio)
