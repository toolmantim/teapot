TEAPOT_GEM_SPEC = Gem::Specification.new do |s|
  s.name     = "teapot"
  s.version  = "1.0"
  s.date     = "2009-01-15"
  s.summary  = s.description = "Rack middleware to help you, as a teapot, comply with HTCPCP/1.0: the Hyper Text Coffee Pot Control Protocol"
  s.email    = "t.lucas@toolmantim.com"
  s.homepage = "http://github.com/toolmantim/teapot"
  s.has_rdoc = true
  s.authors  = ["Tim Lucas"]
  s.files    = ["CHANGELOG.rdoc",
                "LICENSE",
                "README.rdoc",
                "teapot.gemspec",
                "lib/teapot.rb",
                "test/test_teapot.rb"]
  s.rdoc_options = ["--main", "README.rdoc"]
  s.extra_rdoc_files = ["CHANGELOG.rdoc", "README.rdoc"]
end
