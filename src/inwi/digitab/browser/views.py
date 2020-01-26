# -*- coding: utf-8 -*-
from datetime import datetime
from zope.interface import Interface
from plone import api as ploneapi
from inwi.digitab.vocabularies import getsynoptypes, checkvartype
from Products.Five import BrowserView

edok = {
  'uaz_4':'ja',
  'ufd_2':'08:00',
  'ufd_3':'17:00',
  'ufd_1':'07:00',
}

def param1_check(edok, zeile):
    """Prueft ob die boolschen Werte bei Parameter 1 erfuellt sind."""
    input = edok.get(zeile.get('param1'))
    if not input:
        return False
    synops = getsynoptypes(zeile.get('operand'))
    if input in synops:
        return True
    return False

def param1_const(edok, zeile):
    """Prueft Parameter 1 mit seinem Operanden gegen das Ergebnis."""
    input = edok.get(zeile.get('param1'))
    vartype = checkvartype(zeile.get('param1'))
    if zeile.get('param1') == 'heute':
        input = datetime.now().strftime('%d.%m.%Y')
    if not input:
        return False
    operand = zeile.get('operand')
    ergebnis = zeile.get('ergebnis')
    if vartype == 'date':
        wert1 = datetime.strptime(input, '%d.%m.%Y')
        wert2 = datetime.strptime(zeile.get('ergebnis'), '%d.%m.%Y')
        if operand == '>':
            if wert1 > wert2:
                return True
        if operand == '<':
            if wert1 < wert2:
                return True
        if operand == '==':
            if wert1 == wert2:
                return True
    if vartype == 'zahl':
        wert1 = float(input)
        wert2 = float(zeile.get('ergebnis'))
        if operand == '>':
            if wert1 > wert2:
                return True
        if operand == '<':
            if wert1 < wert2:
                return True
        if operand == '==':
            if wert1 == wert2:
                return True
    if vartype == 'string':
        wert1 = input
        wert2 = zeile.get('ergebnis')
        if operand == '==':
            if wert1 == wert2:
                return True
    return False

def param1_math_param2(edok, zeile):
    """Prueft eine mathematische Operation von Parameter 1 und Parameter 2 mit dem
       Vergleichsoperanden gegen das Ergebnis."""
    vartype1 = checkvartype(zeile.get('param1'))
    vartype2 = checkvartype(zeile.get('param2'))
    if vartype1 == vartype2:
        input1 = edok.get(zeile.get('param1'))
        input2 = edok.get(zeile.get('param2'))
        if zeile.get('param1') == 'heute':
            input1 = datetime.now().strftime('%d.%m.%Y')
        if zeile.get('param2') == 'heute':
            input2 = datetime.now().strftime('%d.%m.%Y')
        if not input1 or not input2:
            return False
        operand = zeile.get('operand')
        vergleich = zeile.get('vergleich')
        ergebnis = zeile.get('ergebnis')
        if vartype1 == 'date':
            wert1 = datetime.strptime(input1, "%d.%m.%Y")
            wert2 = datetime.strptime(input2, "%d.%m.%Y")
            if operand == '-':
                result = wert1 - wert2
                diff = float(result.days)
                if vergleich == '>':
                    if diff > float(ergebnis):
                        return True
                elif vergleich == '<':
                    if diff < float(ergebnis):
                        return True
                elif vergleich == '==':
                    if diff == float(ergebnis):
                        return True
        elif vartype == 'time':
            wert1 = datetime.strptime(input1, "%H:%M")
            wert2 = datetime.strptime(input2, "%H:%M")
            if operand == '-':
                result = wert1 - wert2
                diff = float(result.days)
                if vergleich == '>':
                    if diff > float(ergebnis):
                        return True
                elif vergleich == '<':
                    if diff < float(ergebnis):
                        return True
                elif vergleich == '==':
                    if diff == float(ergebnis):
                        return True
        elif vartype == 'zahl':
            wert1 = float(input)
            wert2 = float(input)
            if operand == '+':
                summe = wert1 + wert2
                if vergleich == '>':
                    if summe > float(ergebnis):
                        return True
                if vergleich == '<':
                    if summe < float(ergebnis):
                        return True
                if vergleich == '==':
                    if summe == float(ergebnis):
                        return True
                if vergleich == '!=':
                    if summe == float(ergebnis):
                        return True
        else:
            wert1 = input1
            wert2 = input2
    return False

