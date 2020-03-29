import tkinter as tk
from tkinter import *
import time
import pyautogui
import serial
import numpy

count = 0
s = 300
r = s//6
after_id = None

height = 200
width = 500
offset = 100

#constants for bar graph
emotions = ["anger", "joy", "surprise", "sorrow", "neutral"]
colors = ["red", "pink", "yellow", "blue", "gray"]
bars = [0 for i in range(5)]
firsttime = True

def bargraphsetup():
    c.create_text(50, 280, text = "Anger")
    c.create_text(170, 280, text = "Joy")
    c.create_text(290, 280, text = "Surprise")
    c.create_text(430, 280, text = "Sorrow")
    c.create_text(560, 280, text = "Neutral")

    c.create_rectangle(35, 230, 65, 260, fill = colors[0])
    c.create_rectangle(155, 230, 185, 260, fill = colors[1])
    c.create_rectangle(275, 230, 305, 260, fill = colors[2])
    c.create_rectangle(415, 230, 445, 260, fill = colors[3])
    c.create_rectangle(545, 230, 575, 260, fill = colors[4])

    c.create_text(offset + 200, offset/2, text = "Live-Updating Mood Meter")
    
    #c.create_line(offset, height + offset, offset, offset)
    #c.create_line(offset, height + offset, width + offset, height + offset)
    #create_text(1.5*offset + width//2, height + 1.5*offset, text = 'Emotions')
    #c.create_text(.3*offset, offset + .5*height, text = 'Percent')

    #for i in range(5):
    #    c.create_text(.8*offset, height + offset - height//4*i, text = '' + str(100/4*i) + '%')
    #    c.create_text((2*i + 1.5)*width//10 + offset, height + 1.2 * offset, text = emotions[i])

def bargraph(data):
    global firsttime
    if not firsttime:
        [c.delete(bars[i]) for i in range(5)]
    else:
        firsttime = False

    cumulative_length = 0
    for i in range(5):
        length = 325 * data[i]
        x1 = offset + cumulative_length
        y1 = offset
        x2 = offset + x1 + length
        y2 = offset + 50
        cumulative_length += length
        bars[i] = c.create_rectangle(x1,y1,x2,y2,fill = colors[i])

    #for i in range(5):
    #    h = height * data[i]
    #    bars[i] = c.create_rectangle((2*i + 1)*width//10 + offset, height + offset, (2*i+2) * width//10 + offset, height + offset - h, fill = colors[i], outline = '')

def start():
    global running
    button['text'] = 'Stop'
    button['command'] = stop
    print("Start")
    takeScreenshot()

def takeScreenshot():
    global count
    global after_id
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('C:/Users/Jonathan Ko/Documents/Hackathons/LAHacks/screenshot.png')
    count = count +1
    data = detect_faces('screenshot.png')
    print(data)
    bargraph(data)  
    sendNumber(data)
    after_id = t.after(500, takeScreenshot)

def stop():
    global after_id
    if after_id:
        t.after_cancel(after_id)
        after_id = None
        print ("Stop")
        button['text'] = 'Start'
        button['command'] = start


def detect_faces(path):
    """Detects faces in an image."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    #unknown, very unlikely, unlikely, possible, likely, very likely
    #print('Faces:')

    values = [0 for i in range(5)]
    weighted_values = [0, 0, 0.25, 0.5, 0.75, 1]

    for face in faces:
        values[0] = values[0] + weighted_values[face.anger_likelihood] * face.detection_confidence
        values[1] = values[1] + weighted_values[face.joy_likelihood] * face.detection_confidence
        values[2] = values[2] + weighted_values[face.surprise_likelihood] * face.detection_confidence
        values[3] = values[3] + weighted_values[face.sorrow_likelihood] * face.detection_confidence
        if face.anger_likelihood + face.joy_likelihood + face.surprise_likelihood + face.sorrow_likelihood == 4:
            values[4] = values[4] + face.detection_confidence
    total = 0
    for val in values:
        total += val

    if total == 0:
        total = 1

    values = [values[i] / total for i in range(len(values))]

   

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return values

def sendNumber(data):
    total = 0
    for i in range(len(data)):
        if data[i] == numpy.amax(data):
            total = i + 1
            break
    arduino.write(str.encode(str(total)))
    return

t = tk.Tk()
t.geometry(str(width + 2 * offset)+'x'+str(height + offset*2))  
t.title('Mood Meter') 
button = tk.Button(height = 1,text = 'Start', fg = "black", command = start) 
button.pack()
c = Canvas(t, width=width + 100, height=height + offset*2)
c.pack()
bargraphsetup()

#emotions = ["anger", "joy", "surprise", "sorrow", "neutral"]
#colors = ["red", "pink", "yellow", "blue", "gray"]

# c = Canvas(t, width=width + 100, height=height + offset*2)
# c.pack()

# c.create_line(offset, height + offset, offset, offset)
# c.create_line(offset, height + offset, width + offset, height + offset)
# c.create_text(1.5*offset + width//2, height + 1.5*offset, text = 'Emotions')
# c.create_text(.3*offset, offset + .5*height, text = 'Percent')

# for i in range(5):
#     c.create_text(.8*offset, height + offset - height//4*i, text = '' + str(100/4*i) + '%')

# for i in range(5):
#     c.create_text((2*i + 1.5)*width//10 + offset, height + 1.2 * offset, text = emotions[i])
#     h = height * sample[i]
#     c.create_rectangle((2*i + 1)*width//10 + offset, height + offset, (2*i+2) * width//10 + offset, height + offset - h, fill = colors[i], outline = '')


t.mainloop()
