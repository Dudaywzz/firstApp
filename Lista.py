objetos = ["Copo", "Colher", "Garfo", "Faca", "Prato"]
print("Objetos da lista:")
print("--" *30)

objetos.append('Guardanapo')
print("Objeto adicionado:")
print("--" *30)

objeto = objetos[1]
print("Posição do objetos[1]")
print("--" *30)

objetos.remove("Garfo")
print("Objeto removido:")
print("--" *30)

len(objetos)
print(len(objetos))
print("--" *30)

for objeto in objetos:
    print(objeto)
print("--" *30)

if 'cadeira' in objetos:
    objetos.remove("Cadeira")
    print("Objeto removido:")
    print("--" * 30)
else:
    objetos.append("Cadeira")
    print("Objeto adicionado:")

objetos.sort()
print("--" *30)

primeira = objetos[0]
print("Primeiro objeto:")


len(objetos) - 1
print("Último objeto:")
print("--" *30)

objetos.clear()










