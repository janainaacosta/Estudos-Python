'''
filtro de dados em list comprehension 
'''
import pprint

def p(a):
    pprint.pprint(a, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'preco': 10, },
    {'nome': 'p2', 'preco': 20, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] > 20 and produto['preco'] * 1.05) > 10
]

print(*novos_produtos, sep='\n')