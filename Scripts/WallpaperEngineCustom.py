#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, random, time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def main():
    app2 = QApplication([])
    window2 = QWidget()
    window2.setFixedSize(200,130)
    window2.setWindowTitle("Wallpaper Engine Select")

    layout2 = QVBoxLayout()

    label = QLabel("Enter the workshop ID")
    textbox = QTextEdit()
    button = QPushButton("Set")
    addButton = QPushButton("Add to Random")

    button.clicked.connect(lambda: clickedS(textbox.toPlainText()))
    addButton.clicked.connect(lambda: clickedA(textbox.toPlainText()))
    addButton.clicked.connect(lambda: clickedS(textbox.toPlainText()))

    layout2.addWidget(label)
    layout2.addWidget(textbox)
    layout2.addWidget(button)
    layout2.addWidget(addButton)
    window2.setLayout(layout2)

    window2.show()
    app2.exec_()

def clickedS(NewWallpaper):
    os.system("killall linux-wallpaperengine swaybg hyprpaper")
    os.system("linux-wallpaperengine --silent --fps 48 --screen-root HDMI-A-1 --screen-root DP-1 --screen-root DP-2 " + NewWallpaper + " &")
    time.sleep(1)
    exit(main)

def clickedA(NewWallpaper):
    wallpaper = [NewWallpaper + " "]
    file = open("/home/" + os.getlogin() + "/.config/WallpaperSelect/wallpaper.txt", "r")
    wallpaper.append(str(file.read()))

    with open("/home/" + os.getlogin() + "/.config/WallpaperSelect/wallpaper.txt", "w") as f:
        for s in wallpaper:
            f.write(str(s))
    exit(clickedA)

if __name__ == '__main__':
    main()
