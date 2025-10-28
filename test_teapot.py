"""
Unit tests for the Teapot WSGI middleware.
"""

import unittest
from teapot import Teapot


class DummyApp:
    """A simple WSGI application for testing."""

    def __call__(self, environ, start_response):
        status = "200 OK"
        headers = [("Content-Type", "text/plain")]
        start_response(status, headers)
        return [b""]


class MockStartResponse:
    """Mock start_response callable to capture status and headers."""

    def __init__(self):
        self.status = None
        self.headers = None

    def __call__(self, status, headers):
        self.status = status
        self.headers = headers


class TeapotTest(unittest.TestCase):

    def test_returns_418_with_content_type_coffee_pot_command(self):
        """Test that 418 is returned when Content-Type is application/coffee-pot-command."""
        app = Teapot(DummyApp(), "English Breakfast")
        environ = {
            "REQUEST_METHOD": "GET",
            "CONTENT_TYPE": "application/coffee-pot-command"
        }
        start_response = MockStartResponse()

        response = app(environ, start_response)

        self.assertEqual("418 I'm a teapot", start_response.status)

    def test_returns_418_with_request_method_brew(self):
        """Test that 418 is returned when request method is BREW."""
        app = Teapot(DummyApp(), "STFU")
        environ = {
            "REQUEST_METHOD": "BREW"
        }
        start_response = MockStartResponse()

        response = app(environ, start_response)

        self.assertEqual("418 I'm a teapot", start_response.status)

    def test_defaults_tea_type_to_english_breakfast(self):
        """Test that tea type defaults to English Breakfast."""
        app = Teapot(DummyApp())
        environ = {
            "REQUEST_METHOD": "BREW"
        }
        start_response = MockStartResponse()

        response = app(environ, start_response)
        body = b"".join(response).decode('utf-8')

        self.assertEqual("Care for a cup of English Breakfast?", body)

    def test_serves_tea_passed_into_new(self):
        """Test that custom tea type is used when provided."""
        app = Teapot(DummyApp(), "Lady Grey")
        environ = {
            "REQUEST_METHOD": "BREW"
        }
        start_response = MockStartResponse()

        response = app(environ, start_response)
        body = b"".join(response).decode('utf-8')

        self.assertEqual("Care for a cup of Lady Grey?", body)

    def test_passes_through_normal_requests(self):
        """Test that normal requests are passed through to the wrapped app."""
        app = Teapot(DummyApp())
        environ = {
            "REQUEST_METHOD": "GET"
        }
        start_response = MockStartResponse()

        response = app(environ, start_response)

        self.assertEqual("200 OK", start_response.status)


if __name__ == '__main__':
    unittest.main()
