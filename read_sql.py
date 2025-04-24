import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("DB_USER")
password = quote_plus(os.getenv("DB_PASSWORD"))
host = os.getenv("DB_HOST")
database = os.getenv("DB_DATABASE")

connection_url = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"

engine = create_engine(connection_url)

media_salario_cargo = pd.read_sql("SELECT c.nome AS 'cargo', AVG(c.salario_base) AS 'media de salario' FROM cargo c GROUP BY c.nome", engine)

qtd_produtos = pd.read_sql("SELECT COUNT(cod_produto) AS 'quantidade de produtos' FROM produto;" ,engine)
qtd_produtos = qtd_produtos["quantidade de produtos"].iloc[0]

qtd_funcionarios = pd.read_sql("SELECT COUNT(cod_funcionario) AS 'quantidade de funcionarios' FROM funcionario", engine)
qtd_funcionarios = qtd_funcionarios["quantidade de funcionarios"].iloc[0]

maiores_fabricantes = pd.read_sql("SELECT fab.nome AS fabricante, COUNT(fab.nome) AS qtd_fabricacoes FROM produto p JOIN fabricante fab ON p.cod_fabricante = fab.cod_fabricante GROUP BY fab.nome ORDER BY qtd_fabricacoes DESC LIMIT 3;", engine)

qtd_fretes = pd.read_sql("SELECT t.nome AS 'transportadora', COUNT(n.cod_transportadora) AS 'qtd de fretes' FROM transportadora t JOIN nota_fiscal n ON t.cod_transportadora = n.cod_transportadora GROUP BY t.nome", engine)

engine.dispose()