pkgname = "samurai"
pkgver = "1.2"
pkgrel = 0
build_style = "makefile"
configure_args = [
    "--prefix=/usr"
]
hostmakedepends = ["pkgconf"]
provides = ["ninja"]
replaces = ["ninja"]
pkgdesc = "Ninja-compatible build tool written in C"
maintainer = "vazub <chimera@zubko.cc>"
license = "ISC AND Apache-2.0 AND MIT"
url = "https://github.com/michaelforney/samurai"
source = f"https://github.com/michaelforney/{pkgname}/releases/download/1.2/{pkgname}-{pkgver}.tar.gz"
sha256 = "3b8cf51548dfc49b7efe035e191ff5e1963ebc4fe8f6064a5eefc5343eaf78a5"
hardening = ["vis", "cfi", "cfi-genptr", "cfi-icall"]
#No test suite
options = ["lto", "!check"]

def post_install(self):
    self.install_link("samu", "usr/bin/ninja")
