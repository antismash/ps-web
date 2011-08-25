# -*- coding: utf-8 -*-
from websmash.models import Job
from tests.test_shared import WebsmashTestCase

class AjaxTestCase(WebsmashTestCase):
    def test_server_status(self):
        """Test if server status returns the correct values"""
        rv = self.client.get('/server_status')
        self.assertEquals(rv.json, dict(status='idle', queue_length=0))
        j = Job()
        self.db.session.add(j)
        self.db.session.commit()
        rv = self.client.get('/server_status')
        self.assertEquals(rv.json, dict(status='working', queue_length=1))



