#!/usr/bin/env python
# cerner_2^5_2019
# Author: Michael Percival
# Run this program on a full screen terminal to improve productivity at work :) (try git bash if you are on windows).
# Requires python 3.

import os, sys, random, time

IMG = "                                 ``...--------...``                                                 \n                           `.--:://:::::::::::::::/::-.``                                           \n                       `.-:/::--:::::////////:::::::::///:-.                                        \n                    `.:///::::://////////////////////////////:.`                                    \n                  `:+++//////+++++++++++++++++++++++++++////++++-`                                  \n                ./oso++++++++++++++++oooooooooo+++++++++++++++ooo+:.                                \n              `/syysooooo++++++oooo++/::---:::/++oooo+++++++oooossso:`                              \n             :syyyyyssoooooosso/-.`              `.-/+ooooooooooossss+-                             \n           `/hdhhhyyysssssso:.`                      `.:+soooooooosssso/`                           \n          `+ohdddhhhyyyyy+.`                             ./ssssssooooooo:`                          \n         `/ooohddddhhhho.                                  .---....`````                            \n         -ooooosyddddh:                                                                             \n         :sooooo+ooyy:`                                                      ``````....--::://++.   \n         :soooooo++++//::-..````                       ````````....----::::///+++++ooooooosssso.    \n         `+ooooooo+++++////////::::------------------::::::::///////////++++++oooooooooooosss+`     \n          `/oooooo+++++++++//////:::::::::::::::::::::://///////+++++++++++oooooooooooooooss/`      \n            ./oooo++++++++++////////////////////////////////+++++++++++++++ooooooooooooooso-        \n              `.:/+oo+++++++/////////////////////////////////++++++++++++++oooooooooooooo+.         \n                   .-:/++++++++/////////////////////////////++++++++++oooo++++//::--...``           \n                         ``.--::///++++++++++++++++++++++++////:::---..````         ```             \n              `.--:--..``               ````````````                    ```..-::/++ooo-             \n           `:+oooo+++++///::--...`````               ``````....--:::://++++oooooosss+.              \n          -oooooooo+++++++////:::::::::::--------:::::::::::://////+++oooooooooooss/`               \n         -osooooooo++++++++///////////:::::::::::////////+++++++++++oooooooooooooo:                 \n         :ssooooooo++++++++////////////////////////////+++++++++++++ooooooooooooo.                  \n         :ssoooooossso++++++///////////////////////////+++++++++++ooooooooo++//:`                   \n         .osoooyhddddhs---:///+++++++///////////++++++++++++++++///::--..```                        \n          :sosdddddhhyhy/`   `````...----:::::::------...``````                                     \n          `:sddddhhhyyssys+.                               `````...--::/.                           \n            -ydhhhhyyyssoosso:.`                    `.:+++ooooooossssso-                            \n             .+yhhyyysssooooosso+:-.``        ``.-:+osoooooooooosssso/`                             \n               -+yyysssooooooo+++oooo+++////++++ooo++oooooooossssso/.                               \n                 -+ssssooooooo+++/////::::::://///+++oooooooossoo/.                                 \n                   .:+oooooooo+++////:::---:::////+++ooooooooo/:.                                   \n                     `.:/+oooo+++////:::::::::////+++ooooo+/:.`                                     \n                        `.-:/+++++////:::::::////++++++/:-.`                                        \n                    ````...--:://////////////////////::--...````                                    \n                     ````....---::::////////////::::----...`````                                    \n                           `````````............````````` "

def get_color(x, y, t):
    global colors, image
    for i in range(6, -1, -1):
        if x - max(image) + abs(t) > y + (i * 16) + random.randint(0, 16):
            return "\033[" + str(colors[t >= 0][i]) + "m"
    return t <= 0 and "\033[30m" or "\033[" + str(colors[0][-1]) + "m"

os.system("clear")
screen = [int(x) for x in os.popen("stty size").read().split()]
image = [IMG.count("\n"), max([len(x) for x in IMG.split("\n")])]
frames = image[0] * 6
step = 6
colors = [[37, 31, 33, 34, 35, 36, 32], [31, 33, 34, 35, 36, 37, 30]]

while 1:
    for t in (list(range(-frames, step, step)) + list(range(frames, 0, -step))):
        print("\033[" + str(int((screen[0] - image[0]) / 2)) + "H")
        for y in range(image[0]):
            print((" " * int((screen[1] - image[1]) / 2)) + "".join([(get_color(x, y, t) + IMG.split("\n")[y][x] + "\033[0m") for x in range(len(IMG.split("\n")[y]))]))
        if t == 0:
            colors[0].append(colors[0].pop(random.randint(1, 3)))
    time.sleep(1)
