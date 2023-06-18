import os
import shutil
import xml.etree.ElementTree as ET
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
    if not os.path.exists(EXTERNAL_MODFOLDER):
        print("Creating new external Modfolder.")
        os.makedirs(EXTERNAL_MODFOLDER)


# Check if the important file, careerSavegame.xml, exists in the selected savegame.
def check_savegamefile():
    if os.path.isfile(os.path.join(MAIN_PATH, savegame, savegame_filename)):
        return True
    else:
        return False


def read_savegame_file():
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
        # print("####################################################")


def read_modfolder():
    mod_names = os.listdir(MODS_PATH)

    for mod_name in mod_names:
        modsInFolder.append(mod_name)


def check_active():
    for mod in modsInFolder:
        if mod not in modsInSave:
            print(f"{mod} ist nur im Ordner.")
            # print(os.path.join(MODS_PATH, mod))
            inactiveMods.append(os.path.join(MODS_PATH, mod))


def move_inactive():
    for mod in inactiveMods:
        print(f"Moving {mod} to {EXTERNAL_MODFOLDER}")
        shutil.move(mod, EXTERNAL_MODFOLDER)
        # inactiveMods.pop(0)


def create_modlist():
    modNames.sort()
    with open("modlist.txt", "w", encoding="utf-8") as file:
        for mod in modNames:
            file.write(f"{mod}\n")


if __name__ == '__main__':
    if check_savegamefile():
        # later we will "start" the whole progress here, for now for testing, things will work a bit different.
        check_external_modfolder()
        read_savegame_file()
        read_modfolder()
        check_active()
        move_inactive()
        create_modlist()
    else:
        print("Error in Savegame")
