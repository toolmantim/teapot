# Rack middleware to respond to BREW and coffee-pot-command requests. Use in a rackup file like so:
#
#   use Teapot
#
# or if you're an English Breakfast hater:
#
#   use Teapot, "Lady Grey"
class Teapot
  VERSION = "1.0.0"

  def initialize(app, tea="English Breakfast") #:nodoc:
    @app, @tea = app, tea
  end
  def call(env) #:nodoc:
    if env["REQUEST_METHOD"] == "BREW" || env["Content-Type"] == "application/coffee-pot-command"
      ["418 I'm a teapot", {}, "Care for a cup of #{@tea}?"]
    else
      @app.call(env)
    end
  end
end
