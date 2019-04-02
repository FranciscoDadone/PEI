from tkinter import *
import random
import time
import subprocess

width = 1280
height = 720

root=Tk()
root.geometry("1280x720")
root.resizable(False, False)
root.title("PEI - Proyecto Ecológico Institucional (Selección de dificultad)")
root.config(bg="#99d14e")
root.iconbitmap("imgs/icono.ico")

def a():
	global dificultad
	if dificultad.get()=="":
		dificultad.set("destroy")
	else:
		root.destroy()
root.protocol("WM_DELETE_WINDOW", a)
bg="#99d14e"
nonStop=True

seleccionDificultad=Frame(root)
seleccionDificultad.config(width=width, height=height, bg=bg)
frameJugando=Frame(root)
frameJugando.config(width=width, height=height, bg=bg)

for frame in (seleccionDificultad, frameJugando):
    frame.grid(row=0, column=0, sticky='news')
seleccionDificultad.tkraise()
frame=Frame(frameJugando)
frameArriba=Frame(frameJugando)

# VARIABLES
contadorObjetos=11
residuos={"hamburguesa":"organico", "botella":"plastico", "lata":"vidrio", "avion":"papel", "balde":"plastico", "banana":"organico", "bolsa":"plastico", "bolsaPapel":"papel", "botellaVidrio":"vidrio", "caja":"papel", "carton":"papel", "copa":"vidrio", "llave":"vidrio", "manzana":"organico", "manzanaVerde":"organico", "papelImg":"papel", "plato":"vidrio", "regla":"plastico", "rueda":"plastico", "servilleta":"papel", "vidrioImg":"vidrio", "zanahoria":"organico"}
residuosOI={"hamburguesa":"organico", "botella":"inorganico", "lata":"inorganico", "avion":"inorganico", "balde":"inorganico", "banana":"organico", "bolsa":"inorganico", "bolsaPapel":"inorganico", "botellaVidrio":"inorganico", "caja":"inorganico", "carton":"inorganico", "copa":"inorganico", "llave":"inorganico", "manzana":"organico", "manzanaVerde":"organico", "papelImg":"inorganico", "plato":"inorganico", "regla":"inorganico", "rueda":"inorganico", "servilleta":"inorganico", "vidrioImg":"inorganico", "zanahoria":"organico"}
residuosStock=["hamburguesa", "botella", "lata", "avion", "balde", "banana", "bolsa", "bolsaPapel", "botellaVidrio", "caja", "carton", "copa", "llave", "manzana", "manzanaVerde", "papelImg", "plato", "regla", "rueda", "servilleta", "vidrioImg", "zanahoria"]
labelsStock={"botella":"LabelBotella", "hamburguesa":"LabelHamburguesa", "lata":"LabelLata", "avion":"Labelavion", "balde":"Labelbalde", "banana":"Labelbanana", "bolsa":"Labelbolsa", "bolsaPapel":"LabelbolsaPapel", "botellaVidrio":"LabelbotellaVidrio", "caja":"Labelcaja", "carton":"Labelcarton", "copa":"Labelcopa", "llave":"Labelllave", "manzana":"Labelmanzana", "manzanaVerde":"LabelmanzanaVerde", "papelImg":"LabelpapelImg", "plato":"Labelplato", "regla":"Labelregla", "rueda":"Labelrueda", "servilleta":"Labelservilleta", "vidrioImg":"LabelvidrioImg", "zanahoria":"Labelzanahoria"}
labels={}
xSpeed=7
x=-500
win=False
dificultad=StringVar()
print(width, height)
seguir=True
clickButtonYES=False
def menu():
	global seleccionDificultad, clickButtonYES
	root.title("PEI - Proyecto Ecológico Institucional (Selección de dificultad)")
	clickButtonYES=False
	seleccionDificultad.tkraise()
	wait()
