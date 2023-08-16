class Sensor():
    def __init__(self,identificador, un_medida):
        self.identificador = identificador
        self.un_medida = un_medida
        self.temp_atual = 0.0

    def new_temp(self, new_value):
        self.temp_atual = new_value

    def show_read(self):
        print(f'Identificador: {self.identificador}')
        print(f'Temperatura Atual: {self.temp_atual}')

sensor1 = Sensor('Sensor1', 'Celsius')
sensor2 = Sensor('Sensor2', 'Fahrenheit')

sensor1.new_temp(30.2)
sensor2.new_temp(75.2)

print('-----------------------|')
sensor1.show_read()
print('-----------------------|')
sensor2.show_read()