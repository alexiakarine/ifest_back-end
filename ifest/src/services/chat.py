from models.chat import Mensagem, Texto, Copiar, Imagem, Pix
from services import produtoService, pixService, usuarioService
from datetime import datetime, date

carrinho = {
    "email": "",
    "nome": "",
    "cidade": "",
    "convidados": 0,
    "data": "",
    "carrinho": [],
    "total": 0
}


def respostas(recebido, contexto, n, email) -> tuple:
    recebido = recebido.lower()

    contextos = {
        "geral": geral,
        "decoracao": decoracao,
        "buffet": buffet,
        "local": local,
        "menu": menu
    }

    if recebido == "voltar" and contexto not in ("geral", "menu"):
        contexto = "menu"

    mensagem, contexto, n = contextos[contexto](recebido, n)

    if recebido.isspace() or not recebido:
        mensagem = "Por favor, digite uma mensagem"

    if not mensagem:
        mensagem = "Desculpe, não entendi."

    return mensagem, contexto, n


def geral(recebido, n):

    contexto = "geral"

    mensagem = Mensagem()
    texto = Texto(valor="Você está no iFest! Qual o seu e-mail?")
    mensagem.adicionar_componente(texto)

    if (n == 1):
        carrinho["email"] = recebido

        usuario = usuarioService.buscarUsuario(recebido)

        if usuario == 0:
            texto.valor = "Usuário não encontrado. Insira um e-mail válido."
            n = 0
        else:
            carrinho["nome"] = usuario
            texto.valor = f"{usuario}, a festa é para quantos convidados?"

    if (n == 2):
        try:
            int(recebido)
            carrinho["convidados"] = recebido
            texto.valor = "Em qual data será o evento?"
        except:
            texto.valor = "Por favor, insira um número válido"
            n = 1

    if (n == 3):
        try:
            data = datetime.strptime(recebido, '%d/%m/%Y')
            if data.date() <= date.today():
                texto.valor = "Por favor, insira uma data posterior a hoje"
                n = 2
            else:
                carrinho["data"] = recebido
                texto.valor = "Em qual cidade será realizado o evento?"
        except ValueError:
            texto.valor = "Por favor, insira uma data válida no formato dd/mm/aaaa"
            n = 2

    if (n == 4):
        carrinho["cidade"] = recebido
        texto.valor = "Qual você deseja escolher:"
        mensagem.adicionar_componente(Copiar(valor="Decoração", texto_copiar="Decoração"))
        mensagem.adicionar_componente(Copiar(valor="Local", texto_copiar="Local"))
        mensagem.adicionar_componente(Copiar(valor="Buffet", texto_copiar="Buffet"))

        contexto = "menu"

    n += 1
    return mensagem, contexto, n


def menu(recebido, n):
    n = 0
    mensagem = Mensagem()
    contexto = "menu"

    if any(item in ("decoração", "decoracao") for item in recebido.split(",")):
        recomendacoes = produtoService.recomendacao(str(carrinho['email']))
        contexto = "decoracao"
        mensagem.adicionar_componente(Texto(valor="Esses são os produtos que recomendamos para você:"))
        for indice, linha in recomendacoes.iterrows():
            imagem = Imagem(valor=linha['link'], legenda=linha['nome_decoracao'])
            mensagem.adicionar_componente(imagem)

    if any(item in ("buffet", "comida") for item in recebido.split(",")):
        mensagem.adicionar_componente(Texto(valor="Qual você deseja contratar (valores por convidado):"))
        mensagem.adicionar_componente(Copiar(valor="1.Arroz e guarnição(R$8,00)", texto_copiar="Arroz e guarnição"))
        mensagem.adicionar_componente(Copiar(valor="2.Bolo de corte(R$10,00)", texto_copiar="Bolo de corte"))
        mensagem.adicionar_componente(Copiar(valor="3.Churrasco(R$40,00)", texto_copiar="Churrasco"))
        mensagem.adicionar_componente(Copiar(valor="4.Massas(R$80,00)", texto_copiar="Massas"))
        mensagem.adicionar_componente(Copiar(valor="5.Bebidas(R$15,00)", texto_copiar="Bebidas"))
        mensagem.adicionar_componente(Copiar(valor="0.Voltar", texto_copiar="Voltar"))

        contexto = "buffet"

    if any(item in ("local", "lugar") for item in recebido.split(",")):
        mensagem.adicionar_componente(Texto(valor="Qual você deseja contratar:"))
        mensagem.adicionar_componente(Copiar(valor="1.Chacára(R$1.000,00)", texto_copiar="Chacára"))
        mensagem.adicionar_componente(Copiar(valor="2.Salão(R$800,00)", texto_copiar="Salão"))
        mensagem.adicionar_componente(Copiar(valor="0.Voltar", texto_copiar="Voltar"))

        contexto = "local"

    if recebido == "voltar":
        mensagem.adicionar_componente(Texto(valor="Para finalizar a compra digite FINALIZAR ou escolha uma das opções:"))
        mensagem.adicionar_componente(Copiar(valor="FINALIZAR", texto_copiar="FINALIZAR"))
        mensagem.adicionar_componente(Copiar(valor="Decoração", texto_copiar="Decoração"))
        mensagem.adicionar_componente(Copiar(valor="Local", texto_copiar="Local"))
        mensagem.adicionar_componente(Copiar(valor="Buffet", texto_copiar="Buffet"))

        #mensagem = "Para finalizar a compra digite FINALIZAR " \
         #          "\nEntre Decoração, Local e Buffet, qual você deseja escolher?"

    if recebido == "finalizar":
        contexto = "finalizar"

    return mensagem, contexto, n


