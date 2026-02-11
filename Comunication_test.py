import sys
from tkinter import *
import pymodbus
from pymodbus.client import ModbusTcpClient

class C_plc():
	def __init__(self,host,port):
		self.host = host
		self.port = port
		self.PLC= ModbusTcpClient(host=self.host, port = self.port)
  
	def botones(self,num):
		PLC= ModbusTcpClient(host='192.168.100.16', port = 502 )
		memo = 24
		#partir
		if num == 1:
			if PLC.connect():
				PLC.write_register(memo,10) #memori 24 set 10
		#reconocer
		if num == 2:
			if PLC.connect():
				PLC.write_register(memo,20) #memori 24 set 20
		# #pararlocal
		if num == 3:
			if PLC.connect():
				PLC.write_register(memo,30) #memori 24 set 30
		# #pararremoto
		if num == 4:
			if PLC.connect():
				PLC.write_register(memo,40) #memori 24 set 40

	def leerAnalogo(self,desde,cantidad):
		datos = None
		if self.PLC.connect():
			respuesta = self.PLC.read_holding_registers(address=desde,count=cantidad) ###
			registro = respuesta.registers[0:]
			datos = registro
		return datos

	def escribir_analog(self,inicio,lista):
		if self.PLC.connect():
			self.PLC.write_registers(address=inicio,values=lista) ### revisar

##### DISCRETOS
	def leerCoil(self):
		respuesta = None
		if self.PLC.connect():
			respuesta = self.PLC.read_coils(address=0,count=20) #cantidad de bits (coils)
			bits = respuesta.bits[0:]
			return bits

	def escribirCoil(self,prim,value):
		if self.PLC.connect():
			self.PLC.write_coil(prim,value)
	