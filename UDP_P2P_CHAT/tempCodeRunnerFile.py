      mi_mensaje = (str(mipuerto) + " Dice: " + str(mensaje))
            mi_mensaje = mi_mensaje.encode("utf-8")
            for puerto in lista_puertos:
                # Enviamos este mensaje a TODOS los puertos de nuestra lista de clientes conocidos
                socket.sendto(mi_mensaje, ("192.168.1.101", puerto))