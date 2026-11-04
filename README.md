Software-Inventarverwaltung (Python XML Processing) 

Eine praxisnahe Übung zur Erstellung, zum Auslesen, Abfragen und Bearbeiten von XML-Dateien mit Pythons integriertem Modul xml.etree.ElementTree.

Aufgabenübersicht

Aufgabe 1: XML-Struktur erstellen & Exportieren

Ziel-Datei: software.xml

Verwendete Werkzeuge: ET.Element, ET.SubElement, ET.indent(), tree.write(..., mode="wb")

Ziel: Erstellung eines <inventar>-Root-Elements mit zwei Programm-Einträgen:

ID: p01 | Name: Python 3 | Version: 3.12 | Typ: Open Source

ID: p02 | Name: VS Code | Version: 1.85 | Typ: Freeware

Wichtige Technik: Dateien werden im Binärmodus ("wb") mit xml_declaration=True gespeichert und mit ET.indent() für eine saubere Formatierung strukturiert.

Aufgabe 2: XML einlesen & Inspectieren

Verwendete Werkzeuge: ET.parse(), findall(), .attrib, .text

Ziel: Laden von software.xml, Auslesen des Root-Tag-Namens und Iteration über alle <programm>-Elemente zur Ausgabe von ID, Name und Version in der Konsole.

Aufgabe 3: XML-Knoten bearbeiten & Erweitern

Verwendete Werkzeuge: Element-Filterung, .find().text, ET.SubElement()

Ziel:

Programm p01 suchen und seine Version auf 3.13 aktualisieren.

Ein neues Programm p03 hinzufügen (Git, Version 2.43, Typ Open Source).

Den aktualisierten Baum neu formatieren und zurück in software.xml speichern.

