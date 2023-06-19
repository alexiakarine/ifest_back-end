# API - IFEST :sparkles:
Projeto Integrador do 6º Semestre de Banco de Dados - FATEC Profº Jessen Vidal, São José dos Campos

<hr/>

# :trophy: Equipe

<center>
  <table align="center">
    <tr>
      <td align="center" width="20%">
          <p><b>Product Owner</b></p>
          <p><img src="https://github.com/EquipeFatec/api-5/blob/main/images/Time/Guilherme.jpg" width="70%"/></p>
          <p><a href="https://github.com/guitambau">Guilherme <br/> Perfeito </a>
          <a href="https://www.linkedin.com/in/guilherme-perfeito-a76729168/"><img src="https://github.com/EquipeFatec/api/blob/main/images/linkedin.png"/></a></p>
        </td>
      <td align="center" width="20%">
          <p><b>Scrum Master</b></p>
          <p><img src="https://github.com/EquipeFatec/api-5/blob/main/images/Time/Isabella.jpg" width="70%"/></p>
          <p><a href="https://github.com/isarps">Isabella Rosa <br/> Peixoto Segundo </a>
          <a href="https://www.linkedin.com/in/isabellarps/"><img src="https://github.com/EquipeFatec/api/blob/main/images/linkedin.png"/></a></p>
      </td>
      <td align="center" width="20%">
          <p><b>Dev</b></p>
          <p><img src="https://github.com/EquipeFatec/api-5/blob/main/images/Time/Alexia.jpg" width="70%"/></p>
          <p><a href="https://github.com/alexiakarine">Alexia Karine Silva <br/> dos Santos </a>
          <a href="https://www.linkedin.com/in/alexia-karine-silva-5b0a79116/"><img src="https://github.com/EquipeFatec/api/blob/main/images/linkedin.png"/></a></p>
      </td>
    </tr>
  </table>
 </center>
<hr/>

# :office: Cliente
O projeto deste semestre é interno da FATEC. <br/>

<hr/>

# :information_source: Sobre o Projeto
Criado pela equipe _Sanja Valley_, este projeto visa desenvolver um Chatbot de vendas, onde o usuário poderá pesquisar produtos, cadastrar-se, efetuar compras e verificar o histórico da conversa. O Chatbot também irá realizar uma análise dos dados para fornecer recomendações de produtos aos usuários. <br/>

<hr/>

# :dart: Storycards
| ID |	  COMO   | DESEJO                           |	PARA                                                                               | PRIORIDADE |
| -- | :-------: | -------------------------------- | ---------------------------------------------------------------------------------- | :--------: |
| 01 | Comprador | Acessar Chat                     | Realizar as pesquisas para minha compra                                            |     1      |
| 02 | Comprador | Acrescentar produtos no carrinho |	Inserir itens que desejo comprar                                                   |     2      |
| 03 | Comprador | Exibir itens do carrinho         |	Verificar os itens que selecionei para compra                                      |   	 3      |
| 04 | Comprador | Deletar produtos do carrinho     |	Cancelar itens que desejo remover da compra	                                       |     4      |
| 05 | Comprador | Finalizar Compra                 | Fechar os itens do carrinho de produtos e prosseguir para as etapas de finalização |     5      |
| 06 | Comprador | Acrescentar endereço             | Receber os itens adquiridos no endereço desejado                                   |     6      |
| 07 | Comprador | Gerar QR Code de Pagamento       | Realizar o pagamento da compra                                                     |     7      |
| 08 | Comprador | Receber recomendações de Produtos|	Verificar itens recomendados para minha compra de acordo com o Segmento            |     8      |
| 09 | Sistema   | Salvar Histórico de Conversa     | Disponibilizar log com as conversas realizadas com os usuários                     |     9      |
| 10 | Comprador | Visualizar Imagem do Produto     | Conferir os produtos que quero inserir no carrinho                                 |     10     |

<hr/>

# :computer: Tecnologias Utilizadas
![image](https://user-images.githubusercontent.com/49652498/233513323-bca84a4a-aa89-4b6e-98a1-be8ce02ed1ed.png)<br/>

<hr/>

# :open_file_folder: Entregas

<hr/>

## Sprint 1
#### :gear:	Backend
- Fluxo inicial de conversa Python
- Exibição do menu de compra
- Adicionar e alterar carrinho de compras
- Cálculo total da compra
- Integração com MongoDB
#### :package: Banco de Dados
- Adicionar e alterar carrinho de compras no banco de dados MongoDB
#### :bulb: <a href="https://github.com/Sanja-Valley/ChatterBotIfest/blob/main/Apresenta%C3%A7%C3%B5es/Sprint-1.pdf">Apresentação</a>

<hr/>

## Sprint 2
#### :gear:	Backend
- Arquitetura com Flask
- Endpoints de envio/recepção de mensagens
- Integração com finalização de compra
- QR Code Pix
- Exibição de Imagens
#### :iphone:	Frontend
- Arquitetura inicial com VueJS
- Tela do chat
- Exibição de mensagens
- Integração de mensagens com Backend
- Exibição de Imagens
#### :package: Banco de Dados
- Finalização de compras no MongoDB
- Criação do Banco Relacional PostgreSQL
#### :bulb: <a href="https://github.com/Sanja-Valley/ChatterBotIfest/blob/main/Apresenta%C3%A7%C3%B5es/Sprint-2.pdf">Apresentação</a>

<hr/>

## Sprint 3
#### :gear:	Backend
- Salvar Histórico de Conversas
- Regras de Validação e Verificação dos Inputs
- Integração SQL
- Associação de compra a e-mail
- Recomendações
#### :iphone:	Frontend
- Exibição QR Code e Pix Copia e Cola
- Aceitação de Termos LGPD
#### :package: Banco de Dados
- Salvar Logs de Conversa MongoDB
#### :bulb: <a href="https://github.com/Sanja-Valley/ChatterBotIfest/blob/main/Apresenta%C3%A7%C3%B5es/Sprint-3.pdf">Apresentação</a>

<hr/>

## Sprint 4
#### :gear:	Backend
- Login
- Melhoria de Recomendações
- Notificação de Termos LGPD
- Notificação de Alertas de Dados LGPD
- Exibição de Imagens
- Correção de Bugs
#### :iphone:	Frontend
- Login
- Aceitação de Termos LGPD
- Exibição de Imagens
- Correção de Bugs
#### :package: Banco de Dados
- Salvar Aceitação de Termo LGPD
#### :bulb: <a href="https://github.com/Sanja-Valley/ChatterBotIfest/blob/main/Apresenta%C3%A7%C3%B5es/Sprint-4.pdf">Apresentação</a>
