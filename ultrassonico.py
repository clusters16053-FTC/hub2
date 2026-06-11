from pybricks.hubs import PrimeHub
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Hub transmissor
hub = PrimeHub(broadcast_channel=1)

# Troque a porta se necessário
ultra = UltrasonicSensor(Port.A)

while True:

    distancia = ultra.distance()

    # 15 cm ou menos = obstáculo
    if distancia <= 100:
        hub.ble.broadcast(1)

    # 16 cm ou mais = livre
    else:
        hub.ble.broadcast(0)

    wait(20)