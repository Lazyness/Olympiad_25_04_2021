from constants import videoWriter, img, divace_texture, printfile

def video_write(x,y):
    im = drow(img.copy(),getdots(x,y))
    videoWriter.write(im)

def drow(image,dots):
    for dot in dots:
        if dot[0] >= 0 and dot[1] >= 0 and dot[0] < 1280 and dot[1] < 400:
            image[dot[1]][dot[0]] = dot[2]
    return image


def getdots(x,y):
    dots = []
    for linei in range(len(divace_texture)):
        for doti in range(len(divace_texture[linei])):
            xl = 4 - doti + int(x)
            yl = 4 - linei + int(y)
            color = divace_texture[linei][doti]
            dot = [xl,yl,color]
           
            if color != None:
                dots.append(dot)
    
    return dots

def outputf(message):
    my_file = open(printfile, 'r')
    r = my_file.read()
    my_file = open(printfile, 'w')
    message = r + message
    my_file.write(message)
    
    my_file.close()



def video_reliase():
    videoWriter.release()