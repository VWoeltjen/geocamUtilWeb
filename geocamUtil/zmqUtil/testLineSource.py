#!/usr/bin/env python
# __BEGIN_LICENSE__
#Copyright (c) 2015, United States Government, as represented by the
#Administrator of the National Aeronautics and Space Administration.
#All rights reserved.
# __END_LICENSE__
# __BEGIN_APACHE_LICENSE__
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
# __END_APACHE_LICENSE__

import logging
import sys
import time


def main():
    import optparse
    parser = optparse.OptionParser('usage: %prog testMessages.txt')
    _opts, args = parser.parse_args()
    if len(args) != 1:
        parser.error('expected exactly 1 arg')
    msgFile = args[0]
    logging.basicConfig(level=logging.DEBUG)

    lines = list(open(msgFile, 'r'))
    while 1:
        for line in lines:
            sys.stdout.write(line)
            sys.stdout.flush()
            time.sleep(0.5)


if __name__ == '__main__':
    main()
