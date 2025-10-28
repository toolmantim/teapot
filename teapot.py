"""
WSGI middleware to respond to BREW and coffee-pot-command requests.

Use in a WSGI application like so:

    from teapot import Teapot

    app = Teapot(app)

or if you're an English Breakfast hater:

    app = Teapot(app, "Lady Grey")
"""


class Teapot:
    """
    WSGI middleware that implements RFC 2324 - HTCPCP/1.0
    (Hyper Text Coffee Pot Control Protocol).

    Returns HTTP 418 "I'm a teapot" status code when receiving
    BREW requests or application/coffee-pot-command content type.
    """

    def __init__(self, app, tea="English Breakfast"):
        """
        Initialize the Teapot middleware.

        Args:
            app: The WSGI application to wrap
            tea: The type of tea to serve (default: "English Breakfast")
        """
        self.app = app
        self.tea = tea

    def __call__(self, environ, start_response):
        """
        Handle WSGI requests.

        Args:
            environ: WSGI environment dictionary
            start_response: WSGI start_response callable

        Returns:
            WSGI response iterable
        """
        request_method = environ.get("REQUEST_METHOD", "")
        content_type = environ.get("CONTENT_TYPE", "")

        if request_method == "BREW" or content_type == "application/coffee-pot-command":
            # Return 418 I'm a teapot response
            status = "418 I'm a teapot"
            headers = [("Content-Type", "text/plain")]
            start_response(status, headers)
            body = f"Care for a cup of {self.tea}?"
            return [body.encode('utf-8')]
        else:
            # Pass through to the wrapped application
            return self.app(environ, start_response)
