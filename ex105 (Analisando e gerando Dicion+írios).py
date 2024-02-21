def notas(*n, sit=False):
    """
    ->Esse programa calcula as notas cadastradas e mostra a situação
    :param n: uma ou mais notas
    :param sit: situação da media das notas
    :return: todas as notas, nota maior, nota menor, media e situção das notas
    """
    r = dict()
    r['notas'] = n
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >=5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r
resp = notas(5.5, 1.5, 10, 7.5, 9,sit=True)
print(resp)
help(notas)