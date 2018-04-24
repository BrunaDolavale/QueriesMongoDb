import init.global_variables as global_variables



## PROPORCAO DE MESTRES PARA DOUTORES TITULADOS

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
#print(qtd_docentes)

porcentagem_docentes = (qtd_docentes_permanentes / qtd_docentes * 100)
#print("Porcentagem docentes: ")
#print(porcentagem_docentes)



# Dimensão do corpo discente  em relação à dimensão do grupo de DP

qtd_discentes = 0
discentes = collection_discentes.find({})
for dados in discentes:
  qtd_discentes = qtd_discentes + 1

dimensao_dis_dp = (qtd_discentes/qtd_docentes_permanentes)
#print(dimensao_dis_dp)


## Percentagem de DPs que ministram aulas na graduação
porcentagem = (qtd_docentes_permanentes / qtd_docentes * 100)
#print(porcentagem)





## Número médio de orientações concluídas por docente permanente no triênio
qtd_orientadores = 0
orientadores = collection_discentes.find({'orientadores.nome': { '$regex': "(^P)" }})

for orientador in orientadores:
   print()
  # 
iguais = collection_discentes.aggregate(
   [ { "$match": { 'nome': "PEDRO CAVALCANTI GOMES FERREIRA" } }, { "$group": { '_id': "$category", 'count': { "$sum": 1 } } } ],
   # { collation: { locale: "fr", strength: 1 } }
);
for igual in iguais:
  print(igual)
