# "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/demo.txt"
#a = 12, resultFunction = functionOne(a)

import os
from chem import *

#for both main_chem() and main_iso(), add code that removes the square brackets from the value in the k:v pair and the dash from the key in k:v pair
#also add code that automatically deletes the 'newfile's generated before (maybe after?) each successful run
#maybe good idea to create a AI/ML alg to help determine whether it's best to apply medicine orally, via injection, etc. or a new method not yet
#tested/finished testing?

def main_elem():

    #file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/demo.txt"
    file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/chem.py"
    with open(file_path, 'r') as file:
#        elem_content_keys = "ELEMENTS_KEYS\n"
#        for keys in elements.keys():
#            print(keys)
#            elem_content_keys += (keys + "\n")
        elem_content_values = "ELEMENTS_VALUES"
        for value in elements.values():
            print(value)
            elem_content_values += (value + "\n")
    new_file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_elem.txt"
    with open(new_file_path, 'w') as writer:
#        writer.write(elem_content_keys)
        writer.write(elem_content_values)
    #check if the file was created successfully and delete it
    if os.path.exists("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_elem.txt"):
        os.remove("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_elem.txt")
    else:
        print("File was not generated or cannot be found.")

def main_iso():

    #file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/demo.txt"
    file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/chem.py"
    with open(file_path, 'r') as file:
#        iso_content_keys = "ISOTOPES_KEYS\n"
#        for keys in isotopes.keys():
#            print(keys)
#            iso_content_keys += (keys + "\n")
        iso_content_values = "ISOTOPES_VALUES"
        for value in isotopes.values():
            print(value)
            iso_content_values += (value + "\n")
    new_file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_iso.txt"
    with open(new_file_path, 'w') as writer:
#        writer.write(iso_content_keys)
        writer.write(iso_content_values)
    #check if the file was created successfully and delete it
    if os.path.exists("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_iso.txt"):
        os.remove("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_iso.txt")
    else:
        print("File was not generated or cannot be found.")

def main_ion_oxy():

    #file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/demo.txt"
    file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/chem.py"
    with open(file_path, 'r') as file:
#        ion_oxy_content_keys = "ION_OXY_KEYS\n"
#        for keys in ion_oxy.keys():
#            print(keys)
#            ion_oxy_content_keys += (keys + "\n")
        ion_oxy_content_values = "ION_OXY_VALUES"
        for value in isotopes.values():
            print(value)
            ion_oxy_content_values += (value + "\n")
    new_file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_ion_oxy.txt"
    with open(new_file_path, 'w') as writer:
#        writer.write(ion_oxy_content_keys)
        writer.write(ion_oxy_content_values)
    #check if the file was created successfully and delete it
    if os.path.exists("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_ion_oxy.txt"):
        os.remove("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_ion_oxy.txt")
    else:
        print("File was not generated or cannot be found.")

def main_polyatomic():

    #file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/demo.txt"
    file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/chem.py"
    with open(file_path, 'r') as file:
#        polyatomic_content_keys = "POLYATOMIC_KEYS\n"
#        for keys in polyatomic.keys():
#            print(keys)
#            polyatomic_content_keys += (keys + "\n")
        polyatomic_content_values = "ION_OXY_VALUES"
        for value in polyatomic.values():
            print(value)
            polyatomic_content_values += (value + "\n")
    new_file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_polyatomic.txt"
    with open(new_file_path, 'w') as writer:
#        writer.write(polyatomic_content_keys)
        writer.write(polyatomic_content_values)
    #check if the file was created successfully and delete it
    if os.path.exists("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_polyatomic.txt"):
        os.remove("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_polyatomic.txt")
    else:
        print("File was not generated or cannot be found.")

def main_atomic_prop():

    #file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/demo.txt"
    file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/chem.py"
    with open(file_path, 'r') as file:
#        atomic_prop_content_keys = "ATOMIC_PROPERTIES_KEYS\n"
#        for keys in atomic_prop.keys():
#            print(keys)
#            atomic_prop_content_keys += (keys + "\n")
        atomic_prop_content_values = "ATOMIC_PROPERTIES_VALUES"
        for value in atomic_prop.values():
            print(value)
            atomic_prop_content_values += (value + "\n")
    new_file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_atomic_prop.txt"
    with open(new_file_path, 'w') as writer:
