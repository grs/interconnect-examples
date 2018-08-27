Creates a router deployment where both the inter-router traffic and
clients are secured by TLS authentication. A different CA is used for
each.

The deploymentconfig created expects there to be an imagestream called
amq-interconnect-12-openshift. The default is to expect this in the
openshift namespace, but that can be overridden as a parameter to the
template.

It expects a secret holding the CA with which valid client signatures
are signed. The name of this secret is assumed to be client-ca by
default, but that may also be passed to the template.

It also expects a secret holding the certs and key required for
inter-router TLS. The name of this secret is assumed to be
inter-router-certs by default, but that may also be passed to the
template.

The provision and deprovision scripts show a full example setup with
a dummy ca for both inter-router and client authentication.