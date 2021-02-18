
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
capteur_couleur=ColorSensor(Port.S3)

moteur_pince=Motor(Port.A)
moteur_tapisroulant=Motor(Port.D)

nb_legos=0




# \\programme//


# on s'assure que le truc soit bien à position d'origine 
if bouton.pressed() == True : 

# la machine marchera tant que le capteur verra du [insérer la couleur qu'il détecte si il n'y pas de lego] càd lorsqu'il n'y a plus de lego dans la liste
    while capteur_couleur.color() != None :

        print("début du tri")
# chaque couleur de lego se voit assigner une 'case' les instructions moteur suivante envoie les legos dans leur case  
        if capteur_couleur.color() == Color.RED : 
            moteur_tapisroulant.run_time(300,200)
            moteur_pince.run_time(200,100) 
        elif capteur_couleur.color() == Color.BLUE :
            moteur_tapisroulant.run_time(300,200)
            moteur_pince.run_time(200,100) 
        elif capteur_couleur.color() == Color.GREEN : 
            moteur_tapisroulant.run_time(300,200)
            moteur_pince.run_time(200,100)
        nb_legos+=1

# consigne pour remettre la pince à sa place 
        moteur_pince.run_until_stalled(120, duty_limit=50)

# consigne pour que le moteur revienne a la position initiale càd lorsqu'il touche le bouton 
        while bouton.pressed != True :
            moteur_tapis_roulant.#roule

    print("le tri est fini")
    print(nb_lego,"legos sont passés dans la machine")
