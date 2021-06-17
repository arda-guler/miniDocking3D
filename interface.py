from OpenGL.GL import *
from OpenGL.GLU import *

def warn_f_abs(value, limit):
    
    # state -1: out of limits
    # state  1: nearly out of limits
    # state  0: OK
    
    if abs(value) > limit:
        return -1
    elif abs(value) < limit and abs(value) > limit * 0.8:
        return 1
    else:
        return 0

# functions to draw command visual feedbacks
def Autopilot():
    glColor(1.0, 0.5, 1.0)
    glBegin(GL_LINES)
    glVertex3f(-4.0, 3.7, -10.0)
    glVertex3f(-3.7, 3.7, -10.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-3.85, 3.85, -10.0)
    glVertex3f(-4.2, 3.5, -10.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-3.85, 3.85, -10.0)
    glVertex3f(-3.5, 3.5, -10.0)
    glEnd()

def UpArrow(vel_y, vel_lateral_tolerance):
    
    if warn_f_abs(vel_y, vel_lateral_tolerance) == 0:
        glColor(0.1, 1.0, 0.1)
    elif warn_f_abs(vel_y, vel_lateral_tolerance) == -1:
        glColor(1.0, 0.0, 0.0)
    else:
        glColor(0.5, 0.5, 0.0)
    
    glBegin(GL_LINES)
    glVertex3f(2.0, 2.0, -10.0)
    glVertex3f(0.0, 3.5, -10.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-2.0, 2.0, -10.0)
    glVertex3f(0.0, 3.5, -10.0)
    glEnd()

def DownArrow(vel_y, vel_lateral_tolerance):
    
    if warn_f_abs(vel_y, vel_lateral_tolerance) == 0:
        glColor(0.1, 1.0, 0.1)
    elif warn_f_abs(vel_y, vel_lateral_tolerance) == -1:
        glColor(1.0, 0.0, 0.0)
    else:
        glColor(0.5, 0.5, 0.0)
    
    glBegin(GL_LINES)
    glVertex3f(2.0, -2.0, -10.0)
    glVertex3f(0.0, -3.5, -10.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-2.0, -2.0, -10.0)
    glVertex3f(0.0, -3.5, -10.0)
    glEnd()

