#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import random

def main():
    app = QApplication([])
    window = QWidget()
    window.setFixedSize(320,180)
    window.setWindowTitle("Wallpaper Select")

    layout = QVBoxLayout()

    buttonEngine = QPushButton("Random Wallpaper Engine")
    buttonEngine.setFixedSize(300,40)
    buttonEngine.clicked.connect(clicked_WPE)

    buttonCuEngine = QPushButton("Add/Set Wallpaper Engine")
    buttonCuEngine.setFixedSize(300,40)
    buttonCuEngine.clicked.connect(clicked_CWPE)

    buttonHyprpaper = QPushButton("Image")
    buttonHyprpaper.setFixedSize(300,40)
    buttonHyprpaper.clicked.connect(clicked_H)
    
    buttonRandom = QPushButton("Random")
    buttonRandom.setFixedSize(300,40)
    buttonRandom.clicked.connect(clicked_R)

    layout.addWidget(buttonEngine)
    layout.addWidget(buttonCuEngine)
    layout.addWidget(buttonHyprpaper)
    layout.addWidget(buttonRandom)
    window.setLayout(layout)

    window.show()
    app.exec_()

def clicked_WPE():
    os.system("python ~/.config/WallpaperSelect/wallpaper.py &")
    exit(main)

def clicked_CWPE():
    os.system("python ~/.config/WallpaperSelect/WallpaperEngineCustom.py &")
    exit(main)

def clicked_H():
    os.system("killall linux-wallpaperengine swaybg hyprpaper")
    os.system("waypaper &")
    exit(main)

def clicked_R():
    if str(random.randint(1,2)) == '1':
        os.system("killall linux-wallpaperengine swaybg hyprpaper")
        os.system("waypaper --random --restore &")
        exit(main)
    else:
        os.system("python ~/.config/WallpaperSelect/wallpaper.py &")
        exit(main)
    
if __name__ == '__main__':
    main()