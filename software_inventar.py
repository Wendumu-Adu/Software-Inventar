import xml.etree.ElementTree as ET

def aufgabe_1():
    root = ET.Element("inventar") # create_xml

    #Eintrag 1: Python 3
    prog1 = ET.SubElement(root, "programm", id="p01")
    ET.SubElement(prog1, "name").text = "Python 3"
    ET.SubElement(prog1, "version").text = "3.12"
    ET.SubElement(prog1, "typ").text = "Open Source"

    #Eintrag 2: Vs Code
    prog2 = ET.SubElement(root, "programm", id="p02")
    ET.SubElement(prog2, "name").text = "VS Code"
    ET.SubElement(prog2, "version").text = "1.85"
    ET.SubElement(prog2, "typ").text = "Freeware"

    #Baum erstellen and formatieren
    tree = ET.ElementTree(root)
    ET.indent(tree, space="    ") #4 Leerzeichen

    # "wb" mit xml-deklaration
    with open("software.xml", "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)
    print("Aufgabe 1: 'software.xml' wurde erstellt.")

# read_xml():
def aufgabe_2():
    tree = ET.parse("software.xml")
    root = tree.getroot()

    print(f"\nAufgabe 2: Root-Tag ist '{root.tag}'")
    print("Inhalt von software.xml:")
    for prog in root.findall("programm"):
        prog_id = prog.attrib.get("id")
        name = prog.find("name").text
        version = prog.find("version").text
        print(f"  [{prog_id}] {name} (v{version})")

#def update_xml():
def aufgabe_3():
    tree = ET.parse("software.xml")
    root = tree.getroot()

    # p01 updaten
    for prog in root.findall("programm"):
        if prog.attrib.get("id") == "p01":
            prog.find("version").text = "3.13"

    # p03 hinzufügen
    prog3 = ET.SubElement(root, "programm", id="p03")
    ET.SubElement(prog3, "name").text = "Git"
    ET.SubElement(prog3, "version").text = "2.43"
    ET.SubElement(prog3, "typ").text = "Open Source"

    ET.indent(tree, space="    ")
    with open("software.xml", "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)
    print("\nAufgabe 3: 'p01' aktualisiert und 'p03' hinzugefügt.")

if __name__ == "__main__":
    aufgabe_1() #create_xml()
    aufgabe_2() # read_xml()
    aufgabe_3() #update_xml()
    # Erneut ausgeben, um die Änderungen zu bestätigen
    aufgabe_2()
