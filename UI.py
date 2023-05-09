import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def drawUIText(x, y, font_size, dh, dw, textString):
    font = pygame.font.Font("Fonts/FiraCode-VF.ttf", font_size)
    render = font.render(
        textString, True, (255, 255, 255, 255), (0, 0, 0, 0)).convert_alpha()
    textData = pygame.image.tostring(render, "RGBA", True)
    glWindowPos2d(x, y)
    glDrawPixels(render.get_width(), render.get_height(),
                 GL_RGBA, GL_UNSIGNED_BYTE, textData)
    return render.get_width(), render.get_height()


def drawUI(display):
    frame = 0
    w, h = display.get_size()
    while True:
        print("Frame " + frame.__str__())
        glViewport(0, int(h / 4), int(w / 2),
                   int((h / 2) - 30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == VIDEOEXPOSE:
                print("Exposed!")
            elif event.type == VIDEORESIZE:
                print("Resized!")
                glLoadIdentity()
                try:
                    w, h = event.dict['size']
                except:
                    print("Failed to find event.dict['size']")
                    w, h = display.get_size()
                gluPerspective(45, (w / (h - 30)), 0.1, 50.0)
                glTranslatef(0.0, 0.0, -5)

        print("Screen: w = " + w.__str__() + ", h = " + h.__str__())
        t1w, t1h = drawUIText(
            w/2, h - 30, 16, h, w, "Frame " + frame.__str__())
        t2w, t2h = drawUIText(
            w/2, h - (30 + t1h), 16, h, w, "Head Speed: 0 m/s.")
        t3w, t3h = drawUIText(
            w/2, h - (30 + t1h + t2h), 16, h, w, "Extrusion Speed: 0 m/s.")
        t4w, t4h = drawUIText(
            w/2, h - (30 + t1h + t2h + t3h), 16, h, w, "Extruded Length: 100 m.")
        pygame.display.flip()
        frame += 1
        pygame.time.wait(10)
