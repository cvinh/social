# -*- coding: utf-8 -*-
# License AGPL-3: Antiun Ingenieria S.L. - Antonio Espinosa
# See README.rst file on addon root folder for more details

from openerp.tests.common import TransactionCase


class BaseCase(TransactionCase):
    # Use case : Prepare some data for current test case
    def setUp(self):
        super(BaseCase, self).setUp()
        # More initializations here ...

    # Use case : Clean data after current test case
    def tearDown(self):
        # Clean data here ...
        super(BaseCase, self).tearDown()

    # Auxiliar common methods here
    # Method name can't start with 'test_'

    # Common test methods here
    # Method name must start with 'test_'
