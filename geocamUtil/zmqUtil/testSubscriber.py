#!/usr/bin/env python
# __BEGIN_LICENSE__
#Copyright (c) 2015, United States Government, as represented by the 
#Administrator of the National Aeronautics and Space Administration. 
#All rights reserved.
# __END_LICENSE__

import logging

from zmq.eventloop import ioloop
ioloop.install()

from geocamUtil.zmqUtil.util import zmqLoop
from geocamUtil.zmqUtil.subscriber import ZmqSubscriber


def handleGreeting(topic, body):
    print 'received: %s' % body


def main():
    import optparse
    parser = optparse.OptionParser('usage: %prog')
    ZmqSubscriber.addOptions(parser, 'testSubscriber')
    opts, args = parser.parse_args()
    if args:
        parser.error('expected no args')
    logging.basicConfig(level=logging.DEBUG)

    # set up networking
    s = ZmqSubscriber(**ZmqSubscriber.getOptionValues(opts))
    s.start()

    # subscribe to the message we want
    s.subscribeRaw('geocamUtil.greeting:', handleGreeting)

    zmqLoop()


if __name__ == '__main__':
    main()
