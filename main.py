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
capteur_couleur=ColorSensor(Port.S4)
couleurs_legos=[]
chrono=StopWatch

# \\Programme//

def comptage(couleurs_legos) : 
# compte le nombre d'éléments passant par la machine et noter les couleur respective de chaque lego 
# on pourrait se passer de la variable nb_lego mais elle permet de confirmer le nombre de legos à l'utilisateur
    nb_lego=0
    ev3.speaker.beep()
    for comptage in range(8) :
        print("montrer le lego")
        wait(5000) 
        if capteur_couleur.color() != None :
            couleurs_legos.append(capteur_couleur.color())
            nb_lego=comptage+1
            print("couleur analysé")
        else :
            print("il y a : ",nb_lego,"legos")
            ev3.speaker.beep()
            return nb_lego
               
    print("il y a : 8 legos (c'est le maximum accepte)")
    ev3.speaker.beep()
    return nb_lego

def case1() : 
# les instructions moteur pour emener le legos à la case1
def case2() : 
# les instructions moteur pour emener le legos à la case2
def case3() : 
# les instructions moteur pour emener le legos à la case3

def tri_par_couleur(comptage()) :
# coeur du programme, envoie les legos dans la case corespondant à leur couleur 
    case_rangement=[]
    nb_legos = comptage()
    for k in range(nb_legos-1) : 
        if couleurs_legos[k] = RED : 
            case1() 
        elif couleurs_legos[k] = BLUE : 
            case2() 
        elif couleurs_legos[k] = GREEN : 
            case3()



def main() : 

    if bouton.pressed()==True :
        ev3.speaker.beep()
        comptage() 

main()