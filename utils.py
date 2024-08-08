import json
from urllib.parse import unquote_plus

def extract_route(request):
    return request.split()[1].lstrip('/')

def read_file(filepath):
    with open(filepath, 'rb') as file:
        return file.read()
    
def load_data(filepath):
    filepath = 'data/' + filepath
    with open(filepath, 'r') as file:
        return json.load(file)
    
def load_template(filepath):
    filepath = 'templates/' + filepath
    with open(filepath, 'r') as file:
        return file.read()
    
def nova_nota(params):
    filepath = 'data/notes.json' 
    with open(filepath, 'r') as file:
        notes = json.load(file)
    notes.append(params)
    with open(filepath, 'w') as file:
        json.dump(notes, file)

def cria_params(request):
    corpo = request.split('\n\n')[1]
    params = {}
    for chave_valor in corpo.split('&'):
        chave, valor = chave_valor.split('=')
        params[chave] = unquote_plus(valor)
    return params

def build_response(body='', code='200', reason='OK', headers=''):
    if len(headers) > 0:
        return 'HTTP/1.1 {c} {r}\n{h}\n\n{b}'.format(c=code, r=reason, h=headers, b=body).encode()
    else:
        return 'HTTP/1.1 {c} {r}\n\n{b}'.format(c=code, r=reason, h=headers, b=body).encode()