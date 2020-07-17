import sys
from tkinter import *

def cypher():
    try:
        textoAscii = ''
        for i in entrada_texto.get():
            textoAscii = textoAscii+ord(i).__str__() + ' '
        cadenaBin = textoAscii[:-1].split(' ')
        textoBinario = ''
        for j in cadenaBin:
            textoBinario = textoBinario + bin(int(j))[2:] + " "
        etiqueta3.config(text=textoBinario[:-1])
    except:
        etiqueta3.config(text="introduce un nuevo valor")

def decypher():
    try:
        cadenabin = entrada_texto.get().split(' ')
        textoAscii = ''
        for i in cadenabin:
            textoAscii = textoAscii + str(int(i,2)) + " "
        textoAscii = textoAscii[:-1].split(" ")
        texto = ''.join(chr(int(i)) for i in textoAscii)
        etiqueta4.config(text = texto)
    except:
        etiqueta4.config(text="introduce un nuevo valor")

app = Tk()
app.title("Operaciones")

# Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50, 50), pady=(10, 10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Texto")
etiqueta.grid(column=1, row=1, sticky=(W, E))

etiqueta3= Label(vp, text="cifrar")
etiqueta3.grid(column=1, row=5, sticky=(W, E))
etiqueta4= Label(vp, text="descifrar")
etiqueta4.grid(column=2, row=5, sticky=(W, E))

boton = Button(vp, text="Cypher", command=cypher)
boton.grid(column=1, row=4)
boton2 = Button(vp, text="Descypher", command=decypher)
boton2.grid(column=2, row=4)

valor = ""
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=2, row=1)


app.mainloop()
