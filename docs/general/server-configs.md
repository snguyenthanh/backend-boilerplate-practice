# Server Configurations

## Nginx

An `production/.nginx.conf` file is included that does the same on an Nginx server.

### security

Additionally, the `.nginx.conf` provides TLS security configuration settings based on [Mozilla's TLS Guidelines](https://wiki.mozilla.org/Security/Server_Side_TLS), including:

- HSTS Header
- TLS 1.2 only
- Prefer server-side ciphersuites
- Strong ciphersuites
- Own DH Key (optional)
- OCSP & SSL Stapling (optional)
