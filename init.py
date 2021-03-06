from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

import pprint
import re

client = MongoClient()
client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')

db = client['sucupira']
collection_docentes = db['docentes']
collection_discentes = db['discentes']
collection_producoes = db['producoes']
collection_trabalhos = db['trabalhos']

# docentes
total_docentes_permanentes = 0
total_docentes_colaboradores = 0
total_docentes_visitantes = 0
total_docentes = 0
total_docentes_com_mestrado = 0
total_docentes_com_doutorado = 0
# discentes
total_discentes_com_mestrado = 0
total_discentes_com_doutorado = 0
total_orientadores = 0
# producoes
total_autores_producoes = 0
total_discentes_autores = 0
total_docentes_autores = 0

#teste
numero = 0

######################################## DOCENTES ########################################


#################### CATEGORIA DOCENTE ####################


########## QUANTIDADE TOTAL DE DOCENTES ##########
docentes = collection_docentes.find({})
for docente in docentes:
  total_docentes += 1


########## QUANTIDADE DE DOCENTES PERMANENTES ##########
docentes_permanentes = collection_docentes.find({'vinculo_com_o_programa.categoria': 'PERMANENTE'})
for docente_permanente in docentes_permanentes:
  total_docentes_permanentes += 1
total_docentes_permanentes = total_docentes_permanentes


########## QUANTIDADE DE DOCENTES COLABORADORES ##########
docentes_colaboradores = collection_docentes.find({'vinculo_com_o_programa.categoria': 'COLABORADOR'})
for docente_permanente in docentes_colaboradores:
  total_docentes_colaboradores += 1
total_docentes_colaboradores = total_docentes_colaboradores

########## QUANTIDADE DE DOCENTES VISITANTES ##########
docentes_visitantes = collection_docentes.find({'vinculo_com_o_programa.categoria': 'VISITANTE'})
for docente_permanente in docentes_visitantes:
  total_docentes_visitantes += 1
total_docentes_visitantes = total_docentes_visitantes

#################### NÍVEL DOCENTES #####################

########## DOCENTES COM MESTRADO ##########

docentes_com_mestrado = collection_docentes.find({'titulacao.nivel': 'Mestrado'})
for docente_com_mestrado in docentes_com_mestrado:
  total_docentes_com_mestrado += 1
total_docentes_com_mestrado = total_docentes_com_mestrado

########## DOCENTES COM DOUTORADO ##########

docentes_com_doutorado = collection_docentes.find({'titulacao.nivel': 'Doutorado'})
for docente_com_doutorado in docentes_com_doutorado:
  total_docentes_com_doutorado += 1
total_docentes_com_doutorado = total_docentes_com_doutorado

######################################## DISCENTES ########################################

########## ORIENTADORES ##########
#Não está retornando todos orientadores ainda

orientadores = collection_discentes.find({'orientadores.nome': {'$exists':'true'}})
for orientador in orientadores:
  total_orientadores += 1

########## NÍVEL DISCENTES ##########

########## DISCENTES COM MESTRADO ##########

discentes_com_mestrado = collection_discentes.find({'dados_institucionais.nivel': 'Mestrado'})
for discente_com_mestrado in discentes_com_mestrado:
  total_discentes_com_mestrado += 1
total_discentes_com_mestrado = total_discentes_com_mestrado

########## DISCENTES COM DOUTORADO ##########

discentes_com_doutorado = collection_discentes.find({'dados_institucionais.nivel': 'Doutorado'})
for discente_com_doutorado in discentes_com_doutorado:
  total_discentes_com_doutorado += 1
total_discentes_com_doutorado = total_discentes_com_doutorado


######################################## PRODUÇÕES ########################################

########## AUTORES DAS PRODUÇÕES ##########
            # Não está retornando todos autores ainda

autores_producoes = collection_producoes.find({'autores.nome': {'$exists':'true'}})
for autor_producao in autores_producoes:
  total_autores_producoes += 1

########## TESTE AUTORES DAS PRODUÇÕES ##########
            # Não está retornando todos autores ainda
            # Não está retornando todos autores ainda
            # Não está retornando todos autores ainda
            # Não está retornando todos autores ainda
            # Não está retornando todos autores ainda
            # Não está retornando todos autores ainda
# autores_producoes = collection_producoes.find({'autores.nome': 'METAXOGLOU, KONSTANTINOS'})
# orientadores = collection_docentes.find({ 'pessoa.nome': { '$regex': "^[A-Z]" }})
todos_autores = collection_producoes.aggregate([{'$unwind': '$pessoa.nome'}])


########## DISCENTES AUTORES ##########

discentes_autores = collection_producoes.find({'autores.categoria': 'Discente'})
for discente_autor in discentes_autores:
  total_discentes_autores += 1
total_discentes_autores = total_discentes_autores


########## DOCENTES AUTORES ##########

docentes_autores = collection_producoes.find({'autores.categoria': 'Docente'})
for docente_autor in docentes_autores:
  total_docentes_autores += 1
total_docentes_autores = total_docentes_autores