class Retta:
    def __init__(self, tipo = "param", p1 = None, p2 = None, p3 = None, p4 = None):
        if (tipo == "param"):
            self.__a = p1
            self.__b = p2
            self.__c = p3
            self.__punti = []
            self.__m = p4


    def __init__(self, x, y, x_2, y_2, punto1, punto2):
        self.__x = x
        self.__y = y
        self.__x_2 = x_2
        self.__y_2 = y_2
        self.__p1 = punto1
        self.__p2 = punto2

    punto1 = (self.__x, self.__y)
    punto2 = (self.__x_2, self.__y_2)

    def get_retta(self):
        if punto1 != 0 and punto2 != 0:
            return f'Equazione della retta: y=, {((self.__y_2-self.__y)/(self.__x_2-self.__x)*self.__x)}x + {(((self.__y_2-self.__y)/(self.__x_2-self.__x)*self.__x)-self.__y)}'

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c

    def eqImplicita(self):
        if self.__b==0:
            return f"{self.__a}x+{self.__c}=0"
        elif self.__c==0:
            return f"{self.__a}x+{self.__b}y=0"
        elif self.__a==0:
            return f"{self.__b}y+{self.__c}=0"

    def eqEsplicita(self):
        if self.__b==0:
            return f"x={-self.__c}/{self.__a}"
        elif self.__c==0:
            return f"y={-self.__a}x/{self.__b}"
        elif self.__a==0:
            return f"y={-self.__c}/{self.__b}"
        else:
            return f"y={-self.__a/self.__b}x+{-self.__c/self.__b}"
        
    def trovaY(self, x, y):
        y = ((-self.__a*x)/self.__b + (-self.__c/self.__b))
        return y

    def punti(self, N, M, x):
        self.__N = N
        self.__M = M

        for self.__N in range(self.__M, x):
            tupla = (x, (-self.__a * x) / self.__b + (-self.__c / self.__b))
            x = x+1
            self.__punti.append(tupla)
            return f"Coordinate dei punti: {self.__punti}"

    def m(self):
        if self.__b == 0:
            return f"La retta è parallela all'asse delle ordinate"
        elif self.__a == 0:
            return f"La retta è perpendicolare all'asse delle ascisse"
        else:
            self.__m = -self.__a/self.__b
            return self.__m

    def intersezione(self, a1, b1, c1, m1, intersezione = None):
        self.__a1 = a1
        self.__b1 = b1
        self.__c1 = c1

        if m1 == self.__m:
            return f"Le due rette non hanno un punto di intersezione perché sono parallele"

        elif m1 == self.__m and (-self.__c/self.__b) == (-self.__c1/self.__b1):
            return f"Le due rette sono coincidenti e quindi hanno tutti i punti in comune"

        else:
            intersezione = (((-self.__c / self.__b)+(self.__c1 / self.__b1))/((-self.__b / self.__a)+(self.__b1 / self.__a1)), ((-self.__b / self.__c)+(self.__b1 / self.__c1))/((-self.__b / self.__a)+(self.__b1 / self.__a1)))
            return intersezione