#-----------------Seleccion de dificultad-----------------
imgPEI=PhotoImage(file="imgs/PEI.png")
bg="#99d14e"
root.config(bg=bg)
volverMenu=True
labelPEI=Label(seleccionDificultad, image=imgPEI, bg=bg)
labelPEI.place(x=(width/2)-300, y=10)
labelSelectDif=Label(seleccionDificultad, text="  Selecciona la dificultad a la que quieras jugar  ", font="Arial 40", relief="ridge", bg="#bee58a")
labelSelectDif.place(x=80, y=150)
botonDifFacil=Button(seleccionDificultad, text="Fácil", font="Arial 30", width=12, height=3, bg="#38c359", command=lambda:dificultad.set("facil"))
botonDifFacil.place(x=100, y=300)
botonDifNormal=Button(seleccionDificultad, text="Normal", font="Arial 30", width=12, height=3, bg="#e2b414", command=lambda:dificultad.set("normal"))
botonDifNormal.place(x=500, y=300)
botonDifDificil=Button(seleccionDificultad, text="Difícil", font="Arial 30", width=12, height=3, bg="#ed3921", command=lambda:dificultad.set("dificil"))
botonDifDificil.place(x=880, y=300)
#-----------FUNCIONES GENERALES------------
def settingsComunes():
	global height, width, root, frame, frameArriba, filename, filename2, instrucciones, dificultad, visorDifLabel, background_label, background_label2, bg, perdisteLabel
	C = Canvas(frame, bg="blue", height=height, width=width)
	filename = PhotoImage(file = "imgs/maderaNegra.png")
	background_label = Label(frame, image=filename, bg=bg)
	background_label.place(x=0, y=0, relwidth=1, relheight=1)
	C2 = Canvas(frameArriba, bg="blue", height=height, width=width)
	filename2 = PhotoImage(file = "imgs/maderaNegra.png")
	background_label2 = Label(frameArriba, image=filename, bg=bg)
	background_label2.place(x=0, y=0, relwidth=1, relheight=1)
	frame.place(height=height, width=width, rely=0.8)
	frameArriba.place(height=height/7.5, width=width, rely=0)
	#Instrucciones
	instrucciones=Label(frameArriba, text="Clasificá los objetos haciendo click en los tachos de basura.", font="Arial 15", bg="#212121", fg="white", relief="ridge")
	instrucciones.place(x=width/2, y=30, anchor=CENTER)
	#Visor de dificultad
	if dificultad.get()=="facil":
		dificultadL="fácil"
	elif dificultad.get()=="normal":
		dificultadL="normal"
	elif dificultad.get()=="dificil":
		dificultadL="difícil"
	visorDifLabel=Label(frameArriba, text=" Jugando en " + str(dificultadL) + " ", font="Arial 17", bg="#212121", fg="white", relief="ridge")
	visorDifLabel.place(x=30, y=25)
	try: perdisteLabel.destroy()
	except: pass
