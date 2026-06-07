import sqlite3

conexao = sqlite3.connect('petshop.db')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS animais (
    nome TEXT, especie TEXT, idade INT, peso_kg REAL, vacinado TEXT
)''')
conexao.commit()


cursor.execute('Insert into animais values("Rex","Cachorro",3,12.5,"Sim")')
cursor.execute('Insert into animais values("Mimi","Gato",7,4.2,"Sim")')
cursor.execute('Insert into animais values("Loro","Papagaio",2,0.8,"Não")')
cursor.execute('Insert into animais values("Pipoca","Hamster",1,0.15,"Não")')
cursor.execute('Insert into animais values("Thor","Cachorro",5,18.0,"Sim")')
cursor.execute('Insert into animais values("Jade","Iguana Verde",15,6.89,"Não")')
conexao.commit()

visitar =cursor.execute('Select*from animais ').fetchall() 

for nome, especie, idade,peso_kg,vacinado  in visitar: 

    print(f"{nome} |{especie} |{idade} | {peso_kg} | {vacinado}") 