def RightArrow(vel_x, vel_lateral_tolerance):
    
    if warn_f_abs(vel_x, vel_lateral_tolerance) == 0:
        glColor(0.1, 1.0, 0.1)
    elif warn_f_abs(vel_x, vel_lateral_tolerance) == -1:
        glColor(1.0, 0.0, 0.0)
    else:
        glColor(0.5, 0.5, 0.0)
    
    glBegin(GL_LINES)
    glVertex3f(4.0, 0.0, -10.0)
    glVertex3f(2.5, -2.0, -10.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(4.0, 0.0, -10.0)
    glVertex3f(2.5, 2.0, -10.0)
    glEnd()

def LeftArrow(vel_x, vel_lateral_tolerance):
    
    if warn_f_abs(vel_x, vel_lateral_tolerance) == 0:
        glColor(0.1, 1.0, 0.1)
    elif warn_f_abs(vel_x, vel_lateral_tolerance) == -1:
        glColor(1.0, 0.0, 0.0)
    else:
        glColor(0.5, 0.5, 0.0)
    
    glBegin(GL_LINES)
    glVertex3f(-4.0, 0.0, -10.0)
    glVertex3f(-2.5, -2.0, -10.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-4.0, 0.0, -10.0)
    glVertex3f(-2.5, 2.0, -10.0)
    glEnd()

def BackwardArrow(vel_z, vel_direct_tolerance):

    if vel_z >= 0:
        if warn_f_abs(vel_z, vel_direct_tolerance) == 0:
            glColor(0.1, 1.0, 0.1)
        elif warn_f_abs(vel_z, vel_direct_tolerance) == -1:
            glColor(1.0, 0.0, 0.0)
        else:
            glColor(0.5, 0.5, 0.0)
    else:
        glColor(0.1, 1.0, 0.1)
    
    # top right
    glBegin(GL_LINES)
    glVertex3f(4.0, 4.0, -10.0)
    glVertex3f(2.0, 4.0, -10.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(4.0, 4.0, -10.0)
    glVertex3f(4.0, 2.0, -10.0)
    glEnd()

    # top left
    glBegin(GL_LINES)
    glVertex3f(-4.0, 4.0, -10.0)
    glVertex3f(-2.0, 4.0, -10.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-4.0, 4.0, -10.0)
    glVertex3f(-4.0, 2.0, -10.0)
    glEnd()

    # bottom right
    glBegin(GL_LINES)
    glVertex3f(4.0, -4.0, -10.0)
    glVertex3f(2.0, -4.0, -10.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(4.0, -4.0, -10.0)
    glVertex3f(4.0, -2.0, -10.0)
    glEnd()

    # bottom left
    glBegin(GL_LINES)
    glVertex3f(-4.0, -4.0, -10.0)
    glVertex3f(-2.0, -4.0, -10.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-4.0, -4.0, -10.0)
    glVertex3f(-4.0, -2.0, -10.0)
    glEnd()

def ForwardArrow(vel_z, vel_direct_tolerance):
    
    if vel_z >= 0:
        if warn_f_abs(vel_z, vel_direct_tolerance) == 0:
            glColor(0.1, 1.0, 0.1)
        elif warn_f_abs(vel_z, vel_direct_tolerance) == -1:
            glColor(1.0, 0.0, 0.0)
        else:
            glColor(0.5, 0.5, 0.0)
    else:
        glColor(0.1, 1.0, 0.1)
    
    # top right
    glBegin(GL_LINES)
    glVertex3f(2.0, 4.0, -10.0)
    glVertex3f(2.0, 2.0, -10.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(2.0, 2.0, -10.0)
    glVertex3f(4.0, 2.0, -10.0)
    glEnd()

    # top left
    glBegin(GL_LINES)
    glVertex3f(-2.0, 4.0, -10.0)
    glVertex3f(-2.0, 2.0, -10.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-2.0, 2.0, -10.0)
    glVertex3f(-4.0, 2.0, -10.0)
    glEnd()

    # bottom right
    glBegin(GL_LINES)
    glVertex3f(2.0, -4.0, -10.0)
    glVertex3f(2.0, -2.0, -10.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(2.0, -2.0, -10.0)
    glVertex3f(4.0, -2.0, -10.0)
    glEnd()

    # bottom left
    glBegin(GL_LINES)
    glVertex3f(-2.0, -4.0, -10.0)
    glVertex3f(-2.0, -2.0, -10.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-2.0, -2.0, -10.0)
    glVertex3f(-4.0, -2.0, -10.0)
    glEnd()

def Crosshair(ship_trans, pos_lateral_tolerance):

    if warn_f_abs(ship_trans[0], pos_lateral_tolerance) == 0:
        glColor(0.0, 1.0, 1.0)
    elif warn_f_abs(ship_trans[0], pos_lateral_tolerance) == -1:
        glColor(1.0, 0.2, 0.2)
    else:
        glColor(0.5, 0.5, 0.0)
    
    glBegin(GL_LINES)
    glVertex3f(0.0, -4.0, -10.0)
    glVertex3f(0.0, 4.0, -10.0)
    glEnd()

    if warn_f_abs(ship_trans[1], pos_lateral_tolerance) == 0:
        glColor(0.0, 1.0, 1.0)
    elif warn_f_abs(ship_trans[1], pos_lateral_tolerance) == -1:
        glColor(1.0, 0.2, 0.2)
    else:
        glColor(0.5, 0.5, 0.0)

    glBegin(GL_LINES)
    glVertex3f(4.0, 0.0, -10.0)
    glVertex3f(-4.0, 0.0, -10.0)
    glEnd()

