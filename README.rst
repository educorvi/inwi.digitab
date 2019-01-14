.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

============
inwi.digitab
============

Mit diesem Add-On für das Open-Source CMS Plone sollen Autoren des Intranet-Wissensmanagements "INWI" in die Lage versetzt werden,
selbständig Verarbeitungsregeln für Datensätze, elektronische Dokumente, o.ä. zu konfigurieren. Die Texte des INWI sind aktuell nur
von Menschen lesbar. Demensprechend können die darin beschriebenen Verarbeitungsregeln auch nur von Menschen interpretiert und
ausgeführt werden. Mit diesem Add-On soll es ermöglicht werden, dass die Verarbeitungsregeln auch maschinenlesbar werden. 

Features
--------

- Behavior (Tab INWI-Digitab) für alle Artikeltypen in Plone, die auf Dexterity basieren
- Parameterauswahl anhand der DALE-XML-Struktur
- Vocabularies für Parameter, Operanden und Aktionen
- Prototyphafte Umsetzung einer Dokumentverarbeitung


Beispiele
---------

- Aktuell sind noch keine Beispiele verfügbar.


Dokumentation
-------------

Eine deutsche Konzeptbeschreibung ist im docs-Ordner verfügbar.

Übersetzungen
-------------

- Das Add-On ist aktuell nur in Deutsch verfügbar. Weitere Übersetzungen sind nicht geplant.


Installation
------------

Installieren Sie INWI-Digitab durch Hinzufügen des Add-Ons zur buildout.cfg::

    [buildout]

    ...

    eggs =
        inwi.digitab


danach starten Sie: ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/educorvi/inwi.digitab/issues
- Source Code: https://github.com/educorvi/inwi.digitab


Support
-------

Für selbständige Tests unseres Prototyps und dabei auftretende Fehler: walther.educorvi@gmail.com


License
-------

GPLv2.
