pkgname = "luajit"
pkgver = "2.1.0_beta3"
pkgrel = 0
build_style = "makefile"
configure_args = [
    "--prefix=/usr"
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "Just-in-time compiler and drop-in replacement for Lua 5.1"
maintainer = "vazub <chimera@zubko.cc>"
license = "MIT"
url = "https://luajit.org"
source = f"{url}/download/LuaJIT-2.1.0-beta3.tar.gz"
sha256 = "1ad2e34b111c802f9d0cdf019e986909123237a28c746b21295b63c9e785d9c3"
hardening = ["vis", "cfi", "cfi-genptr", "cfi-icall"]
#No test suite
options = ["lto", "!check"]
    
@subpackage("luajit-devel")
def _devel(self):
    return self.default_devel()
