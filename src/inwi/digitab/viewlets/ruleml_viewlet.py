# -*- coding: utf-8 -*-
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides
from plone.app.layout.viewlets import ViewletBase
from plone import api as ploneapi
from inwi.digitab.vocabularies import possibleParams, getOperanden, getComparer, possibleActions, possibleLinks, possibleCustomer
from inwi.digitab.vocab_dale import dale, dokumentarten


class RuleMLViewlet(ViewletBase):

    def update(self):
        # Bereinigung der Rulestable
        alsoProvides(self.request, IDisableCSRFProtection)
        newtable = []
        if hasattr(self.context, 'rulestable'):
            rulestable = self.context.rulestable
            for i in rulestable:
                if i.get('rel'):
                    newtable.append(i)
        self.context.rulestable = newtable

    def get_aktion(self):
        obj = ploneapi.content.get(UID=self.context.aktion)
        return obj.title

    def get_dale(self, value):
        if value:
            return dale.getTerm(value).title
        return value

    def get_operand(self, value):
        if value:
            return getOperanden.getTerm(value).title
        return value

    def render(self):
        if not hasattr(self.context, 'rulestable'):
            return ''
        if not self.context.rulestable:
            return ''
        return super(RuleMLViewlet, self).render()
