# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from plone import api as ploneapi
from inwi.digitab.vocabularies import possibleParams, getOperanden, getComparer, possibleActions, possibleLinks, possibleCustomer
from inwi.digitab.vocab_dale import dale, dokumentarten


class RuleMLViewlet(ViewletBase):

    def update(self):
        self.message = self.get_message()

    def get_message(self):
        return u'My message'

    def get_aktion(self):
        obj = ploneapi.content.get(UID=self.context.aktion)
        return obj.title

    def get_dale(self, value):
        return dale.getTerm(value).title

    def get_operand(self, value):
        return getOperanden.getTerm(value).title

    def render(self):
        if not hasattr(self.context, 'rulestable'):
            return ''
        if not self.context.rulestable:
            return ''
        return super(RuleMLViewlet, self).render()
