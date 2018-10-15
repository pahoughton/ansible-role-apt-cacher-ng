# 2018-10-14 (cc) <paul4hough@gmail.com>
#
# 2018-10-14 (cc) <paul4hough@gmail.com>
#
$runstart = Time.now
runtimes_fn = "#{Dir.pwd}/rake.test.runtimes.out"

at_exit {
  runtime = Time.now - $runstart
  sh "date '+%F-%X molecule test stop' >> #{runtimes_fn} "
  # clean output stored raw
  # sh "tail -50 < #{runtimes_fn} | sed \"s,\\x1B\\[[0-9;]*[a-zA-Z],,g\" "
  puts "run time: #{runtime}"
}

task :default => [:test,]

task :test do
  sh "date '+%F-%X molecule test start' >> #{runtimes_fn}"
  sh "molecule test "
end
task :testdetails do
  sh "date '+%F-%X molecule test start' >> #{runtimes_fn}"
  sh "molecule test >> #{runtimes_fn} 2>&1"
end
