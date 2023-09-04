import sys

def obtener_direccion_broadcast(direccion_ip, mascara_cidr):
    octetos = direccion_ip.split(".")
    octetos_binarios = ""
    for octeto in octetos:
        octetos_binarios += bin(int(octeto))[2:].zfill(8)

    mascara_binaria = "1" * mascara_cidr + "0" * (32 - mascara_cidr)

    broadcast_binario = ""
    for bit1, bit2 in zip(octetos_binarios, mascara_binaria):
        broadcast_binario += str(int(bit1) or int(bit2))

    broadcast = ""
    for i in range(0, 32, 8):
        broadcast += str(int(broadcast_binario[i:i+8], 2))
        if (i < 24):
            broadcast += "."

    return broadcast

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pregunta1.py <direccion_ip> <mascara_cidr>")
        sys.exit(1)

    direccion_ip = sys.argv[1]
    mascara_cidr = int(sys.argv[2])

    broadcast = obtener_direccion_broadcast(direccion_ip, mascara_cidr)

    print("Dirección IP: ", direccion_ip)
    print("Máscara de subred en notación CIDR: ", mascara_cidr)
    print("Dirección de Broadcast: ", broadcast)