#!/usr/bin/perl
# __BEGIN_LICENSE__
# Copyright (c) 2015, United States Government, as represented by the Administrator of the National Aeronautics and Space Administration. All rights reserved.
#
# The “xGDS” platform is licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
# __END_LICENSE__


use strict;
use warnings;

use File::Slurp;
use File::Basename;

my %comment = (
    ".ac"   => "dnl",
    ".am"   => "#",
    ".cc"   => "//",
    ".cpp"  => "//",
    ".css"  => "/*",
    ".cxx"  => "//",
    ".oldtest"  => "//",
    ".hpp"  => "//",
    ".cg"   => "//",
    ".glsl" => "//",
    ".h"    => "//",
    ".hh"   => "//",
    ".i"    => "//",
    ".m4"   => "dnl",
    ".mak"  => "#",
    ".pl"   => "#",
    ".py"   => "#",
    ".sh"   => "#",
    ".js"   => "//",
    ".tcc"  => "//",
    ".rst"  => ".. o ",
    ".java" => "//",
    ".aidl" => "//",
    ".xml" => "<!--,-->",
);

my %atEnd = (
    ".rst" => 1,
    ".css"  => "*/",
    
);

# Read the license text from __DATA__ by default
my $f = \*DATA;
$f = $ARGV[0] if @ARGV > 0;

my @license = read_file($f);
my $shebang = '';

@license = map { chop; $_; } @license;

# process each line given on stdin
foreach my $filename (<>) {
    chomp $filename;

    # get the extension, and skip it if we don't know about it
    my (undef, undef, $ext) = fileparse($filename, qr/\.[^.]*/);

    unless (exists $comment{$ext}) {
        warn "Skipped $filename\n";
        next;
    }

    my $file = read_file($filename);

    next if ($file =~ /^\s*$/);
    next if ($file =~ /__NO_RELICENSE__/);

    $shebang = '';
    # Protect a shebang line, xml declaration, or emacs mode line
    if ($file =~ s/^(#!.*\n)//) {
        if (defined($1)) {
            $shebang = $1;
        }
    } elsif ($file =~ s/^(<\?xml.*\n)//) {
        if (defined($1)) {
            $shebang = $1;
        }
    } elsif ($file =~ s/^([^\n]*-\*-[^\n]*-\*-[^\n]*\n)//) {
        if (defined($1)) {
            $shebang = $1;
        }
    }

    # Remove a license header if it exists
    $file =~ s/^[^\n]*__BEGIN_LICENSE__.*?__END_LICENSE__[^\n]*$//ms;

    my ($chead, $ctail);
    if ($comment{$ext} =~ /,/) {
        ($chead, $ctail) = split(/,/, $comment{$ext});
        $ctail = " " . $ctail;
    } else {
        ($chead, $ctail) = ($comment{$ext}, "");
    }

    # wrapping each line of the license in the comment head and tail strings
    my $wrappedLicense = $chead . join($ctail . "\n" . $chead, @license) . $ctail;
    if ($atEnd{$ext}) {
        # Remove all blank lines from the bottom of the file
        while ($file =~ s/\s*\n$//) {};

        # append the wrapped license
        $file = $shebang . $file . "\n\n" . $wrappedLicense . "\n";
    } else {
        # Remove all blank lines from the top of the file
        while ($file =~ s/^\s*\n//) {};

        # prepend the wrapped license
        $file = $shebang . $wrappedLicense . "\n\n" . $file;
    }

    write_file($filename, $file);
}

#__BEGIN_SIMPLE_LICENSE__
#Copyright (c) 2015, United States Government, as represented by the
#Administrator of the National Aeronautics and Space Administration.
#All rights reserved.
#__END_SIMPLE_LICENSE__

# __BEGIN_LICENSE__
#Copyright (c) 2015, United States Government, as represented by the 
#Administrator of the National Aeronautics and Space Administration. 
#All rights reserved.
#
#The xGDS platform is licensed under the Apache License, Version 2.0 
#(the "License"); you may not use this file except in compliance with the License. 
#You may obtain a copy of the License at 
#http://www.apache.org/licenses/LICENSE-2.0.
#
#Unless required by applicable law or agreed to in writing, software distributed 
#under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR 
#CONDITIONS OF ANY KIND, either express or implied. See the License for the 
#specific language governing permissions and limitations under the License.
# __END_LICENSE__
 
__DATA__
 __BEGIN_LICENSE__
Copyright (c) 2015, United States Government, as represented by the 
Administrator of the National Aeronautics and Space Administration. 
All rights reserved.
 __END_LICENSE__
