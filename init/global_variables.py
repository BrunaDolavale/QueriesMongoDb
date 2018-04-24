import init.init_imports as init_imports

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

collection_producoes = db.producoes
collection_producoes = db['producoes']


collection_trabalhos = db.trabalhos
collection_trabalhos = db['trabalhos']



qtd_doutores_titulados = 0
qtd_mestres_titulados = 0
prop_mestre_doutor = 0
qtd_docentes_permanentes = 0
qtd_docentes_colaboradores = 0
qtd_docentes = 0
qtd_discentes = 0
qtd_orientadores = 0
prop_mestre_doutor = (qtd_mestres_titulados / qtd_doutores_titulados)