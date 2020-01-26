# -*- coding: utf-8 -*-
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider
from zope.interface import Invalid
from collective.z3cform.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield import DictRow
from inwi.digitab.vocabularies import possibleParams, getOperanden, getComparer, possibleActions, possibleLinks
from inwi.digitab.vocab_dale import dale, dokumentarten

class IRule(model.Schema):
    """Felder einer Verarbeitungsregel"""

    var1 = schema.Choice(title=u"Variable-1",
                           source=dale,
                           required=True)

    operand = schema.Choice(title=u"Operand",
                           source=getOperanden,
                           required=False)
    
    var2 = schema.Choice(title=u"Variable-2",
                          source=dale,
                          required=False)

    vergleich = schema.Choice(title=u"Vergleich",
                          source=getComparer,
                          required=False)

    ergebnis = schema.Int(title=u"Ergebnis",
                          description="(ganze Zahl)",
                          required=False)

    link = schema.Choice(title=u"Verknüpfung",
                          source=possibleLinks,
                          required=True)

class RuleInvalid(Invalid):
    __doc__ = u"Fehler in der von Ihnen konfigurierten Regel."


def rule_constraint(value):
    """ Prueft die Regel ob alle notwendigen Parameter vorhanden sind."""

    for i in value:
        if not i.get('operand') and not i.get('vergleich'):
            raise RuleInvalid(u"Es muss entweder ein Operand oder ein Vergleich konfiguriert werden.")
        if i.get('vergleich') and not i.get('ergebnis'):
            raise RuleInvalid(u"Bei einem konfigurierten Vergleich muss ein Ergebnis eingetragen werden.")
    return True
                    

@provider(IFormFieldProvider)
class IRulesTable(model.Schema):
    """Add a Table to configure rules for a INWI-Document
    """

    model.fieldset(
            'inwidigitab',
            label=u'INWI-Digitab',
            fields=('aktion', 'dokumentart', 'rulestable',),
        )

    aktion = schema.Choice(title=u"Auswahl des Prozesses / der Aktion",
                           description=u'Welcher Prozess oder welche Aktion wird angestossen, wenn die Regel im Ergebnis "wahr" liefert?',
                           required=False,
                           source=possibleActions,
    )

    dokumentart = schema.Choice(title=u"Auswahl Dokumentart",
                           description=u"Für welche Dokumentart wird die folgende Regel aufgestellt?",
                           required=False,
                           source=dokumentarten,
    )

    directives.widget('rulestable', DataGridFieldFactory)
    rulestable = schema.List(title=u"Verarbeitungsregeln",
                            description=u"Bitte konfigurieren Sie hier die Verarbeitungsregeln für das elektronische Dokument.",
                            required=True,
                            constraint=rule_constraint,
                            value_type=DictRow(title=u"Regel", schema=IRule))

