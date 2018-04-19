from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
import re

client = MongoClient()
client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')

  ## Getting Database
db = client.sucupira
db = client['sucupira']

  ##Getting Collections
collection_docentes = db.docentes
collection_docentes = db['docentes']
collection_discentes = db.discentes
collection_discentes = db['discentes']
qtd_doutores_titulados = 0
qtd_mestres_titulados = 0
##Modelo que retorna 1:
  ##print(collection_docentes.find_one({ 'pessoa.nacionalidade': { "$not": { "$eq": 'Brasil' } } }))
##****************************************************************************************************##





# PROPORCAO DE MESTRES PARA DOUTORES TITULADOS

mestres_titulados = collection_discentes.find({'$and':[{'dados_institucionais.situacao':{'$eq':'TITULADO'}},
  {'dados_institucionais.nivel':{'$eq': 'Mestrado'}}]})

for dados in mestres_titulados:
  qtd_mestres_titulados = qtd_mestres_titulados + 1
# print(qtd_mestres_titulados)

doutores_titulados = collection_discentes.find({'$and':[{'dados_institucionais.situacao':{'$eq':'TITULADO'}},
  {'dados_institucionais.nivel':{'$eq': 'Doutorado'}}]})
for dados in doutores_titulados:
  qtd_doutores_titulados = qtd_doutores_titulados + 1
# print(qtd_doutores_titulados)

prop_mestre_doutor = 0
prop_mestre_doutor = (qtd_mestres_titulados / qtd_doutores_titulados)
# print(prop_mestre_doutor)





## No. Total de DP dividido pelo no. total de docentes (permanentes + colaboradores)

qtd_docentes_permanentes = 0
docentes_permanentes = collection_docentes.find({'vinculo_com_o_programa.categoria': 'PERMANENTE'})
for dados in docentes_permanentes:
  qtd_docentes_permanentes = qtd_docentes_permanentes + 1
#print("Quantidade: ")
#print(qtd_docentes_permanentes)

qtd_docentes_colaboradores = 0
docentes_colaboradores = collection_docentes.find({'vinculo_com_o_programa.categoria': 'COLABORADOR'})
for dados in docentes_colaboradores:
  qtd_docentes_colaboradores = qtd_docentes_colaboradores + 1
#print("Quantidade: ")
#print(qtd_docentes_colaboradores)

qtd_docentes = 0
docentes = collection_docentes.find({})
for dados in docentes:
  qtd_docentes = qtd_docentes + 1
##print(qtd_docentes)

porcentagem_docentes = (qtd_docentes_permanentes / qtd_docentes)
#print("Porcentagem docentes: ")
#print(porcentagem_docentes * 100)



# Dimensão do corpo discente  em relação à dimensão do grupo de DP

qtd_discentes = 0
discentes = collection_discentes.find({})
for dados in discentes:
  qtd_discentes = qtd_discentes + 1

dimensao_dis_dp = (qtd_discentes/qtd_docentes_permanentes)
##print(dimensao_dis_dp)


## Percentagem de DPs que ministram aulas na graduação
porcentagem = (qtd_docentes_permanentes / qtd_docentes * 100)
##print(porcentagem)





## Número médio de orientações concluídas por docente permanente no triênio
qtd_orientadores = 0
# orientadores = collection_docentes.find({ 'pessoa.nome': { '$regex': "(^P)" }})
orientadores = collection_docentes.find({ 'pessoa.nome': { '$regex': "^[A-Z]" }})

for dados in orientadores:
  print(orientadores)