def gameReset():
	global residuos, contadorObjetos, resetButtonYES, perdisteLabel, resetLabel, resetButtonNO, LabelTachoPapel, LabelTachoVidrio, LabelTachoOrganico, LabelTachoPlastico, residuosStock, contadorClasificar, winLabel, LabelTachoInorganico, perdisteTiempoLabel, dificultad, seguir, cuentaR, volverMenu, visorDifLabel, resetButtonVolver, x, residuosOI, labelsStock, clickButtonYES, instrucciones
	x=-500
	if dificultad.get()=="dificil":
		contadorObjetos=21
		try: perdisteLabel.destroy()
		except: pass
	else:
		contadorObjetos=11
		try: perdisteLabel.destroy()
		except: pass
	residuos={"hamburguesa":"organico", "botella":"plastico", "lata":"vidrio", "avion":"papel", "balde":"plastico", "banana":"organico", "bolsa":"plastico", "bolsaPapel":"papel", "botellaVidrio":"vidrio", "caja":"papel", "carton":"papel", "copa":"vidrio", "llave":"vidrio", "manzana":"organico", "manzanaVerde":"organico", "papelImg":"papel", "plato":"vidrio", "regla":"plastico", "rueda":"plastico", "servilleta":"papel", "vidrioImg":"vidrio", "zanahoria":"organico"}
	residuosOI={"hamburguesa":"organico", "botella":"inorganico", "lata":"inorganico", "avion":"inorganico", "balde":"inorganico", "banana":"organico", "bolsa":"inorganico", "bolsaPapel":"inorganico", "botellaVidrio":"inorganico", "caja":"inorganico", "carton":"inorganico", "copa":"inorganico", "llave":"inorganico", "manzana":"organico", "manzanaVerde":"organico", "papelImg":"inorganico", "plato":"inorganico", "regla":"inorganico", "rueda":"inorganico", "servilleta":"inorganico", "vidrioImg":"inorganico", "zanahoria":"organico"}
	residuosStock=["hamburguesa", "botella", "lata", "avion", "balde", "banana", "bolsa", "bolsaPapel", "botellaVidrio", "caja", "carton", "copa", "llave", "manzana", "manzanaVerde", "papelImg", "plato", "regla", "rueda", "servilleta", "vidrioImg", "zanahoria"]
	labelsStock={"botella":"LabelBotella", "hamburguesa":"LabelHamburguesa", "lata":"LabelLata", "avion":"Labelavion", "balde":"Labelbalde", "banana":"Labelbanana", "bolsa":"Labelbolsa", "bolsaPapel":"LabelbolsaPapel", "botellaVidrio":"LabelbotellaVidrio", "caja":"Labelcaja", "carton":"Labelcarton", "copa":"Labelcopa", "llave":"Labelllave", "manzana":"Labelmanzana", "manzanaVerde":"LabelmanzanaVerde", "papelImg":"LabelpapelImg", "plato":"Labelplato", "regla":"Labelregla", "rueda":"Labelrueda", "servilleta":"Labelservilleta", "vidrioImg":"LabelvidrioImg", "zanahoria":"Labelzanahoria"}	
	try: perdisteLabel.destroy()
	except: pass
	try: LabelTachoPapel.config(state=NORMAL)
	except: pass
	try: LabelTachoVidrio.config(state=NORMAL)
	except: pass
	try: LabelTachoOrganico.config(state=NORMAL)
	except: pass
	try: LabelTachoPlastico.config(state=NORMAL)
	except: pass
	try: LabelTachoInorganico.config(state=NORMAL)
	except: pass
	try: LabelTachoOrganico.config(state=NORMAL)
	except: pass
	cuentaR=60
	seguir=True
	if dificultad.get()=="dificil" and clickButtonYES:
		timer()
	try:
		resetButtonYES.destroy()
		resetButtonNO.destroy()
		resetLabel.destroy()
		contadorClasificar.destroy()
		resetButtonVolver.destroy()
	except: pass
	try: winLabel.destroy()
	except: pass
	try: perdisteTiempoLabel.destroy()
	except: pass
	labelsDef()
	randomObj()
	mostrarObjeto()
	instrucciones=Label(frameArriba, text="Clasificá los objetos haciendo click en los tachos de basura.", font="Arial 15", bg="#212121", fg="white", relief="ridge")
	instrucciones.place(x=width/2, y=30, anchor=CENTER)
	try: perdisteLabel.destroy()
	except: pass
def move():
	global xSpeed, x, height, width, currentObj, dificultad, contadorObjetos, labels, labelsStock, randomizer
	if x==x:
		x+=xSpeed
	try: labels[labelsStock[randomizer]].place(x=x, y=height/2, anchor=CENTER)
	except:
		x=-500
		xSpeed=7
	if x<width/2:
		if dificultad.get()=="facil" or dificultad.get()=="normal":
			root.after(10, move)
			xSpeed=7
	if x==1460:
		labels[labelsStock[randomizer]].destroy()
	if dificultad.get()=="dificil" and x<1460:
		root.after(10, move)
		if contadorObjetos<5:
			xSpeed+=0.2
		elif contadorObjetos==10:
			xSpeed=8
def randomObj():
	global objeto, randomizer, residuosStock, contadorObjetos, contadorClasificar
	contadorObjetos-=1
	a=""
	if contadorObjetos<10:
		a="0"
	contadorClasificar=Label(frame, text="Objetos restantes: " + a + str(contadorObjetos), font="Arial 30", bg="#212121", fg="white", relief="ridge")
	contadorClasificar.grid(row=5, column=6, padx=50)
	try:
		randomizer=random.choice(residuosStock)
	except:
		pass
	objeto=""
	for obj in residuosStock:
		if randomizer==obj:
			objeto=obj
			del residuosStock[residuosStock.index(objeto)]
def clickButtonYESDEF():
	global clickButtonYES, instrucciones
	clickButtonYES=True
	gameReset()
