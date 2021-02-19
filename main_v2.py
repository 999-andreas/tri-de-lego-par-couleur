#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# déclaration des variables et objets
ev3 = EV3Brick()
bouton=TouchSensor(Port.S1)
capteur_couleur=ColorSensor(Port.S2)

moteur_pince=Motor(Port.A)
moteur_tapisroulant=Motor(Port.B)

nb_legos=0


# \\programme//

print(capteur_couleur.color())

# on s'assure que la machine soit bien à la position d'origine 
if bouton.pressed() : 
    moteur_tapisroulant.reset_angle(0)

    print("début du tri")
# la machine marchera tant que le capteur verra pas du noir
# càd lorsqu'il n'y a plus de lego dans la pile
    while capteur_couleur.color() != Color.BLACK :
        

# chaque couleur de lego se voit assigner une 'case' les instructions moteur suivante envoie les legos dans leur case  
        if capteur_couleur.color() == Color.RED : 
            moteur_tapisroulant.run_target(500, 10)
            
        elif capteur_couleur.color() == Color.BLUE :
            moteur_tapisroulant.run_target(500, 132)
             
        elif capteur_couleur.color() == Color.GREEN : 
            moteur_tapisroulant.run_target(500, 360)
        
        elif capteur_couleur.color() == Color.YELLOW : 
            moteur_tapisroulant.run_target(500, 530)

# on garde dans une variable le nombre de lego totale passé dans la machine   
        nb_legos+=1

# consigne pour lacher lego
        moteur_pince.run_angle(1500,-180)
        moteur_pince.run_angle(1500, 180)
        

# consigne pour que le moteur revienne a la position initiale càd lorsqu'il touche le bouton 
        while not bouton.pressed() :
            moteur_tapisroulant.run(-500)
        moteur_tapisroulant.stop()
        wait(500)
        moteur_tapisroulant.reset_angle(0)
        print("fin du tri")
        print(nb_legos,"lego.s sont passés dans la machine")
