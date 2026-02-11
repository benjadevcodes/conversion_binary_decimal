from tkinter import *
from Comunication_test import *
import math

#Creacion de ventana principal + conexion a plc
class app():
	def __init__(self,ventMain):
		self.ventMain = ventMain
		self.ventMain.title("Variables analogas")
		self.ventMain.geometry('600x300')
		self.ventMain.wm_attributes("-topmos",True)
		self.ventMain.resizable(width=True, height=True)
		self.PLC = C_plc(host='127.0.0.1', port=502) # para simulador 221 ip = 127.0.0.1
		self.canvas = Canvas(width=600, height=700, bg='lightgrey')		
		self.canvas.pack(expand=NO, fill=BOTH)

#bin
		tipo_letra = "Calibri"
		tamaño_letra = 18
	
		self.etiqueta_1 = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
		self.etiqueta_2 = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
		self.etiqueta_3 = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
		self.etiqueta_4 = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
		self.etiqueta_5 = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
		self.etiqueta_6 = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
		self.etiqueta_7 = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
		self.etiqueta_8 = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
		self.etiqueta_9 = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
		self.etiqueta_10 = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
		self.etiqueta_11 = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
		self.etiqueta_12 = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
		self.etiqueta_13 = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
		self.etiqueta_14 = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
		self.etiqueta_15 = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
		self.etiqueta_16 = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
		self.suma_show = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
		self.binario_show = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
		self.yes_no_show = Label(self.ventMain,font=(tipo_letra,tamaño_letra))
  
		self.etiqueta_1.place(x=0,y=0)
		self.etiqueta_2.place(x=0,y=30)
		self.etiqueta_3.place(x=0,y=60)
		self.etiqueta_4.place(x=0,y=90)
		self.etiqueta_5.place(x=0,y=120)
		self.etiqueta_6.place(x=0,y=150)
		self.etiqueta_7.place(x=0,y=180)
		self.etiqueta_8.place(x=0,y=210)
		self.etiqueta_9.place(x=60,y=0)
		self.etiqueta_10.place(x=60,y=30)
		self.etiqueta_11.place(x=60,y=60)
		self.etiqueta_12.place(x=60,y=90)
		self.etiqueta_13.place(x=60,y=120)
		self.etiqueta_14.place(x=60,y=150)
		self.etiqueta_15.place(x=60,y=180)
		self.etiqueta_16.place(x=60,y=210)
		self.suma_show.place(x=120,y=0)
		self.binario_show.place(x=0,y=260) 
		self.yes_no_show.place(x=250,y=120)
  

   
		self.ventMain.after(100,self.Actualizar)
#actualizar		
	def Actualizar(self):
		self.bits = self.PLC.leerCoil()

		self.etiqueta_1.config(text=self.bits[0])
		self.etiqueta_2.config(text=self.bits[1])
		self.etiqueta_3.config(text=self.bits[2])
		self.etiqueta_4.config(text=self.bits[3])
		self.etiqueta_5.config(text=self.bits[4])
		self.etiqueta_6.config(text=self.bits[5])
		self.etiqueta_7.config(text=self.bits[6])
		self.etiqueta_8.config(text=self.bits[7])
		self.etiqueta_9.config(text=self.bits[8])
		self.etiqueta_10.config(text=self.bits[9])
		self.etiqueta_11.config(text=self.bits[10])
		self.etiqueta_12.config(text=self.bits[11])
		self.etiqueta_13.config(text=self.bits[12])
		self.etiqueta_14.config(text=self.bits[13])
		self.etiqueta_15.config(text=self.bits[14])
		self.etiqueta_16.config(text=self.bits[15])
#read
		decb_1 = self.bits[0]*(2**0)
		decb_2 = self.bits[1]*(2**1)
		decb_3 = self.bits[2]*(2**2)
		decb_4 = self.bits[3]*(2**3)
		decb_5 = self.bits[4]*(2**4)
		decb_6 = self.bits[5]*(2**5)
		decb_7 = self.bits[6]*(2**6)
		decb_8 = self.bits[7]*(2**7)
		decb_9 = self.bits[8]*(2**8)
		decb_10 = self.bits[9]*(2**9)
		decb_11 = self.bits[10]*(2**10)
		decb_12 = self.bits[11]*(2**11)
		decb_13 = self.bits[12]*(2**12)
		decb_14 = self.bits[13]*(2**13)
		decb_15 = self.bits[14]*(2**14)
		decb_16 = self.bits[15]*(2**15)
		
		numero = decb_1 + decb_2 + decb_3 + decb_4 + decb_5 + decb_6 + decb_7 + decb_8 + decb_9 + decb_10 + decb_11+ decb_12 + decb_13+ decb_14+ decb_15
		
		self.suma_show.config(text="Bin/Dec: " + str(numero))
		binary = ["","","","","","","","","","","","","","","","",""]
# lectura y primera conversion dec bin  
		valor_analogo = self.PLC.leerAnalogo(0,1)
		el_valor = valor_analogo[0]
		el_valor_div = el_valor/2
		dec = el_valor_div - (math.floor(el_valor_div))


