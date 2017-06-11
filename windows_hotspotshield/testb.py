from PIL import Image, ImageDraw, ImageGrab
import time
from ctypes import windll
import subprocess
import sys
import random
import pyautogui
import requests
def take_screenshot(filename="screenshot_taken_with_python.jpg"):
    '''
    takes screenshot of the window and saves it in to current directory.
    Takes input as a file name
    '''
    # this is a workaround that makes python to take screenshot of whole screen
    user32 = windll.user32
    user32.SetProcessDPIAware()
    # end of workaround
    img = ImageGrab.grab()
    img.save(filename)

def start_hotspot_shield_app():
    path_to_the_app = 'C:\\Program Files (x86)\\Hotspot Shield\\bin\\hsscp.exe'
    subprocess.call([path_to_the_app])

def diff(a, b):
    return sum((a - b) ** 2 for a, b in zip(a, b))

def find_button_position():
    # opening images
    d_im = Image.open("discon_icon.png")
    sb_im = Image.open("before_vpn.png")
    d_im_size = d_im.size
    sb_im_size = sb_im.size
    print d_im_size
    print sb_im_size

    # getting middle pixel of an image:
    x0, y0 = d_im_size[0]//2, d_im_size[1]//2
    # this will return tuple: (255, 97, 97, 255)
    # from this tuple we need first 3 that are RGB parameters of image
    pixel = d_im.getpixel((x0, y0))[:-1]
    print "asdf", x0, y0
    print pixel
    # loop through x axis pixels
    best = (100000, 0, 0)
    icon_squared = 36*33
    count = 0
    max_count = 0

    for x in xrange(sb_im_size[0]):
        for y in xrange(sb_im_size[1]):
            ipixel = sb_im.getpixel((x, y))
            # print "got pixel RGB: {} for pixel:({}, {})".format(ipixel, x, y)
            if ipixel == pixel:
                count += 1
                # print "boooyaa: {}".format(count)
                # if count == icon_squared -5:
                    # print "found square"
            elif count !=0 and max_count<count:
                max_count = count
                max_x = x
                max_y = y
                # draw.rectangle((x - 5, y - 5, x + 5, y + 5), outline='black')
                # print "Current count: {}. Maximum count: {}. Pos = {} {}. Reassigning to 0".format(count, max_count, x, y)
                count = 0
            # d = diff(ipixel, pixel)
            # if d < best[0]:
            #     best = (d, x, y)
    draw = ImageDraw.Draw(sb_im)
    draw.rectangle((max_x - x0, max_y - y0, max_x + x0, max_y + y0), outline='yellow')
    # draw.rectangle((max_x - 16, max_y - 16, max_x + 1, max_y + 1), outline='yellow')
    sb_im.save("found_on_screeshot.png")
    return max_x-x0, max_y-y0
    # draw = ImageDraw.Draw(sb_im)
    # x, y = best[1:]

    # draw.rectangle((842 - 5, 180-5, 842+5, 180+5), outline='black')
    # sb_im.save("found_on_screeshot.png")


def find_image():
    im, pattern, samples = sys.argv[1:]
    samples = int(samples)

    im = Image.open(im)
    walnut = Image.open(pattern)
    pixels = []
    while len(pixels) < samples:
        x = random.randint(0, walnut.size[0] - 1)
        y = random.randint(0, walnut.size[1] - 1)
        pixel = walnut.getpixel((x, y))
        if pixel[-1] > 200:
            pixels.append(((x, y), pixel[:-1]))

    def diff(a, b):
        return sum((a - b) ** 2 for a, b in zip(a, b))

    best = []

    for x in range(im.size[0]):
        for y in range(im.size[1]):
            d = 0
            for coor, pixel in pixels:
                try:
                    ipixel = im.getpixel((x + coor[0], y + coor[1]))
                    d += diff(ipixel, pixel)
                except IndexError:
                    d += 256 ** 2 * 3
            best.append((d, x, y))
            best.sort(key=lambda x: x[0])
            best = best[:3]

    draw = ImageDraw.Draw(im)
    for best in best:
        x, y = best[1:]
        draw.rectangle((x, y, x + walnut.size[0], y + walnut.size[1]), outline='yellow')
    im.save('out.png')


if __name__=="__main__":
    resp_before = requests.get("http://curlmyip.net")
    print resp_before.text
    start_hotspot_shield_app()
    time.sleep(5)
    take_screenshot("before_vpn.png")
    button_postion = find_button_position()
    print button_postion
    # pyautogui.moveTo(button_postion[0], button_postion[1], duration=2)
    pyautogui.moveTo(button_postion[0], button_postion[1], 5, pyautogui.easeOutElastic)
    time.sleep(1)
    print "moved"
    pyautogui.click()
    print "clicked"
    time.sleep(5)
    resp_after = requests.get("http://curlmyip.net")
    print resp_after.text
    print "success?"
    # find_image()