def resetCheck():
	global labels, objeto, resetButtonYES, LabelTachoPapel, LabelTachoVidrio, LabelTachoOrganico, LabelTachoPlastico, resetButtonNO, resetLabel, instrucciones, x, xSpeed, LabelTachoInorganico, resetButtonVolver
	instrucciones.destroy()
	resetLabel=Label(frameArriba, text="¿Deseas volver a jugar?", font="Arial 20", bg="#212121", fg="white")
	resetLabel.place(anchor=CENTER, x=width/2, y=25)
	resetButtonYES=Button(frameArriba, text="Si ", font="Arial 15", bg="#212121", fg="white", relief="ridge", command=lambda:clickButtonYESDEF())
	resetButtonYES.place(anchor=CENTER, x=(width/2)-110, y=70)
	resetButtonNO=Button(frameArriba, text="No", font="Arial 15", bg="#212121", fg="white", relief="ridge", command=lambda:root.destroy())
	resetButtonNO.place(anchor=CENTER, x=(width/2)-60, y=70)
	resetButtonVolver=Button(frameArriba, text="Volver al menú", font="Arial 15", bg="#212121", fg="white", relief="ridge", command=lambda:menu())
	resetButtonVolver.place(anchor=CENTER, x=(width/2)+50, y=70)
	try: LabelTachoPapel.config(state=DISABLED)
	except: pass
	try: LabelTachoVidrio.config(state=DISABLED)
	except: pass
	try: LabelTachoPlastico.config(state=DISABLED)
	except: pass
	try: LabelTachoOrganico.config(state=DISABLED)
	except: pass
	try: LabelTachoInorganico.config(state=DISABLED)
	except: pass
	x=-500
	xSpeed=7
	for i in labels:
		labels[i].destroy()
# IMAGENES RECIDUOS
botella=PhotoImage(file="imgs/botella.png")
hamburguesa=PhotoImage(file="imgs/hamburguesa.png")
lata=PhotoImage(file="imgs/lata.png")
avion=PhotoImage(file="imgs/avion.png")
balde=PhotoImage(file="imgs/balde.png")
banana=PhotoImage(file="imgs/banana.png")
bolsa=PhotoImage(file="imgs/bolsa.png")
bolsaPapel=PhotoImage(file="imgs/bolsaPapel.png")
botellaVidrio=PhotoImage(file="imgs/botellaVidrio.png")
caja=PhotoImage(file="imgs/caja.png")
carton=PhotoImage(file="imgs/carton.png")
copa=PhotoImage(file="imgs/copa.png")
llave=PhotoImage(file="imgs/llave.png")
manzana=PhotoImage(file="imgs/manzana.png")
manzanaVerde=PhotoImage(file="imgs/manzanaVerde.png")
papelImg=PhotoImage(file="imgs/papelImg.png")
plato=PhotoImage(file="imgs/plato.png")
regla=PhotoImage(file="imgs/regla.png")
rueda=PhotoImage(file="imgs/rueda.png")
servilleta=PhotoImage(file="imgs/servilleta.png")
vidrioImg=PhotoImage(file="imgs/vidrioImg.png")
zanahoria=PhotoImage(file="imgs/zanahoria.png")

def labelsDef():
	global labels, frameJugando
	labels["LabelBotella"]=Label(image=botella, bg=bg)
	labels["LabelHamburguesa"]=Label(image=hamburguesa, bg=bg)
	labels["LabelLata"]=Label(image=lata, bg=bg)
	labels["Labelavion"]=Label(image=avion, bg=bg)
	labels["Labelbalde"]=Label(image=balde, bg=bg)
	labels["Labelbanana"]=Label(image=banana, bg=bg)
	labels["Labelbolsa"]=Label(image=bolsa, bg=bg)
	labels["LabelbolsaPapel"]=Label(image=bolsaPapel, bg=bg)
	labels["LabelbotellaVidrio"]=Label(image=botellaVidrio, bg=bg)
	labels["Labelcaja"]=Label(image=caja, bg=bg)
	labels["Labelcarton"]=Label(image=carton, bg=bg)
	labels["Labelcopa"]=Label(image=copa, bg=bg)
	labels["Labelllave"]=Label(image=llave, bg=bg)
	labels["Labelmanzana"]=Label(image=manzana, bg=bg)
	labels["LabelmanzanaVerde"]=Label(image=manzanaVerde, bg=bg)
	labels["LabelpapelImg"]=Label(image=papelImg, bg=bg)
	labels["Labelplato"]=Label(image=plato, bg=bg)
	labels["Labelregla"]=Label(image=regla, bg=bg)
	labels["Labelrueda"]=Label(image=rueda, bg=bg)
	labels["Labelservilleta"]=Label(image=servilleta, bg=bg)
	labels["LabelvidrioImg"]=Label(image=vidrioImg, bg=bg)
	labels["Labelzanahoria"]=Label(image=zanahoria, bg=bg)
