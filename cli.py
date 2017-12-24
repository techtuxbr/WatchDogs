from program import computer
from program import cpu
import sys

params = sys.argv

if len(params) > 1:
    if params[1] == "os" or params[1] == "system":
        print("Sistema operacional: ", computer.os())
        print("Versao: ", computer.osVersion())
    elif params[1] == "name":
        print("Node de rede:", computer.name())
    elif params[1] == "distro":
        print("Distribuicao: ", computer.distro())
    elif params[1] == "processor" or params[1] == "-p":
        if len(params) == 4 and params[2] == "percentage" and int(params[3]) >= 1:
            for x in range(int(params[3])):
                print("Consumindo: ", cpu.percentage().user + cpu.percentage().system, "%")
                print("Livre: ", cpu.percentage().idle,"%")
                print("_________________________")
        else:
            print("Processador: ", computer.cpu())
            print("Velocidade: ", cpu.freq(),"GHz")
            print("Cores: ", cpu.cores())
            print("Cores Fisicos: ", cpu.phyCores())
    elif params[1] == "arc":
        print("Arquitetura da maquina:", computer.arc())
    else:
        print("Parametro desconhecido!")
else:
    print("Sistema operacional: ", computer.os())
