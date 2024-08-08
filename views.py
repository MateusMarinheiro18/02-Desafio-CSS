from utils import load_data, load_template, nova_nota, cria_params, build_response

def atualiza_notas():
    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        request = request.replace('\r', '')  # Remove caracteres indesejados
        corpo = request.split('\n\n')[1]
        params = cria_params(request)
        nova_nota(params)
        body = atualiza_notas()
        return build_response(body=body, code='303', reason='See Other', headers='Location: /')

    # O RESTO DO CÓDIGO DA FUNÇÃO index CONTINUA DAQUI PARA BAIXO
    
    elif request.startswith('GET'):
        body = atualiza_notas()
        return build_response(body=body)

teste = "POST / HTTP/1.1\nHost: 0.0.0.0:8080\nConnection: keep-alive\nContent-Length: 25\nCache-Control: max-age=0\nUpgrade-Insecure-Requests: 1\nOrigin: http://0.0.0.0:8080\nContent-Type: application/x-www-form-urlencoded\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\nReferer: http://0.0.0.0:8080/\nAccept-Encoding: gzip, deflate\nAccept-Language: en-US,en;q=0.9,pt;q=0.8\n\ntitulo=Sorvete+de+banana&detalhes=Coloque+uma+banana+no+congelador+e+espere.+Pronto%21+1%2B1%3D2."

#print(cria_params(teste))