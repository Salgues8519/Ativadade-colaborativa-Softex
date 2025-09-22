from abc import ABC, abstractmethod

class VeiculoMotorizado(ABC):
    def __init__(self, motor, placa, velocidade):
        self.motor = motor
        self.placa = placa
        self. velocidade = velocidade
    
    @abstractmethod
    def ligar_motor(self):
        pass

    @abstractmethod
    def acelerar(self):
        pass

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        self.__ligado = False
    
    def ligar(self):
        self.__ligado = True
        return f"Motor {self.tipo} está ligado"
    
    def get_status(self):
        if self.__ligado == True:
            return "Ligado"
        else:
            return "Desligado"
    
    def desligar(self):
        self.__ligado = False
        return f"Motor {self.tipo} está desligado"

class Carro(VeiculoMotorizado):
    def __init__(self, motor, placa, velocidade, marca, modelo):
        super().__init__(motor, placa, velocidade)
        self.marca = marca
        self.modelo = modelo

    def ligar_motor(self):
        if self.velocidade == 0 and self.motor.get_status() == "Desligado":
            return self.motor.ligar()
        else:
            return "Carro já está ligado"
    
    def acelerar(self):
        if self.motor.get_status() == "Ligado":
            self.velocidade += 10
            print(f"O {self.modelo} está acelerando em 10km")
        else:
            raise Exception("Erro: O motor precisa estar ligado para acelerar.")
    
    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 5
            print("O carro diminuiu em 5km")
        else:
            print(f"A velocidade do {self.modelo} já é zero")

    def desligar(self):
        if self.velocidade == 0 and self.motor.get_status() == "Ligado":
            self.motor.desligar()
        else:
            print(f"{self.modelo} precisa estar parado e ligado para ser desligado")


class Moto(VeiculoMotorizado):
    def __init__(self, motor, placa, velocidade, marca, modelo):
        super().__init__(motor, placa, velocidade)
        self.marca = marca
        self.modelo = modelo

    def ligar_motor(self):
        if self.velocidade == 0 and self.motor.get_status() == "Desligado":
            return self.motor.ligar()
        else:
            return "Moto já está ligado"
    
    def acelerar(self):
        if self.motor.get_status() == "Ligado":
            return f"O {self.modelo} está acelerando"
        else:
            raise Exception("Erro: O motor precisa estar ligado para acelerar.")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 5
            print("O carro diminuiu em 5km")
        else:
            print(f"A velocidade do {self.modelo} já é zero")

    def desligar(self):
        if self.velocidade == 0 and self.motor.get_status() == "Ligado":
            self.motor.desligar()
        else:
            print(f"{self.modelo} precisa estar parado e ligado para ser desligado")