pkgname = "libbsd"
pkgver = "0.11.7"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--prefix=/usr"
]
hostmakedepends = ["pkgconf", "gsed"]
makedepends = ["libmd-devel", "linux-headers"]
depends = ["libmd"]
pkgdesc = "Provides useful functions commonly found on BSD systems"
maintainer = "vazub <chimera@zubko.cc>"
license = "BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND MIT AND ISC AND Beerware AND custom:BSD-5-Clause AND custom:none"
url = "https://libbsd.freedesktop.org"
source = f"{url}/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "9baa186059ebbf25c06308e9f991fda31f7183c0f24931826d83aa6abd8a0261"
# FIXME: investigate 1 test failure (ntest)
options = ["lto", "!check"]
exec_wrappers = [
    ("/usr/bin/gsed", "sed")
]
    
def post_install(self):
    self.install_license("COPYING")

@subpackage("libbsd-devel")
def _devel(self):
    return self.default_devel()
