# teapot

It's imperative to respond correctly to coffee machine BREW requests when you are, in fact, a teapot. This piece of WSGI middleware will ensure you comply with HTCPCP/1.0: the Hyper Text Coffee Pot Control Protocol.

For more information see http://www.ietf.org/rfc/rfc2324.txt

## INSTALL

```bash
pip install teapot
```

Or install from source:

```bash
pip install .
```

## USAGE

Simply import and use in your WSGI application:

```python
from teapot import Teapot

# Wrap your WSGI application
app = Teapot(app)
```

Your WSGI application will now serve English Breakfast and respond with a `418 I'm a teapot` if it receives any `BREW` or `application/coffee-pot-command` requests.

Hater of English Breakfast? You're in luck—just pass in your preferred brew:

```python
app = Teapot(app, "Lady Grey")
```

### Flask Example

```python
from flask import Flask
from teapot import Teapot

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

# Wrap the Flask app with Teapot middleware
app.wsgi_app = Teapot(app.wsgi_app)

if __name__ == '__main__':
    app.run()
```

### Django Example

In your Django `settings.py`:

```python
# Add to your middleware
MIDDLEWARE = [
    # ... other middleware
]

# Wrap the WSGI application in wsgi.py
from teapot import Teapot
application = Teapot(application)
```

## BREWING

You can perform a BREW request using curl's request method flag `-X`:

```bash
curl -i -X BREW http://localhost:5000
```

Expected response:
```
HTTP/1.1 418 I'm a teapot
Content-Type: text/plain

Care for a cup of English Breakfast?
```

## TESTING

Run the tests:

```bash
python test_teapot.py
```

Or using unittest:

```bash
python -m unittest test_teapot
```

## LICENSE

WTFPL (Do What The F* You Want To Public License) v2