def mostrarObjeto():
	global currentObj, labelsStock, randomizer
	currentObj=labelsStock[randomizer]
	move()
def tachoBasura(residuo):
	global residuos, currentObj, labels, objeto, perdisteLabel, seguir, winLabel, contadorObjetos, x, perdisteTiempoLabel, seguir, win
	seguir=True
	if residuo==residuos.get(objeto) or residuo==residuosOI.get(objeto):
		labels[currentObj].destroy()
		del labels[currentObj]
		x=-600
		randomObj()
		mostrarObjeto()
	else:
		perdisteLabel=Label(frameJugando, text="¡Perdiste!", font="Arial 150 bold", bg=bg)
		perdisteLabel.place(x=width/2, y=height/2, anchor=CENTER)
		resetCheck()
		seguir=False
	if contadorObjetos==0:
		winLabel=Label(frameJugando, text="¡Ganaste!", font="Arial 150 bold", bg=bg)
		winLabel.place(x=width/2, y=height/2, anchor=CENTER)
		resetCheck()
		seguir=False
		win=True
def timer():
	global cuentaR, seguir, perdisteTiempoLabel, perdisteLabel, win, labelTimer
	b=""
	if cuentaR<10:
		b="0"
	labelTimer=Label(frameArriba, bg="#212121", text="Tiempo restante: " + b + str(int(cuentaR)) + " segundos!", font="Arial 15", fg="white", relief="ridge")
	if cuentaR>=0:
		labelTimer.place(x=980, y=25)
		labelTimer.update()
	else:
		cuentaR=0
		perdisteTiempoLabel=Label(text="Se te acabó el tiempo :(", font="Arial 50 bold", bg=bg)
		perdisteTiempoLabel.place(x=width/2, y=(height/2)+130, anchor=CENTER)
		seguir=False
	if cuentaR<=0 and win!=True:
		perdisteLabel=Label(frameJugando, text="¡Perdiste!", font="Arial 150 bold", bg=bg)
		perdisteLabel.place(x=width/2, y=height/2, anchor=CENTER)
		perdisteTiempoLabel=Label(text="Se te acabó el tiempo :(", font="Arial 50 bold", bg=bg)
		perdisteTiempoLabel.place(x=width/2, y=(height/2)+130, anchor=CENTER)
		resetCheck()
		seguir=False
	if seguir:
		if cuentaR!=(cuentaR-1):
			cuentaR-=1
		root.after(1000, timer)
