require 'test/unit'

require 'rubygems'
require 'rack/mock'

require File.join(File.dirname(__FILE__), "..", "lib", "teapot")

class DummyApp
  def call(env)
    [200, {}, ""]
  end
end

class TeapotTest < Test::Unit::TestCase
  def test_returns_418_with_content_type_coffee_pot_command
    req = Rack::MockRequest.new(Teapot.new(DummyApp.new, "English Breakfast"))
    res = req.get("", {"Content-Type" => "application/coffee-pot-command"})
    assert_equal 418, res.status
  end
  def test_returns_418_with_request_method_brew
    req = Rack::MockRequest.new(Teapot.new(DummyApp.new, "STFU"))
    res = req.request("BREW")
    assert_equal 418, res.status
  end
  def test_defaults_tea_type_to_english_breakfast
    req = Rack::MockRequest.new(Teapot.new(DummyApp.new))
    res = req.request("BREW")
    assert_equal "Care for a cup of English Breakfast?", res.body
  end
  def test_serves_tea_passed_into_new
    req = Rack::MockRequest.new(Teapot.new(DummyApp.new, "Lady Grey"))
    res = req.request("BREW")
    assert_equal "Care for a cup of Lady Grey?", res.body
  end
end
