#!/usr/bin/env python
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

from __future__ import print_function, unicode_literals
import optparse
from proton import Message, Url
from proton.handlers import MessagingHandler
from proton.reactor import Container

class HelloWorld(MessagingHandler):
    def __init__(self, url, key, cert):
        super(HelloWorld, self).__init__()
        self.server = url
        self.address = url.path
        self.key = key
        self.cert = cert

    def on_start(self, event):
        event.container.ssl.client.set_credentials(self.cert, self.key, None)
        conn = event.container.connect(self.server)
        event.container.create_receiver(conn, self.address)
        event.container.create_sender(conn, self.address)

    def on_sendable(self, event):
        event.sender.send(Message(body="Hello World!"))
        event.sender.close()

    def on_message(self, event):
        print(event.message.body)
        event.connection.close()

parser = optparse.OptionParser(usage="usage: %prog [options]")
parser.add_option("-a", "--address", default="amqps://amq-interconnect-myproject.127.0.0.1.nip.io:443/examples",
                  help="address to use (default %default)")
parser.add_option("-k", "--key-file", default="./client-certs/tls.key",
                  help="TLS key to use (default %default)")
parser.add_option("-c", "--cert-file", default="./client-certs/tls.crt",
                  help="TLS cert to use (default %default)")
opts, args = parser.parse_args()

try:
    Container(HelloWorld(Url(opts.address), str(opts.key_file), str(opts.cert_file))).run()
except KeyboardInterrupt: pass

