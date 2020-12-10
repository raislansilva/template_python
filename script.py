# -*- coding: utf-8 -*-
import jinja2
import base64
from string import Template
from itertools import groupby

# with open('template.html','r') as html:
#     template = Template(html.read())
#     corpo=[]
#     for nome in nomes:
#         print template.substitute(nome=nome)


template = jinja2.Template(u"""
<html>
<title>Requisições</title>
<p>
{{cat}}
</p>
<ul>
  {% for attr in attrs %}
  <li>{{attr['nome'].decode('utf8')}}</li>
  {% endfor %}
</ul>
</html>""")

servidores = [
    {"nome": "Raislan", "categoria": "TI", "grau": 1},
    {"nome": "Sheila", "categoria": "Direito", "grau": 1},
    {"nome": "Carla", "categoria": "Saúde", "grau": 2},
    {"nome": "Julia", "categoria": "TI", "grau": 1},
    {"nome": "Joao", "categoria": "TI", "grau": 2},
    {"nome": "Maria", "categoria": "Direito", "grau": 1},
    {"nome": "Joana", "categoria": "Direito", "grau": 2}
]



for s in servidores:
    if s["grau"] == 1:
        if s["categoria"] == "TI":
            s.update({"group": "xTI"})
        elif s["categoria"] == "Direito":
            s.update({"group": "xDIR"})
        elif s["categoria"] == "Saúde":
            s.update({"group": "xSAU"})
    elif s["grau"] == 2:
        if s["categoria"] == "TI":
            s.update({"group": "yTI"})
        elif s["categoria"] == "Direito":
            s.update({"group": "yDIR"})
        elif s["categoria"] == "Saúde":
            s.update({"group": "ySAU"})

orderna = lambda item:item['group']
servidores.sort(key=orderna)
servidores_agrupados = groupby(servidores,orderna)

for agrupamento, valores_agrupados in servidores_agrupados:
    print(agrupamento)
    nomes=[]
    for servidor in valores_agrupados:
        nomes.append(servidor)
    print template.render({'attrs': nomes,'cat':nomes[0]['categoria'].decode('utf8')}).encode('utf8')
    print "--------------------------------------------------"
#archive = base64.b64encode(template.render({'attrs': nomes}).encode('utf8'))
