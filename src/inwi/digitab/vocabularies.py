# -- coding: utf-8 -*-
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IContextSourceBinder
from Products.CMFCore.utils import getToolByName
from plone import api as ploneapi
from zope.interface import directlyProvides


def checkvartype(var):
    vartypes = {
      "heute":'date',
      "unb_4":'date',
      "unh_2":'string',
      "uvt_4":'date',
      "uvt_5":'string',
      "vin_4":'geschlecht',
      "vin_5":'string',
      "vin_9":'date',
      "ufb_3":'string',
      "ufb_6":'string',
      "ufb_7":'date',
      "ufd_1":'time',
      "ufd_2":'time',
      "ufd_3":'time',
      "dis_1":'string',
      "dis_4":'string',
      "dis_3":'string',
      "afb_1":'zahl',
      "afb_4":'date',
      "afb_7":'date',
      "uaz_4":'bool',
    }
    return vartypes.get(var)


def getsynoptypes(op):
    synoptypes = {
      "true":(True, 'ja', 'j', 'JA', 'J'),
      "false":(False, 'nein', 'n', 'NEIN', 'N'),
      "m":("m", "M", "male", "Male"),
      "w":("w", "W", "female", "Female"),
    }
    return synoptypes.get(op)


possibleParams = SimpleVocabulary([
    SimpleTerm(value=u"heute", token=u"heute", title=u"heute"),
    SimpleTerm(value=u"unb_4", token=u"unb_4", title=u"Erstellungsdatum"),    
    SimpleTerm(value=u"unh_2", token=u"unh_2", title=u"Dokumentart"),
    SimpleTerm(value=u"uvt_4", token=u"uvt_4", title=u"Unfalltag"),
    SimpleTerm(value=u"uvt_5", token=u"uvt_5", title=u"Aktenzeichen"),
    SimpleTerm(value=u"vin_4", token=u"vin_4", title=u"Geschlecht Versicherter"),
    SimpleTerm(value=u"vin_5", token=u"vin_5", title=u"PLZ Versicherter"),
    SimpleTerm(value=u"vin_9", token=u"vin_9", title=u"Geburtstag Versicherter"),
    SimpleTerm(value=u"ufb_3", token=u"ufb_3", title=u"PLZ Betrieb"),
    SimpleTerm(value=u"ufb_6", token=u"ufb_6", title=u"Beschäftigt als"),
    SimpleTerm(value=u"ufb_7", token=u"ufb_7", title=u"Beschäftigt seit"),
    SimpleTerm(value=u"ufd_1", token=u"ufd_1", title=u"Unfallzeit"),
    SimpleTerm(value=u"ufd_2", token=u"ufd_2", title=u"Arbeitszeit Beginn"),
    SimpleTerm(value=u"ufd_3", token=u"ufd_3", title=u"Arbeitszeit Ende"),
    SimpleTerm(value=u"dis_1", token=u"dis_1", title=u"Diagnose Text"),
    SimpleTerm(value=u"dis_4", token=u"dis_4", title=u"Diagnoseschlüssel"),
    SimpleTerm(value=u"dis_3", token=u"dis_3", title=u"Diagnosecode"),
    SimpleTerm(value=u"afb_1", token=u"afb_1", title=u"Arbeitsunfähigkeit"),
    SimpleTerm(value=u"afb_4", token=u"afb_4", title=u"AU ab (Datum)"),
    SimpleTerm(value=u"afb_7", token=u"afb_7", title=u"vorauss. Ende AU (Datum)"),
    SimpleTerm(value=u"uaz_4", token=u"uaz_4", title=u"Tödlicher Unfall"),
    ])


getOperanden = SimpleVocabulary([
    SimpleTerm(value='true', token='true', title=u"ja (wahr)"),
    SimpleTerm(value='false', token='false', title="nein (falsch)"),
    SimpleTerm(value=u"m", token=u"m", title=u"männlich"),
    SimpleTerm(value=u"w", token=u"w", title=u"weiblich"),
    SimpleTerm(value=u"+", token=u"+", title=u"+ (Plus)"),
    SimpleTerm(value=u"-", token=u"-", title=u"- (Minus)"),
    SimpleTerm(value=u"<", token=u"<", title=u"< kleiner als"),
    SimpleTerm(value=u">", token=u">", title=u"> größer als"),
    SimpleTerm(value=u"==", token=u"==", title="== (gleich)"),
    SimpleTerm(value=u"!=", token=u"!=", title="!= (ungleich)"),
    SimpleTerm(value=u"match", token=u"match", title="in CUSA"),
    SimpleTerm(value=u"no_match", token=u"no_match", title="nicht in CUSA"),
    ])


getComparer = SimpleVocabulary([
    SimpleTerm(value=u"<", token=u"<", title=u"< (kleiner als)"),
    SimpleTerm(value=u">", token=u">", title=u"> (größer als)"),
    SimpleTerm(value=u"==", token=u"==", title=u"== (gleich)"),
    SimpleTerm(value=u"!=", token=u"!=", title=u"!= (ungleich)"),
    SimpleTerm(value=u"in", token=u"in", title=u"enthält"),
    SimpleTerm(value=u"not in", token=u"not in", title=u"enthält nicht"),
    ])

def possibleActions(context):
    terms = []
    brains = ploneapi.content.find(portal_type="Stammblatt")
    if brains:
        for i in brains:
            terms.append(SimpleVocabulary.createTerm(i.UID, i.UID, i.Title))
    return SimpleVocabulary(terms)
directlyProvides(possibleActions, IContextSourceBinder)


possibleLinks = SimpleVocabulary([
    SimpleTerm(value=u'keine', token=u'keine', title=u'Keine'),
    SimpleTerm(value=u'and', token=u'and', title=u'UND'),
    SimpleTerm(value=u'or', token=u'or', title=u'ODER'),
    ])

possibleCustomer = SimpleVocabulary([
    SimpleTerm(value=u'Versicherte', token=u'Versicherte', title=u'Versicherte'),
    SimpleTerm(value=u'Mitgliedsbetriebe', token=u'Mitgliedsbetriebe', title=u'Mitgliedsbetriebe und Einrichtungen'),
    SimpleTerm(value=u'SiFA', token=u'SiFA', title=u'SiFA'),
    ])

