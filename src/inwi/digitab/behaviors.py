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
from inwi.digitab.vocabularies import possibleParams, getOperanden, getComparer, possibleActions

class IRule(model.Schema):
    """Felder einer Verarbeitungsregel"""

    param1 = schema.Choice(title=u"Parameter-1",
                           source=possibleParams,
                           required=True)

    operand = schema.Choice(title=u"Operand-1",
                           source=getOperanden,
                           required=False)
    
    param2 = schema.Choice(title=u"Parameter-2",
                          source=possibleParams,
                          required=False)

    vergleich = schema.Choice(title=u"Operand-2",
                          source=getComparer,
                          required=False)

    ergebnis = schema.TextLine(title=u"Ergebnis",
                          required=False)

    aktion = schema.Choice(title=u"Aktion",
                          source=possibleActions,
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
            fields=('rulestable',),
        )

    directives.widget('rulestable', DataGridFieldFactory)
    rulestable = schema.List(title=u"Verarbeitungsregeln",
                            description=u"Bitte konfigurieren Sie hier die Verarbeitungsregeln für elektronische Dokumente.",
                            required=True,
                            constraint=rule_constraint,
                            value_type=DictRow(title=u"Regel", schema=IRule))

