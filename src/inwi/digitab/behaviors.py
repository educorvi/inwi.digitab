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
from inwi.digitab.vocabularies import possibleParams, getOperanden, getComparer, possibleActions, possibleLinks, possibleCustomer
from inwi.digitab.vocab_dale import dale, dokumentarten

class IRule(model.Schema):
    """Felder einer Verarbeitungsregel"""

    rel = schema.Choice(title=u"Relation",
                           source=dale,
                           required=True)

    ind1 = schema.Choice(title=u"Operand",
                           source=getOperanden,
                           required=False)
    
    var = schema.Choice(title=u"Variable-2",
                          source=dale,
                          required=False)

    ind2 = schema.Choice(title=u"Vergleich",
                          source=getComparer,
                          required=False)

    ind3 = schema.TextLine(title=u"Ergebnis",
                          description=u"Zahl oder Text",
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
            fields=('aktion', 'kundengruppe', 'dokumentart', 'rulestable',),
        )

    aktion = schema.Choice(title=u"Auswahl des Prozesses / der Aktion",
                           description=u'Welcher Prozess oder welche Aktion wird angestossen, wenn die Regel im Ergebnis "wahr" liefert?',
                           required=True,
                           source=possibleActions,
    )

    kundengruppe = schema.Choice(title=u"Auswahl der Kundengruppe",
                          description=u'Für welche Kundengruppe soll die Regel angewendet werden?',
                          required=True,
                          source=possibleCustomer,
    )

    dokumentart = schema.Choice(title=u"Auswahl Dokumentart",
                           description=u"Für welche Dokumentart wird die folgende Regel aufgestellt?",
                           required=True,
                           source=dokumentarten,
    )

    directives.widget('rulestable', DataGridFieldFactory)
    rulestable = schema.List(title=u"Verarbeitungsregeln",
                            description=u"Bitte konfigurieren Sie hier die Verarbeitungsregeln für das elektronische Dokument.",
                            required=True,
                            constraint=rule_constraint,
                            value_type=DictRow(title=u"Regel", schema=IRule))

