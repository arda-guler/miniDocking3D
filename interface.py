from OpenGL.GL import *
from OpenGL.GLU import *
from sound import *

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

# alerts
def SpeedAlert(time_to_alert, max_speed, ship_speed, dist):
    if not ship_speed == 0:
        if ship_speed > max_speed * 100 and dist/ship_speed < time_to_alert and not getChannelBusy(2):
            playSfx("alert_speed", channel=2)

def TargetAlert(time_to_alert, pos_x, pos_y, vel_x, vel_y, lateral_tolerance, ship_speed, dist):
    if not ship_speed == 0:
        if (dist/ship_speed < time_to_alert and not getChannelBusy(5) and ship_speed > 0 and
            ((abs(pos_x) > lateral_tolerance or abs(pos_y) > lateral_tolerance) or
            vel_x * (dist/ship_speed) + pos_x > lateral_tolerance * 2 or vel_x * (dist/ship_speed) + pos_x < -lateral_tolerance * 2 or
            vel_y * (dist/ship_speed) + pos_y > lateral_tolerance * 2 or vel_y * (dist/ship_speed) + pos_y < -lateral_tolerance * 2)):
            
            playSfx("alert_target", channel=5)

