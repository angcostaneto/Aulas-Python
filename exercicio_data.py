from datetime import datetime

# Exercicio proposto
# eu digito 2 datas em formato americano ano-mes-dia,
# e ele me retorna a data no formato brasileiro ( dia-mes-ano ) e a disntância em dias das 2 datas.

def diferencaData(data):
    data = datetime.strptime(data, '%Y-%m-%d')
    return abs((datetime.now() - data).days)

def formataData(data):
    return datetime.strftime(datetime.strptime(data, '%Y-%m-%d'), '%d/%m/%Y')

data_inicial = '2021-03-29'
print('Diferença atual: ', diferencaData(data_inicial))
print('Data formatada: ', formataData(data_inicial))