#        writer.write(atomic_prop_content_keys)
        writer.write(atomic_prop_content_values)
    #check if the file was created successfully and delete it
    if os.path.exists("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_atomic_prop.txt"):
        os.remove("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_atomic_prop.txt")
    else:
        print("File was not generated or cannot be found.")

def main_bonds():

    #file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/demo.txt"
    file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/chem.py"
    with open(file_path, 'r') as file:
#        bonds_content_keys = "BONDS_KEYS\n"
#        for keys in bonds.keys():
#            print(keys)
#            bonds_content_keys += (keys + "\n")
        bonds_content_values = "BONDS_VALUES"
        for value in bonds.values():
            print(value)
            bonds_content_values += (value + "\n")
    new_file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_bonds.txt"
    with open(new_file_path, 'w') as writer:
#        writer.write(bonds_content_keys)
        writer.write(bonds_content_values)
    #check if the file was created successfully and delete it
    if os.path.exists("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_bonds.txt"):
        os.remove("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_bonds.txt")
    else:
        print("File was not generated or cannot be found.")

def main_rings():

    #file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/demo.txt"
    file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/chem.py"
    with open(file_path, 'r') as file:
#        rings_content_keys = "RINGS_KEYS\n"
#        for keys in rings.keys():
#            print(keys)
#            rings_content_keys += (keys + "\n")
        rings_content_values = "RINGS_VALUES"
        for value in rings.values():
            print(value)
            rings_content_values += (value + "\n")
    new_file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_rings.txt"
    with open(new_file_path, 'w') as writer:
#        writer.write(rings_content_keys)
        writer.write(rings_content_values)
    #check if the file was created successfully and delete it
    if os.path.exists("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_rings.txt"):
        os.remove("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_rings.txt")
    else:
        print("File was not generated or cannot be found.")

def main_anomaticity():

    #file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/demo.txt"
    file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/chem.py"
    with open(file_path, 'r') as file:
#        anomaticity_content_keys = "ANOMATICITY_KEYS\n"
#        for keys in anomaticity.keys():
#            print(keys)
#            anomaticity_content_keys += (keys + "\n")
        anomaticity_content_values = "ANOMATICITY_VALUES"
        for value in anomaticity.values():
            print(value)
            anomaticity_content_values += (value + "\n")
    new_file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_anomaticity.txt"
    with open(new_file_path, 'w') as writer:
#        writer.write(anomaticity_content_keys)
        writer.write(anomaticity_content_values)
    #check if the file was created successfully and delete it
    if os.path.exists("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_anomaticity.txt"):
        os.remove("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_anomaticity.txt")
    else:
        print("File was not generated or cannot be found.")

def main_stereo_isomerism():

    #file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/demo.txt"
    file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/chem.py"
    with open(file_path, 'r') as file:
#        stereo_isomerism_content_keys = "STEREO_ISOMERISM_KEYS\n"
#        for keys in stereo_isomerism.keys():
#            print(keys)
#            stereo_isomerism_content_keys += (keys + "\n")
        stereo_isomerism_content_values = "STEREO_ISOMERISM_VALUES"
        for value in stereo_isomerism.values():
            print(value)
            stereo_isomerism_content_values += (value + "\n")
    new_file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_stereo_isomerism.txt"
    with open(new_file_path, 'w') as writer:
#        writer.write(stereo_isomerism_content_keys)
        writer.write(stereo_isomerism_content_values)
    #check if the file was created successfully and delete it
    if os.path.exists("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_stereo_isomerism.txt"):
        os.remove("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_stereo_isomerism.txt")
    else:
        print("File was not generated or cannot be found.")

def main_reactions():

    #file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/demo.txt"
    file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/chem.py"
    with open(file_path, 'r') as file:
#        reactions_content_keys = "REACTIONS_KEYS\n"
#        for keys in reactions.keys():
#            print(keys)
#            reactions_content_keys += (keys + "\n")
        reactions_content_values = "REACTIONS_VALUES"
        for value in reactions.values():
            print(value)
            reactions_content_values += (value + "\n")
    new_file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_reactions.txt"
    with open(new_file_path, 'w') as writer:
#        writer.write(reactions_content_keys)
        writer.write(reactions_content_values)
    #check if the file was created successfully and delete it
    if os.path.exists("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_reactions.txt"):
        os.remove("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_reactions.txt")
    else:
        print("File was not generated or cannot be found.")

def main_disconnections():

    #file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/demo.txt"
    file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/chem.py"
    with open(file_path, 'r') as file:
