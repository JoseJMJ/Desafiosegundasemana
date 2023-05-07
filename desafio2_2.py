Texto_frase= input("BIENVENIDO, a continuacion ingrese una frase").lower() 
lista_texto = list(Texto_frase) 
print("ingrese 3 letras que no se repitan") # Se le solicitan las letras al usuario
let1 = input("ingresá la primer letra: ").lower() # A continuacion se modifican los valores con lower
let2 = input("ingresá la segunda letra: ").lower() 
let3 = input("ingresá la tercer letra: ").lower() 

#1) Cantidad de veces que aparece cada una de las letras que eligio. 

contador1=0
contador2=0
contador3=0

for l1 in lista_texto: 
    if l1 == let1: 
        contador1 += 1 
for l2 in lista_texto:
    if l2 == let2:
        contador2 += 1
for l3 in lista_texto:
    if l3 == let3:
        contador3 += 1 
print(f"La letra '{let1}' aparece {contador1} veces en el texto que ingresaste.")
print(f"La letra '{let2}' aparece {contador2} veces en el texto que ingresaste.")
print(f"La letra '{let3}' aparece {contador3} veces en el texto que ingresaste.")

#2) Cuantas palabras hay en total en todo el texto.
palabras = Texto_frase.split() 
c_palabras = len(palabras)
print('el texto tiene',c_palabras,'palabras')
#3)Cual es la primera letra y cuál es la última. (Indexación)
primera_letra = lista_texto[0]
ultima_letra = lista_texto[-1]
print("la primera letra es:",primera_letra[0],"y la ultima letra es:",ultima_letra[-1])
#4)Mostrar el texto en orden inverso
al_reves = Texto_frase[::-1]
print(f"su texto al reves es:",al_reves)
#5)Decir si la palabra "python" aparece en el texto.
esta_python = "python" in Texto_frase.lower()
libro_texto = {True: "La palabra python está presente en la frase.", False: "la palabra python no se encuentra en la frase."}
print(libro_texto[esta_python])