#1 conversion
		if dec == 0.5:
			binary[14] = 1
			self.yes_no_show.config(text=binary[14])
		if dec == 0.0:
			binary[14] = 0
			self.yes_no_show.config(text=binary[14])

		el_valor_div = ((el_valor_div-dec)/2)
#2 conversion
		dec = el_valor_div - (math.floor(el_valor_div))

		if dec == 0.5:
			binary[13] = 1
			self.yes_no_show.config(text=binary[13])
		if dec == 0.0:
			binary[13] = 0
			self.yes_no_show.config(text=binary[13])
		el_valor_div = ((el_valor_div-dec)/2)
#3 conversion
		dec = el_valor_div - (math.floor(el_valor_div))

		if dec == 0.5:
			binary[12] = 1
			self.yes_no_show.config(text=binary[12])
		if dec == 0.0:
			binary[12] = 0
			self.yes_no_show.config(text=binary[12])
		el_valor_div = ((el_valor_div-dec)/2)
#4 conversion
		dec = el_valor_div - (math.floor(el_valor_div))

		if dec == 0.5:
			binary[11] = 1
			self.yes_no_show.config(text=binary[11])
		if dec == 0.0:
			binary[11] = 0
			self.yes_no_show.config(text=binary[11])
		el_valor_div = ((el_valor_div-dec)/2)
#5 conversion
		dec = el_valor_div - (math.floor(el_valor_div))

		if dec == 0.5:
			binary[10] = 1
			self.yes_no_show.config(text=binary[10])
		if dec == 0.0:
			binary[10] = 0
			self.yes_no_show.config(text=binary[10])
		el_valor_div = ((el_valor_div-dec)/2)
#6 conversion
		dec = el_valor_div - (math.floor(el_valor_div))

		if dec == 0.5:
			binary[9] = 1
			self.yes_no_show.config(text=binary[9])
		if dec == 0.0:
			binary[9] = 0
			self.yes_no_show.config(text=binary[9])
		el_valor_div = ((el_valor_div-dec)/2)
#7 conversion
		dec = el_valor_div - (math.floor(el_valor_div))

		if dec == 0.5:
			binary[8] = 1
			self.yes_no_show.config(text=binary[8])
		if dec == 0.0:
			binary[8] = 0
			self.yes_no_show.config(text=binary[8])
		el_valor_div = ((el_valor_div-dec)/2)
#8 conversion
		dec = el_valor_div - (math.floor(el_valor_div))

		if dec == 0.5:
			binary[7] = 1
			self.yes_no_show.config(text=binary[7])
		if dec == 0.0:
			binary[7] = 0
			self.yes_no_show.config(text=binary[7])
		el_valor_div = ((el_valor_div-dec)/2)
#9 conversion
		dec = el_valor_div - (math.floor(el_valor_div))

		if dec == 0.5:
			binary[6] = 1
			self.yes_no_show.config(text=binary[6])
		if dec == 0.0:
			binary[6] = 0
			self.yes_no_show.config(text=binary[6])
		el_valor_div = ((el_valor_div-dec)/2)
#10 conversion
		dec = el_valor_div - (math.floor(el_valor_div))

		if dec == 0.5:
			binary[5] = 1
			self.yes_no_show.config(text=binary[5])
		if dec == 0.0:
			binary[5] = 0
			self.yes_no_show.config(text=binary[5])
		el_valor_div = ((el_valor_div-dec)/2)
#11 conversion
		dec = el_valor_div - (math.floor(el_valor_div))

		if dec == 0.5:
			binary[4] = 1
			self.yes_no_show.config(text=binary[4])
		if dec == 0.0:
			binary[4] = 0
			self.yes_no_show.config(text=binary[4])
		el_valor_div = ((el_valor_div-dec)/2)
#12 conversion
		dec = el_valor_div - (math.floor(el_valor_div))

		if dec == 0.5:
			binary[3] = 1
			self.yes_no_show.config(text=binary[3])
		if dec == 0.0:
			binary[3] = 0
			self.yes_no_show.config(text=binary[3])
		el_valor_div = ((el_valor_div-dec)/2)
#13 conversion
		dec = el_valor_div - (math.floor(el_valor_div))

		if dec == 0.5:
			binary[2] = 1
			self.yes_no_show.config(text=binary[2])
		if dec == 0.0:
			binary[2] = 0
			self.yes_no_show.config(text=binary[2])
		el_valor_div = ((el_valor_div-dec)/2)
#14 conversion
		dec = el_valor_div - (math.floor(el_valor_div))

		if dec == 0.5:
			binary[1] = 1
			self.yes_no_show.config(text=binary[1])
		if dec == 0.0:
			binary[1] = 0
			self.yes_no_show.config(text=binary[1])
		el_valor_div = ((el_valor_div-dec)/2)

#15 conversion
		dec = el_valor_div - (math.floor(el_valor_div))

		if dec == 0.5:
			binary[0] = 1
			self.yes_no_show.config(text=binary[0])
		if dec == 0.0:
			binary[0] = 0
			self.yes_no_show.config(text=binary[0])


		self.binario_show.config(text = "Dec/Bin: " + str(binary))

		

		self.ventMain.after(100,self.Actualizar)	


def main(args):
	root = Tk()
	aplicacion = app(root)
	root.mainloop()
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
