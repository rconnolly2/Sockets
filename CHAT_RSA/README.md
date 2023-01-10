
# Chat RSA en Area Local


Este código es una simple prueba de un chat entre dos ordenadores dentro de una red de área local con 
[Criptografía asimétrica](https://es.wikipedia.org/wiki/Criptograf%C3%ADa_asim%C3%A9trica). Cada mensaje esta encriptado con el algoritmo RSA y enviado en paquetes TCP muy parecido a como funciona WhatsApp.

Este programa utiliza el formato PEM para la encriptacion RSA, diferencia entre diferentes formatos:
![diferenciaPEMVSDER](https://i.stack.imgur.com/Ku0lg.png)



## Como utilizar el script

Primero al ejecutar el script te preguntara si quieres ser host o cliente
(1 para host y 2 para cliente):
```bash
  Quieres ser host? pon 1 o cliente pon 2: 1
```
Ahora te preguntara tu IP de esta maquina:
```bash
  Dame la IP de la maquina que te quieres conectar dentro de tu red: EJ: 192.168.1.101
```
######################################################################################################

Ahora en otro ordenador o maquina virtual dentro de la red local ejecuta el script otra vez y selecciona cliente (2):
```bash
  Quieres ser host? pon 1 o cliente pon 2: 2
```
Ahora pon la IP del ordenador anterior en tu red local:
```bash
  Dame la IP de la maquina que te quieres conectar dentro de tu red: EJ: 192.168.1.101
```
## 💻Requisitos
Este programa solo necesita instalar un libreria ya que las librerias para crear hilos y enviar paquetes ya estan incluidas por defecto con python.
Una vez que tengas la ventana de terminal abierta y instalado pip, escribe el 
siguiente comando para instalar RSA:


```bash
  pip install rsa
```

## 📕Librerias utilizadas

**threading:** Para crear hilos dentro de python

**sockets:** Para enviar paquetes tcp en python

**rsa:** Para poder utilizar el algoritmo rsa

