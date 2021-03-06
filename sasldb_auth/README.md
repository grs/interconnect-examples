Creates a router deployment where the inter-router traffic is secured
by TLS authentication and clients are authenticated against username
and password pairs stored in a sasldb.

The deploymentconfig created expects there to be an imagestream called
amq-interconnect-12-openshift. The default is to expect this in the
openshift namespace, but that can be overridden as a parameter to the
template.

It expects a secret holding the sasldb. The name of this secret is
assumed to be sasldb by default, but that may also be passed to the
template.

It also expects a secret holding the certs and key required for
inter-router TLS. The name of this secret is assumed to be
inter-router-certs by default, but that may also be passed to the
template.

The provision and deprovision scripts show a full example setup.