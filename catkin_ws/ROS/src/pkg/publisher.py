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
import random

class Talker:
    def __init__(self):
        rospy.init_node('talker',anonymous=True) #padrao
        self.pub1=rospy.Publisher('coordenadas_linear',Vector3,queue_size=10) #a string e o topico(output)
        self.pub2=rospy.Publisher('coordenadas_angular',Vector3,queue_size=10)
        self.list=list(range(20)) #simulacao das cordenaadas do sensor
    
    def linear_vel(self):
        rate=rospy.Rate(1)
        while not rospy.is_shutdown():
            vl1=Vector3()
            vl1.x=random.choice(self.list)
            vl1.y=random.choice(self.list)
            vl1.z=random.choice(self.list)
            rospy.loginfo(vl1)
            self.pub1.publish(vl1)
            
            vl2=Vector3()
            vl2.x=random.choice(self.list)
            vl2.y=random.choice(self.list)
            vl2.z=random.choice(self.list)
            rospy.loginfo(vl2)
            self.pub2.publish(vl2)
            rate.sleep()

            print(' ')

if __name__=='__main__':
    try:
        t=Talker()
        t.linear_vel()
    except rospy.ROSInterruptException:
        print('something went wrong')


