#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, subprocess, getpass
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *



def main():
    app = QApplication([])
    window = QWidget()
    window.setFixedSize(320,95)
    window.setWindowTitle("Wallpaper Select")

    layout = QVBoxLayout()

    button1 = QPushButton("Add to '/usr/bin/' and applications")
    button1.setFixedSize(300,40)
    button1.clicked.connect(addTo)

    button2 = QPushButton("")

    layout.addWidget(button2)
    layout.addWidget(button1)
    window.setLayout(layout)

    window.show()
    app.exec_()

def install():
    os.system("mkdir ~/.config/WallpaperSelect/")


def addTo():
    os.system("sudo wallpaper-select")


if __name__ == '__main__':
    main()