def param1_compare_param2(edok, zeile):
    """Verleicht Parameter 1 mit Parameter 2"""
    vartype1 = checkvartype(zeile.get('param1'))
    vartype2 = checkvartype(zeile.get('param2'))
    if vartype1 == vartype2:
        input1 = edok.get(zeile.get('param1'))
        input2 = edok.get(zeile.get('param2'))
        if zeile.get('param1') == 'heute':
            input1 = datetime.now().strftime('%d.%m.%Y')
        if zeile.get('param2') == 'heute':
            input2 = datetime.now().strftime('%d.%m.%Y')
        if not input1 or not input2:
            return False
        operand = zeile.get('operand')
        if vartype1 == 'date':
            wert1 = datetime.strptime(input1, "%d.%m.%Y")
            wert2 = datetime.strptime(input2, "%d.%m.%Y")
        elif vartype1 == 'time':
            wert1 = datetime.strptime(input1, "%H:%M")
            wert2 = datetime.strptime(input2, "%H:%M")
        elif vartype1 == 'zahl': 
            wert1 = float(input1)
            wert2 = float(input2)
        else:
            wert1 = input1
            wert2 = input2

        if operand == '<':
            if wert1 < wert2:
                return True
        elif operand == '>':
            if wert1 > wert2:
                return True
        elif operand == '==':
            if wert1 == wert2:
                return True
        elif operand == '!=':
            if wert1 != wert2:
                return True
    return False


class TestView(BrowserView):

    def rulegroups(self):
        """Unterscheidet zwischen einzeiligen Regeln und mehrzeiligen Regeln.
           Einzelige Regeln werden als Dictionary der Liste hinzugefügt.
           Mehrzeilige Regeln werden zu einer Liste zusammegefasst."""
        groups = []
        group = []
        for i in self.context.rulestable:
            if i.get('aktion') in ["and", "or"]:
                if not group:
                    group.append(i)
                else:
                    group.append(i)
            if i.get('aktion') not in ["and", "or"]:
                if group:
                    group.append(i)
                    groups.append(group)
                    group = []
                else:
                    groups.append(i)
        return groups

    def __call__(self):
        """Die Gruppe wird durchlaufen und gegen das elektronische Dokument geprüft."""
        groups = self.rulegroups()
        aufgaben = []
        for i in groups:

            if isinstance(i, list):
                results = []
                boolvalue = i[0].get('aktion')
                aufgabe = ploneapi.content.get(UID=i[-1].get('aktion'))
                for k in i:
                    if k.get('operand') and not k.get('param2'):
                        if k.get('operand') in ['true', 'false']:
                            results.append(param1_check(edok, k))
                        elif k.get('operand') in ['m', 'w']:
                            results.append(param1_check(edok, k))
                    if k.get('operand') and k.get('param2') and not k.get('vergleich'):
                        results.append(param1_compare_param2(edok, k))
                    if k.get('operand') and k.get('param2') and k.get('vergleich'):
                        results.append(param1_math_param2(edok, k))
                    if k.get('operand') and not k.get('param2') and k.get('ergebnis'):
                        results.append(param1_const(edok, k))
                if boolvalue == 'or':
                    if len(i) == 2:
                        if results[0] or results[1]:
                            aufgaben.append(aufgabe.title)
                    elif len(i) == 3:
                        if results[0] or results[1] or results[2]:
                            aufgaben.append(aufgabe.title)
                if boolvalue == 'and':
                    if len(i) == 2:
                        if results[0] and results[1]:
                            aufgaben.append(aufgabe.title)
                    elif len(i) == 3:
                        if results[0] and results[1] and results[2]:
                            aufgaben.append(aufgabe.title)
          
            elif isinstance(i, dict):
                aufgabe = ploneapi.content.get(UID=i.get('aktion'))
                if i.get('operand') and not i.get('param2'):
                    if i.get('operand') in ['true', 'false']:
                        if param1_check(edok, i):
                            aufgaben.append(aufgabe.title)
                    elif i.get('operand') in ['m', 'w']:
                        if param1_check(edok, i):
                            aufgaben.append(aufgabe.title)
                if i.get('operand') and i.get('param2') and not i.get('vergleich'):
                    if param1_compare_param2(edok, i):
                        aufgaben.append(aufgabe.title)
                if i.get('operand') and i.get('param2') and i.get('vergleich'):
                    if param1_math_param2(edok, i):
                        aufgaben.append(aufgabe.title)
                if i.get('operand') and not i.get('param2') and i.get('ergebnis'):
                    if param1_const(edok, i):
                        aufgaben.append(aufgabe.title)
                
        print(aufgaben)
