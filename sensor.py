import serial
import time
from csv import writer

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1) 
time.sleep(2)  

archivo = "/var/www/html/sensor_js/data.csv"
a = 0

def adicionar_data(distancia):
    datos = [
        a,  
        str(distancia)]
    with open(archivo, 'w+', newline='') as f:
        csv_writer = writer(f, delimiter=";")
        csv_writer.writerow(datos)

while True:
    distancia = arduino.readline().decode('utf-8').strip()
    if distancia:
        try:
            distancia_valor = float(distancia)
            if 2 <= distancia_valor <= 400:  
                print(f"Distancia: {distancia} cm")
                adicionar_data(distancia)
                a +=1
        except ValueError:
            print("Error al convertir la distancia")
