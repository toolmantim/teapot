require 'rake/testtask'
require 'rdoc/task'
require 'rubygems/package_task'

task :default => [:test]

Rake::TestTask.new { |t|
  t.pattern = 'test/test_*.rb'
  t.verbose = true
  t.warning = true
}

RDoc::Task.new do |rd|
  rd.main = "Readme.rdoc"
  rd.rdoc_files.include("Readme.rdoc", "lib/*.rb", "License", "Changelog.rdoc")
  rd.rdoc_dir = "doc"
end

spec = Gem::Specification.load('teapot.gemspec')

Gem::PackageTask.new(spec) do |package|
  package.need_zip = true
  package.need_tar = true
end

require 'rake/clean'
CLEAN.include('pkg')
CLEAN.include('doc')