def decoracao(recebido, n):
    mensagem = Mensagem()
    contexto = "decoracao"

    recebido = recebido.replace(', ', ',')

    if recebido == "finalizar":
        contexto = "finalizar"
        return mensagem, contexto, n

    mensagem.adicionar_componente(Texto(valor="Item adicionado com sucesso!"))
    mensagem.adicionar_componente(Copiar(valor="Digite VOLTAR para continuar comprando.", texto_copiar="VOLTAR"))
    mensagem.adicionar_componente(Copiar(valor="Digite FINALIZAR para encerrar a compra.", texto_copiar="FINALIZAR"))

    #mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou" \
    #          " FINALIZAR para encerrar a compra"
    carrinho["carrinho"].append({"item": str(produtoService.finalizar_carrinho(str(recebido))), "preco": 180.00})
    carrinho["total"] += 180.00

    return mensagem, contexto, n


def buffet(recebido, n):
    mensagem = Mensagem()
    contexto = "buffet"
    qtd_convidados = int(carrinho["convidados"])

    if recebido:

        recebido = recebido.replace(', ', ',')

        if any(item in ("arroz e guarnição", "guarnição", "arroz") for item in recebido.split(",")):
            preco = 8 * qtd_convidados
            carrinho["carrinho"].append({"item": "Arroz e Guranição", "preco": preco})
            carrinho["total"] += preco

        if any(item in ("bolo de corte", "bolo") for item in recebido.split(",")):
            preco = 10 * qtd_convidados
            carrinho["carrinho"].append({"item": "Bolo de Corte", "preco": preco})
            carrinho["total"] += preco

        if any(item in ("churrasco", "carne") for item in recebido.split(",")):
            preco = 40 * qtd_convidados
            carrinho["carrinho"].append({"item": "Churrasco", "preco": preco})
            carrinho["total"] += preco

        if any(item in ("massas", "massa") for item in recebido.split(",")):
            preco = 80 * qtd_convidados
            carrinho["carrinho"].append({"item": "Massas", "preco": preco})
            carrinho["total"] += preco

        if any(item in ("bebidas", "bebida") for item in recebido.split(",")):
            preco = 15 * qtd_convidados
            carrinho["carrinho"].append({"item": "Bebidas", "preco": preco})
            carrinho["total"] += preco

        if recebido == "finalizar":
            contexto = "finalizar"

        mensagem.adicionar_componente(Texto(valor="Item adicionado com sucesso!"))
        mensagem.adicionar_componente(Copiar(valor="Digite VOLTAR para continuar comprando.", texto_copiar="VOLTAR"))
        mensagem.adicionar_componente(Copiar(valor="Digite FINALIZAR para encerrar a compra.", texto_copiar="FINALIZAR"))

    return mensagem, contexto, n


def local(recebido, n):
    mensagem = Mensagem()
    contexto = "local"

    recebido = recebido.replace(', ', ',')

    if recebido:

        if any(item in ("salão", "salao", "1") for item in recebido.split(",")):
            carrinho["carrinho"].append({"item": "Salão", "preco": 800.00})
            carrinho["total"] += 800.00

        if any(item in ("chácara", "chacara", "2") for item in recebido.split(",")):
            carrinho["carrinho"].append({"item": "Chácara", "preco": 1000.00})
            carrinho["total"] += 1000.00

        if recebido == "finalizar":
            contexto = "finalizar"

        mensagem.adicionar_componente(Texto(valor="Item adicionado com sucesso!"))
        mensagem.adicionar_componente(Copiar(valor="Digite VOLTAR para continuar comprando.", texto_copiar="VOLTAR"))
        mensagem.adicionar_componente(Copiar(valor="Digite FINALIZAR para encerrar a compra.", texto_copiar="FINALIZAR"))

    return mensagem, contexto, n


def finalizar():
    mensagem = Mensagem()
    c = produtoService.adicionarCarrinho(carrinho)
    if c:
        nome = c["nome"]
        convidados = c["convidados"]
        data = c["data"]
        cidade = c["cidade"]

        mensagem.adicionar_componente(Texto(valor=f"{nome}, dados da sua festa: "))
        mensagem.adicionar_componente(Texto(valor=f"Quantidade de Convidados: {convidados} "))
        mensagem.adicionar_componente(Texto(valor=f"Data: {data} "))
        mensagem.adicionar_componente(Texto(valor=f"Cidade: {cidade} "))
        mensagem.adicionar_componente(Texto(valor=f"Produtos Adquiridos:"))

        for produto in c["carrinho"]:
            mensagem.adicionar_componente(Texto(valor=f"{produto['item']} - R${produto['preco']}"))

        mensagem.adicionar_componente(Texto(valor=f"Valor total: {c['total']} "))
        mensagem.adicionar_componente(Texto(valor="Agradecemos por realizar sua festa conosco!"))
        pix = pixService.gerarPix()
        mensagem.adicionar_componente(Pix(valor=pix['qr_code_image'], copia_cola=pix['payload']))

        return mensagem

    else:
        return 'Não foi possível finalizar a compra.'


def termo_lgpd_chat(email: str):

    usuario = usuarioService.buscarUsuario(email)

    if usuario == 0:
        return False
    else:
        carrinho["nome"] = usuario
        return usuarioService.termo_lgpd(email=email)

