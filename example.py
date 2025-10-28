"""
Simple example WSGI application using the Teapot middleware.

Run with: python example.py
Test with: curl -i -X BREW http://localhost:8000
"""

from wsgiref.simple_server import make_server
from teapot import Teapot


def simple_app(environ, start_response):
    """A simple WSGI application."""
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return [b'Hello! This is a regular response.\n']


if __name__ == '__main__':
    # Wrap the application with Teapot middleware
    app = Teapot(simple_app, "English Breakfast")

    # Create and start the server
    with make_server('', 8000, app) as httpd:
        print("Serving on port 8000...")
        print("Try: curl -i -X BREW http://localhost:8000")
        print("Or:  curl -i http://localhost:8000")
        httpd.serve_forever()
