require 'rake/testtask'
require 'rake/rdoctask'
require 'rake/gempackagetask'

task :default => [:test]

Rake::TestTask.new { |t|
  t.pattern = 'test/test_*.rb'
  t.verbose = true
  t.warning = true
}

Rake::RDocTask.new do |rd|
  rd.main = "Readme.rdoc"
  rd.rdoc_files.include("Readme.rdoc", "lib/*.rb", "License", "Changelog.rdoc")
  rd.rdoc_dir = "doc"
end

load File.join(File.dirname(__FILE__), "teapot.gemspec")

Rake::GemPackageTask.new(TEAPOT_GEM_SPEC) do |package|
  package.need_zip = true
  package.need_tar = true
end

require 'rake/clean'
CLEAN.include('pkg')
CLEAN.include('doc')
