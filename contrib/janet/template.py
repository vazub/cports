pkgname = "janet"
pkgver = "1.27.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Dynamic Lisp dialect and bytecode VM"
maintainer = "vazub <chimera@zubko.cc>"
license = "MIT"
url = "https://janet-lang.org"
source = f"https://github.com/{pkgname}-lang/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "a81c8750844323eb73aea064db9c467aa3361a03fc6f251d3e19a473b147082d"
hardening = ["vis"]
options = ["lto"]
    
def post_install(self):
    self.install_files("examples", "usr/share/janet")

@subpackage("janet-devel")
def _devel(self):
    return self.default_devel() 

