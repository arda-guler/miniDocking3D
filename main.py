import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pywavefront
import random
from os import path, system

from sound import *
from interface import *

ship = pywavefront.Wavefront('data/models/station_new.obj', collect_faces=True)

ship_scale = [1,1,1]
ship_trans = [random.randint(-15,15),random.randint(-15,15),random.randint(-200, -50)]
ship_rot = [0, 0, 0]

initSound()

def read_high_score():
    if path.exists("data/high_score.sav"):
        high_score = open("data/high_score.sav", "r").readlines()[0]
        return "%.1f" % float(high_score)
    else:
        return "High score file not found."

def write_high_score(score):
    high_score_file = open("data/high_score.sav", "a")
    high_score_file.seek(0)
    high_score_file.truncate()
    high_score_file.write(str(score))

def Model():
    glColor(0.0, 0.25, 1.0)
    
    glPushMatrix()

    glTranslatef(ship_trans[0], ship_trans[1], ship_trans[2])
    
    glRotate(ship_rot[0], 1, 0, 0)
    glRotate(ship_rot[1], 0, 1, 0)
    glRotate(ship_rot[2], 0, 0, 1)

    for mesh in ship.mesh_list:
        glBegin(GL_TRIANGLES)
        for face in mesh.faces:
            for vertex_i in face:
                glVertex3f(*ship.vertices[vertex_i])
        glEnd()

    glPopMatrix()

