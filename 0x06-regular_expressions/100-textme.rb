#!/usr/bin/env ruby
print ARGV[0].scan(/(?<=from:).[A-Za-z0-9]*/).join
print ','
print ARGV[0].scan(/(?<=to:).[A-Za-z0-9]*/).join
print ','
puts ARGV[0].scan(/(?<=flags:).[A-Za-z0-9:+-]*/).join
