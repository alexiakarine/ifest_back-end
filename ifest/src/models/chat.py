from dataclasses import dataclass, asdict


@dataclass
class Componente:
    valor: str
    tipo: str


@dataclass
class Imagem(Componente):
    legenda: str = ""
    tipo: str = "imagem"


@dataclass
class Texto(Componente):
    tipo: str = "texto"

@dataclass
class Pix(Componente):
    tipo: str = "pix"
    copia_cola: str = ""


@dataclass
class Copiar(Componente):
    texto_copiar: str = ""
    tipo: str = "copiar"


class Mensagem:
    def __init__(self):
        self.componentes = []

    def adicionar_componente(self, componente: Componente):
        self.componentes.append(componente)

    def converter_mensagem(self):
        resposta_lista = []
        for componente in self.componentes:
            resposta_lista.append(asdict(componente))
        return resposta_lista
