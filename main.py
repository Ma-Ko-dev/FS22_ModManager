import os
import shutil
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter.font import Font
# from tkinter import ttk
from paths import *

# Paths to FS22 main folder for mods and savegames. For some privacy i decided to hide my path names since they include
# my full Name.
# TODO: Change this to a changeable one later (With a GUI for example). For now its static.

# What savegame to read
# TODO: Change the Savegame with a GUI. For now it has to be changed in the code.
savegame = "savegame8"
savegame_filename = "careerSavegame.xml"

# modlisten
modsInFolder = []
modsInSave = []
modNames = []
inactiveMods = []


# check if the external mod folder exists. creates one if not
def check_external_modfolder():
    """Creates the "backup" folder for mods that are not in a savegame  if it's not present."""
    if not os.path.exists(EXTERNAL_MODFOLDER):
        print("Creating new external Modfolder.")
        os.makedirs(EXTERNAL_MODFOLDER)


# Check if the important file, careerSavegame.xml, exists in the selected savegame.
def check_savegamefile():
    """Checks if the savegame we are trying to read exists."""
    if os.path.isfile(os.path.join(MAIN_PATH, savegame, savegame_filename)):
        return True
    else:
        return False


def read_savegame_file():
    """Reads the careerSavegame.xml and fills some lists with the corresponding information."""
    tree = ET.parse(os.path.join(MAIN_PATH, savegame, savegame_filename))
    root = tree.getroot()
    mod_entries = root.findall('mod')

    for mod in mod_entries:
        modsInSave.append(f"{mod.attrib['modName']}.zip")
        modNames.append(f"{mod.attrib['title']}, Version: {mod.attrib['version']}")
        # mod_name = mod.attrib['modName']
        # mod_title = mod.attrib['title']
        # mod_version = mod.attrib['version']
        # mod_required = mod.attrib['required']
        # mod_file_hash = mod.attrib['fileHash']
        #
        # print("Mod Name:", mod_name)
        # print("Mod Title:", mod_title)
        # print("Mod Version:", mod_version)
        # print("Mod Required:", mod_required)
        # print("Mod File Hash:", mod_file_hash)


def read_modfolder():
    """Reads the games modfolder and saves all files as strings in a list for later use."""
    mod_names = os.listdir(MODS_PATH)

    for mod_name in mod_names:
        modsInFolder.append(mod_name)


def check_active():
    """Compares the modsInFolder list against the modsInSave list and saves mods that are not in the savegame in a
    seperate list."""
    for mod in modsInFolder:
        if mod not in modsInSave:
            inactiveMods.append(os.path.join(MODS_PATH, mod))


def move_inactive():
    """Moves all mods that are inactive/not in the mod folder to the "backup" folder."""
    for mod in inactiveMods:
        print(f"Moving {mod} to {EXTERNAL_MODFOLDER}")
        shutil.move(mod, EXTERNAL_MODFOLDER)


def create_modlist():
    """Sorts and creates a textfile for a modlist (for sharing for example)."""
    modNames.sort()
    with open("modlist.txt", "w", encoding="utf-8") as file:
        for mod in modNames:
            file.write(f"{mod}\n")


def open_gui():
    root = tk.Tk()

    min_win_width = 300
    min_win_height = 200
    max_win_width = 800
    max_win_height = 600
    root.minsize(min_win_width, min_win_height)
    root.maxsize(max_win_width, max_win_height)
    root.title("Farming Simulator 22 ModManager")

    headline_font = Font(family="Helvetica", size=15, weight="bold")
    label_headline_text = "Farming Simulator 2022 ModManager"
    label_headline = tk.Label(root, text=label_headline_text, font=headline_font)
    label_headline.grid(row=0, column=0, sticky="nsew", padx=20)

    label_savegame_text = "Welches Savegame soll bearbeitet werden:"
    label_savegame = tk.Label(root, text=label_savegame_text)
    label_savegame.grid(row=1, column=0, sticky="nsew", padx=20)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()


if __name__ == '__main__':
    # if check_savegamefile():
    #     # later we will "start" the whole progress here, for now for testing, things will work a bit different.
    #     check_external_modfolder()
    #     read_savegame_file()
    #     read_modfolder()
    #     check_active()
    #     move_inactive()
    #     create_modlist()
    # else:
    #     print("Error in Savegame")
    open_gui()
