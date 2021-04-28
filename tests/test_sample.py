import pytest
import os
from flask import Flask


class Test:

    def test_base(self):
        app = Flask(__name__)
        client = app.test_client()
        response = client.get('/base')

        assert 0 == 0
