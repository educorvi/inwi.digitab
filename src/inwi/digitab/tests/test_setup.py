# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from inwi.digitab.testing import INWI_DIGITAB_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that inwi.digitab is properly installed."""

    layer = INWI_DIGITAB_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if inwi.digitab is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'inwi.digitab'))

    def test_browserlayer(self):
        """Test that IInwiDigitabLayer is registered."""
        from inwi.digitab.interfaces import (
            IInwiDigitabLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IInwiDigitabLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = INWI_DIGITAB_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['inwi.digitab'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if inwi.digitab is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'inwi.digitab'))

    def test_browserlayer_removed(self):
        """Test that IInwiDigitabLayer is removed."""
        from inwi.digitab.interfaces import \
            IInwiDigitabLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IInwiDigitabLayer,
            utils.registered_layers())
