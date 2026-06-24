from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# broadcast_channel=1 → envia ultrassônico pro Hub 1
# observe_channels=[2] → recebe inclinação do Hub 1
hub = PrimeHub(broadcast_channel=1, observe_channels=[2])

ultra = UltrasonicSensor(Port.B)
motor = Motor(Port.A)

em_rampa = False

while True:

    # =========================
    # ENVIA ULTRASSÔNICO
    # =========================

    distancia = ultra.distance()

    if distancia <= 60:
        hub.ble.broadcast(1)
    else:
        hub.ble.broadcast(0)

    # =========================
    # RECEBE INCLINAÇÃO DO HUB 1
    # =========================

    dados = hub.ble.observe(2)

    if dados is True and not em_rampa:
        em_rampa = True
        motor.run_angle(200, -200)   # gira 2500 graus para frente

    elif dados is False and em_rampa:
        em_rampa = False
        motor.run_angle(200, 200)  # gira 2500 graus para voltar

    wait(20)