####################################### DIFICULTADES ##########################################
def dificultades():
	global dificultad, bg, frameJugando, width, height, root, cuentaR, contadorObjetos, LabelTachoPapel, frame, frameArriba, tachoPapel, tachoVidrio, tachoOrganico, tachoPlastico, tachoInorganico, LabelTachoVidrio, LabelTachoOrganico, LabelTachoPlastico, LabelTachoInorganico, perdisteTiempoLabel, perdisteLabel
	gameReset()
	#-----------------NORMAL-----------------
	if dificultad.get()=="normal":
		contadorObjetos=11
		bg="#e2b414"
		frameJugando.config(width=width, height=height, bg=bg)
		frameJugando.tkraise()
		root.title("PEI - Proyecto Ecológico Institucional (Dificultad Normal)")
		root.config(bg=bg)
		settingsComunes()
		randomObj()
		# IMAGENES TACHOS
		LabelTachoPapel=Button(frame, image=tachoPapel, bg="#0d0d0d", command=lambda:tachoBasura("papel"))
		LabelTachoPapel.grid(row=5, column=1, padx=50)
		LabelTachoVidrio=Button(frame, image=tachoVidrio, bg="#0d0d0d", command=lambda:tachoBasura("vidrio"))
		LabelTachoVidrio.grid(row=5, column=2, padx=50)
		LabelTachoOrganico=Button(frame, image=tachoOrganico, bg="#0d0d0d", command=lambda:tachoBasura("organico"))
		LabelTachoOrganico.grid(row=5, column=3, padx=50)
		LabelTachoPlastico=Button(frame, image=tachoPlastico, bg="#0d0d0d", command=lambda:tachoBasura("plastico"))
		LabelTachoPlastico.grid(row=5, column=4, padx=50)
		labelsDef()
		mostrarObjeto()
		try: perdisteLabel.destroy()
		except: pass
	#-----------FACIL---------------
	elif dificultad.get()=="facil":
		contadorObjetos=11
		bg="#99d14e"
		frameJugando.config(width=width, height=height, bg=bg)
		frameJugando.tkraise()
		root.title("PEI - Proyecto Ecológico Institucional (Dificultad Fácil)")
		root.config(bg=bg)
		settingsComunes()
		randomObj()
		# IMAGENES TACHOS
		LabelTachoOrganico=Button(frame, image=tachoOrganico, bg="#0d0d0d", command=lambda:tachoBasura("organico"))
		LabelTachoOrganico.grid(row=5, column=1, padx=50)
		LabelTachoInorganico=Button(frame, image=tachoInorganico, bg="#0d0d0d", command=lambda:tachoBasura("inorganico"))
		LabelTachoInorganico.grid(row=5, column=2, padx=50)
		labelsDef()
		mostrarObjeto()
		try: perdisteLabel.destroy()
		except: pass
	elif dificultad.get()=="dificil":
		cuentaR=61
		timer()
		contadorObjetos=21
		bg="#fd5d47"
		frameJugando.config(width=width, height=height, bg=bg)
		frameJugando.tkraise()
		perdisteLabel=Label(text="¡Perdiste!", font="Arial 150 bold", bg=bg)
		root.title("PEI - Proyecto Ecológico Institucional (Dificultad Difícil)")
		root.config(bg=bg)
		settingsComunes()
		randomObj()
		# IMAGENES TACHOS
		LabelTachoPapel=Button(frame, image=tachoPapel, bg="#0d0d0d", command=lambda:tachoBasura("papel"))
		LabelTachoPapel.grid(row=5, column=1, padx=50)
		LabelTachoVidrio=Button(frame, image=tachoVidrio, bg="#0d0d0d", command=lambda:tachoBasura("vidrio"))
		LabelTachoVidrio.grid(row=5, column=2, padx=50)
		LabelTachoOrganico=Button(frame, image=tachoOrganico, bg="#0d0d0d", command=lambda:tachoBasura("organico"))
		LabelTachoOrganico.grid(row=5, column=3, padx=50)
		LabelTachoPlastico=Button(frame, image=tachoPlastico, bg="#0d0d0d", command=lambda:tachoBasura("plastico"))
		LabelTachoPlastico.grid(row=5, column=4, padx=50)
		labelsDef()
		mostrarObjeto()
		try: perdisteLabel.destroy()
		except: pass
	else:
		root.destroy()
def wait():
	global dificultad, tachoOrganico, tachoPlastico, tachoPapel, tachoVidrio, tachoInorganico
	root.wait_variable(dificultad)
	if dificultad.get()=="dificil":
		tachoOrganico=PhotoImage(file="imgs/organicoDificil.png")
		tachoPlastico=PhotoImage(file="imgs/plasticoDificil.png")
		tachoPapel=PhotoImage(file="imgs/papelDificil.png")
		tachoVidrio=PhotoImage(file="imgs/vidrioDificil.png")
	else: 
		tachoOrganico=PhotoImage(file="imgs/organico.png")
		tachoPapel=PhotoImage(file="imgs/papel.png")
		tachoVidrio=PhotoImage(file="imgs/vidrio.png")
		tachoPlastico=PhotoImage(file="imgs/plastico.png")
		tachoInorganico=PhotoImage(file="imgs/inorganico.png")
	dificultades()
wait()
root.mainloop()