def main():
    global ship_orient

    frame_up_cmd = False
    frame_down_cmd = False
    frame_right_cmd = False
    frame_left_cmd = False
    frame_fwd_cmd = False
    frame_bkd_cmd = False

    draw_crosshair = True
    radar_enabled = True

    autodock = False

    total_commands = 0
    pos_lateral_tolerance = 0.35
    vel_lateral_tolerance = 0.002
    vel_direct_tolerance = 0.01

    #beep_sleep = None
    beep_iterator = 0
    
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.05, 500.0)
    glEnable(GL_CULL_FACE)

    vel = [random.uniform(0.003, -0.003), random.uniform(0.003, -0.003), random.uniform(0.003, -0.003)]
    angle = 0

    ship_rot[0] = 0
    ship_rot[1] = 0
    ship_rot[2] = 0
    
    glTranslate(0, 0, 0)

    try:
        system('cls')
    except:
        pass

    print("Lateral translation by arrow keys. Forwards with PgUp, backwards with PgDn.\nC to toggle crosshair, R to toggle radar beep.\n")
    print("For high score: Maximize targeting accuracy, minimize contact velocity and thruster use.\n\n")
    print("Press A to hand over controls to the autopilot. (Highscores won't count.)\n")

    while True:

        # get keyboard input
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if not autodock:

                    # translation commands
                    if event.key == pygame.K_UP:
                        frame_up_cmd = True
                    if event.key == pygame.K_DOWN:
                        frame_down_cmd = True
                    if event.key == pygame.K_RIGHT:
                        frame_right_cmd = True
                    if event.key == pygame.K_LEFT:
                        frame_left_cmd = True
                    if event.key == pygame.K_PAGEUP:
                        frame_fwd_cmd = True
                    if event.key == pygame.K_PAGEDOWN:
                        frame_bkd_cmd = True

                # interface commands
                if event.key == pygame.K_c:
                    draw_crosshair = not draw_crosshair
                if event.key == pygame.K_r:
                    radar_enabled = not radar_enabled

                # engage autodock
                if event.key == pygame.K_a:
                    autodock = True
                    print("AUTOPILOT ACTIVE\n")

        if autodock:
           
            # x axis
            if abs(ship_trans[0]) <= pos_lateral_tolerance * 0.3:
                if vel[0] >= vel_lateral_tolerance * 0.6:
                    frame_right_cmd = True
                elif vel[0] <= -vel_lateral_tolerance * 0.6:
                    frame_left_cmd = True
            elif ship_trans[0] < 0:
                if vel[0] < vel_lateral_tolerance * 3:
                    frame_left_cmd = True
            elif ship_trans[0] > 0:
                if vel[0] > -vel_lateral_tolerance * 3:
                    frame_right_cmd = True

            # y axis
            if abs(ship_trans[1]) <= pos_lateral_tolerance * 0.3:
                if vel[1] >= vel_lateral_tolerance * 0.6:
                    frame_up_cmd = True
                elif vel[1] <= -vel_lateral_tolerance * 0.6:
                    frame_down_cmd = True
            elif ship_trans[1] < 0:
                if vel[1] < vel_lateral_tolerance * 3:
                    frame_down_cmd = True
            elif ship_trans[1] > 0:
                if vel[1] > -vel_lateral_tolerance * 3:
                    frame_up_cmd = True

            # z axis
            if ship_trans[2] >= -15.0:
                # make sure the ship is aligned before proceeding further than 15 meters
                if abs(ship_trans[0]) <= pos_lateral_tolerance * 0.9 and abs(ship_trans[1]) <= pos_lateral_tolerance * 0.9:
                    if vel[2] < vel_direct_tolerance * 0.75:
                        frame_fwd_cmd = True
                    elif vel[2] > vel_direct_tolerance * 0.9:
                        frame_bkd_cmd = True
                else:
                    if vel[2] > 0:
                        frame_bkd_cmd = True
                    elif vel[2] < -vel_direct_tolerance:
                        frame_fwd_cmd = True
            else:
                if vel[2] < vel_direct_tolerance * 2:
                    frame_fwd_cmd = True
                elif vel[2] > vel_direct_tolerance * 4:
                    frame_bkd_cmd = True


        #print("Pos: %.2f, %.2f, %.2f" % (-ship_trans[0], -ship_trans[1], -ship_trans[2]))

        ship_trans[0] += vel[0]
        ship_trans[1] += vel[1]
        ship_trans[2] += vel[2]

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        if autodock:
            Autopilot()

        # draw space station model
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        Model()

        # give command feedback to user
        if frame_up_cmd:
            vel[1] -= 0.001 + random.uniform(0.0002, -0.0002)
            UpArrow(vel[1], vel_lateral_tolerance)
            frame_up_cmd = False
            playSfx("rcs_burst")
            total_commands += 1

        if frame_down_cmd:
            vel[1] += 0.001 + random.uniform(0.0002, -0.0002)
            DownArrow(vel[1], vel_lateral_tolerance)
            frame_down_cmd = False
            playSfx("rcs_burst")
            total_commands += 1

        if frame_right_cmd:
            vel[0] -= 0.001 + random.uniform(0.0002, -0.0002)
            RightArrow(vel[0], vel_lateral_tolerance)
            frame_right_cmd = False
            playSfx("rcs_burst")
            total_commands += 1

        if frame_left_cmd:
            vel[0] += 0.001 + random.uniform(0.0002, -0.0002)
            LeftArrow(vel[0], vel_lateral_tolerance)
            frame_left_cmd = False
            playSfx("rcs_burst")
            total_commands += 1

        if frame_fwd_cmd:
            vel[2] += 0.001 + random.uniform(0.0002, -0.0002)
            ForwardArrow(vel[2], vel_direct_tolerance)
            frame_fwd_cmd = False
            playSfx("rcs_burst")
            total_commands += 1

        if frame_bkd_cmd:
            vel[2] -= 0.001 + random.uniform(0.0002, -0.0002)
            BackwardArrow(vel[2], vel_direct_tolerance)
            frame_bkd_cmd = False
            playSfx("rcs_burst")
            total_commands += 1

        if draw_crosshair:
            Crosshair(ship_trans, pos_lateral_tolerance)

        if radar_enabled:
            beep_sleep = ((ship_trans[0] ** 2 + ship_trans[1] ** 2 + ship_trans[2] ** 2)**0.5)
            if beep_sleep <= 4.0:
                beep_sleep = 4.0

            if beep_iterator >= beep_sleep:
                playSfx("radar_beep")
                beep_iterator = 0
            else:
                beep_iterator += 1
        else:
            beep_iterator = beep_sleep
            
        # docking position
        if abs(ship_trans[0] - 0) <= pos_lateral_tolerance and abs(ship_trans[1] - 0) <= pos_lateral_tolerance and abs(ship_trans[2] - 0) <= 1:
            if vel[0] <= vel_lateral_tolerance and vel[1] <= vel_lateral_tolerance and vel[2] <= vel_direct_tolerance:
                
                score = (((1 - abs(ship_trans[0] - 0))**2 + (1 - abs(ship_trans[0] - 0))**2)**(0.5)) * 100
                score *= ((1 - abs(vel[0]))**2 + (1 - abs(vel[1]))**2 + (1 - abs(vel[2]))**2) * 100
                score *= 1/(total_commands**0.5)
                
                vel = [0.0, 0.0, 0.0]
                print("\nDOCKING SUCCESS\n")
                if not autodock:
                    print("Score: %.1f" % score)
                else:
                    print("Autodock scored %.1f" % score)
                playSfx("dock")
                print("Previous high score: " + read_high_score())
                if not autodock:
                    if not read_high_score() == "High score file not found.":
                        if float(read_high_score()) < score:
                            print("NEW HIGH SCORE!")
                            write_high_score(score)
                    else:
                        print("NEW HIGH SCORE!")
                        write_high_score(score)
                break
            else:
                print("FAIL - TOO FAST!")
                print(read_high_score())
                playSfx("alert", 2)
                break

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.time.wait(10000)
    pygame.quit()

main()

