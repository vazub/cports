pkgname = "exempi"
pkgver = "2.6.3"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool"]
makedepends = ["boost-devel", "libexpat-devel", "zlib-devel"]
pkgdesc = "Library for easy parsing of XMP metadata"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://libopenraw.freedesktop.org/exempi"
source = f"https://libopenraw.freedesktop.org/download/{pkgname}-{pkgver}.tar.bz2"
sha256 = "b0749db18a9e78cf771737954a838cdcdb1d5415888bac1ba9caf8cba77c656c"
# FIXME cfi
hardening = ["vis", "!cfi"]

# fix up libtool crap for aarch64
def pre_configure(self):
    self.do("autoreconf", "-if")

def post_install(self):
    self.install_license("COPYING")

@subpackage("exempi-devel")
def _devel(self):
    return self.default_devel()
