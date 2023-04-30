pkgname = "jimtcl"
pkgver = "0.82"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--enable-utf8",
    	"--enable-shared",
    	"--docdir=/usr/share/jimtcl"
]
hostmakedepends = ["openssl-devel", "pkgconf"]
pkgdesc = "Small footprint implementation of Tcl"
maintainer = "vazub <chimera@zubko.cc>"
license = "BSD-2-Clause-Views"
url = "http://jim.tcl.tk"
source = f"https://github.com/msteveb/{pkgname}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e8af929b815e4d30e54ff116b2b933e56c00a02b9110529d1a58660b2469aea7"
#FIXME: some test fails with "illegal instruction"
options = ["lto", "!check"]
    
def post_install(self):
    self.install_license("LICENSE")
    
@subpackage("jimtcl-devel")
def _devel(self):
    return self.default_devel()

@subpackage("jimtcl-doc")
def _doc(self):
    return self.default_doc(extra = ["usr/share/jimtcl/Tcl.html",]) 