#        disconnections_content_keys = "DISCONNECTIONS_KEYS\n"
#        for keys in disconnections.keys():
#            print(keys)
#            disconnections_content_keys += (keys + "\n")
        disconnections_content_values = "DISCONNECTIONS_VALUES"
        for value in reactions.values():
            print(value)
            disconnections_content_values += (value + "\n")
    new_file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_disconnections.txt"
    with open(new_file_path, 'w') as writer:
#        writer.write(disconnections_content_keys)
        writer.write(disconnections_content_values)
    #check if the file was created successfully and delete it
    if os.path.exists("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_disconnections.txt"):
        os.remove("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_disconnections.txt")
    else:
        print("File was not generated or cannot be found.")

def main_conventions():

    #file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/demo.txt"
    file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/chem.py"
    with open(file_path, 'r') as file:
#        conventions_content_keys = "CONVENTIONS_KEYS\n"
#        for keys in conventions.keys():
#            print(keys)
#            conventions_content_keys += (keys + "\n")
        conventions_content_values = "CONVENTIONS_VALUES"
        for value in conventions.values():
            print(value)
            conventions_content_values += (value + "\n")
    new_file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_conventions.txt"
    with open(new_file_path, 'w') as writer:
#        writer.write(conventions_content_keys)
        writer.write(conventions_content_values)
    #check if the file was created successfully and delete it
    if os.path.exists("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_conventions.txt"):
        os.remove("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_conventions.txt")
    else:
        print("File was not generated or cannot be found.")

def main_related_lang():

    #file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/demo.txt"
    file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/chem.py"
    with open(file_path, 'r') as file:
#        related_lang_content_keys = "RELATED_LANGUAGE_KEYS\n"
#        for keys in related_lang.keys():
#            print(keys)
#            related_lang_content_keys += (keys + "\n")
        related_lang_content_values = "RELATED_LANGUAGE_VALUES"
        for value in related_lang.values():
            print(value)
            related_lang_content_values += (value + "\n")
    new_file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_related_lang.txt"
    with open(new_file_path, 'w') as writer:
#        writer.write(related_lang_content_keys)
        writer.write(related_lang_content_values)
    #check if the file was created successfully and delete it
    if os.path.exists("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_related_lang.txt"):
        os.remove("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_related_lang.txt")
    else:
        print("File was not generated or cannot be found.")

def main_compounds():

    #file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/demo.txt"
    file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/chem.py"
    with open(file_path, 'r') as file:
#        compounds_content_keys = "COMPOUNDS_KEYS\n"
#        for keys in compounds.keys():
#            print(keys)
#            compounds_content_keys += (keys + "\n")
        compounds_content_values = "COMPOUNDS_VALUES"
        for value in compounds.values():
            print(value)
            compounds_content_values += (value + "\n")
    new_file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_compounds.txt"
    with open(new_file_path, 'w') as writer:
#        writer.write(compounds_content_keys)
        writer.write(compounds_content_values)
    #check if the file was created successfully and delete it
    if os.path.exists("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_compounds.txt"):
        os.remove("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_compounds.txt")
    else:
        print("File was not generated or cannot be found.")

def main_polycations():

    #file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/demo.txt"
    file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/chem.py"
    with open(file_path, 'r') as file:
#        polycations_content_keys = "POLYCATIONS_KEYS\n"
#        for keys in polycations.keys():
#            print(keys)
#            polycations_content_keys += (keys + "\n")
        polycations_content_values = "POLYCATIONS_VALUES"
        for value in polycations.values():
            print(value)
            polycations_content_values += (value + "\n")
    new_file_path = "/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_polycations.txt"
    with open(new_file_path, 'w') as writer:
#        writer.write(polycations_content_keys)
        writer.write(polycations_content_values)
    #check if the file was created successfully and delete it
    if os.path.exists("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_polycations.txt"):
        os.remove("/Users/josiahe.thompson/Library/Mobile Documents/com~apple~CloudDocs/G2RETRO/SCRIPTS/newfile_polycations.txt")
    else:
        print("File was not generated or cannot be found.")

if __name__ == "__main__":
    main_elem(),
    main_iso(), main_ion_oxy(), main_polyatomic(), main_atomic_prop()
    main_bonds(), main_rings(), main_anomaticity(), main_stereo_isomerism(), main_reactions()
    main_disconnections(), main_conventions(), main_related_lang(), main_compounds(), main_polycations()