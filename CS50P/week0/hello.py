# Perguntando ao usu o seu nome 
name = input("Qual o seu nome? ").strip().title()


# separar nome e sobrenome de usuário
first, last = name.split(" ")

# Dizendo olá para o usuário 
print  (f"Olá, {name}, seja bem vindo a aula de Python de Harvard") 

# Dizendo olá para o usuário com o nome
print  (f"Prazer {first}, tudo certinho?")

# Dizendo olá para o usuário com o sobrenome 
print  (f"Como vai senhor(a), {last}") 