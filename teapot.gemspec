Gem::Specification.new do |spec|
  spec.name          = "teapot"
  spec.version       = "1.0.1"
  spec.summary       = "Rack middleware to help you, as a teapot, comply with HTCPCP/1.0: the Hyper Text Coffee Pot Control Protocol"
  spec.description   = spec.summary
  spec.authors       = ["Tim Lucas"]
  spec.email         = ["t.lucas@toolmantim.com"]
  spec.homepage      = "http://github.com/toolmantim/teapot"
  spec.license       = "WTFPL"
  spec.required_ruby_version = ">= 3.0"
  spec.files         = [
    "Changelog.rdoc",
    "License",
    "Readme.rdoc",
    "teapot.gemspec",
    "lib/teapot.rb",
    "test/test_teapot.rb"
  ]
  spec.require_paths = ["lib"]
end

