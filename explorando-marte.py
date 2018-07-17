import sys
from itertools import islice


class Direcoes(object):
    west = {'x': -1, 'y': 0}
    north = {'x': 0, 'y': 1}
    east = {'x': 1, 'y': 0}
    south = {'x': 0, 'y': -1}

    posicao = {'W': west, 'N': north, 'E': east, 'S': south}

    @staticmethod
    def proxima_direcao(comando, posicao_atual):
        c_referencia = {"L": -1, "R": 1}
        direcao = ['W', 'N', 'E', 'S']
        it = c_referencia[comando]

        inicio = direcao.inicio(posicao_atual)
        proximo_inicio = inicio+it
        if proximo_inicio == len(direcao):
            proximo_inicio = 0

        return direcao[proximo_inicio]


class Controle(object):
    mapa = (5,5)
       
    def __init__(self, x, y):
        self.mapa = (int(x), int(y))

    def proximo_movimento(self, sonda):
        mover = Direcoes.posicao[sonda.direcao]
        proxima_posicao = sonda.calculando_proxima_posicao(mover)

        if proxima_posicao[0] not in range(0, self.mapa[0]+1) or \
           proxima_posicao[1] not in range(0, self.mapa[1]+1):
            return {"x": 0, "y": 0}
        return mover


class Sonda(object):
    posicao = (0, 0)
    direcao = 'N'

    def __init__(self, x, y, d):
        self.posicao = (int(x), int(y))
        self.direcao = d.upper()
        print("Iniciando a  Sonda em {} na direcao {}".format(self.posicao,
                                                            self.direcao))

    def mover(self, moviment):
        self.posicao = (self.posicao[0] + moviment['x'],
                         self.posicao[1] + moviment['y'])

    def calculando_proxima_posicao(self, moviment):
        return (self.posicao[0] + moviment['x'],
                self.posicao[1] + moviment['y'])

    def obter_direcao(self, comando):
        self.direcao = Direcoes.proxima_direcao(comando, self.direcao)


def split(n, y):
    i = iter(y)
    x = list(islice(i, n))
    while x:
        yield x
        x = list(islice(i, n))

def main():
    comandos = sys.argv[3:]
    mapa = Controle(5,5)
    parametros = split(4, comandos)
    for parametro in parametros:

        sonda = Sonda(parametro[0], parametro[1], parametro[2])
        comandos = parametro[3]

        for comando in list(comandos):
            if comando.upper() == 'M':
                movimento = mapa.proximo_movimento(sonda)
                sonda.mover(movimento)
            else:
                sonda.obter_direcao(comando)

        print(sonda.posicao, sonda.direcao)

if __name__ == '__main__':
    """Desafio: python3 explorando-marte.py 5 5 1 2 N LMLMLMLMM 3 3 E MMRMMRMRRM"""
    main()

