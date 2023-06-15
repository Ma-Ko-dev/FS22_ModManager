import os
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
        # print(mod_name)
        modsInFolder.append(mod_name)


def check_active():
    for mod in modsInFolder:
        if mod not in modsInSave:
            print(f"{mod} ist nur im Ordner.")
            # TODO: Create function to move these mods to another folder


if __name__ == '__main__':
    print(MAIN_PATH)
    print(MODS_PATH)
    if check_savegamefile():
        # later we will "start" the whole progress here, for now for testing, things will work a bit different.
        read_savegame_file()
        read_modfolder()
        check_active()
    else:
        print("Error in Savegame")
