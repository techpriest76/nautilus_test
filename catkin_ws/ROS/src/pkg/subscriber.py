#!/usr/bin/env python3

#Um robô possui um sensor de velocidade que fornece os vetores de velocidade linear e angular com suas
#componentes x, y e z.
#Crie um pacote contendo um publisher que publica esses dados e um subscriber que escuta esse tópico,
#calcula o módulo dos vetores e publica os resultados em tópicos separados.
#Observações:
#● Utilize as mensagens mais apropriadas para cada um dos tópicos;
#● Os dados do sensor podem ser gerados aleatoriamente no publisher;
#● Disponibilize todo o pacote como um repositório em seu GitHub.

import rospy
from geometry_msgs.msg import Vector3
from std_msgs.msg import Float32

class Listener():
    def __init__(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber('coordenadas_linear', Vector3, self.callback1)
        rospy.Subscriber('coordenadas_angular',Vector3, self.callback2)
        self.pub1=rospy.Publisher('modulo_linear',Float32,queue_size=10)
        self.pub2=rospy.Publisher('modulo_angular',Float32,queue_size=10)

    def callback1(self,msg):
        print('vetor de velocidade linear:')
        print('publicado no topico "modulo_linear"')
        x,y,z=msg.x,msg.y,msg.z
        modulo_linear=((x**2)+(y**2)+(z**2))**0.5
        f=Float32()
        f.data=modulo_linear
        rospy.loginfo(f)
        self.pub1.publish(f)

    def callback2(self,msg):
        print('vetor de velocidade angular: ')
        print('publicado no topico "modulo_angular')
        x,y,z=msg.x,msg.y,msg.z
        modulo_angular=((x**2)+(y**2)+(z**2))**0.5
        f=Float32()
        f.data=modulo_angular
        rospy.loginfo(f)
        self.pub2.publish(f)
        print(' ')
  
if __name__=='__main__':
    print('As coordenadas iniciais para para vetor sao de 0,0,0')
    l=Listener()
    rospy.spin()
