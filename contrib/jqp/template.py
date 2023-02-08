pkgname = "jqp"
pkgver = "0.4.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "TUI playground to experiment with jq"
license = "MIT"
url = "https://github.com/noahgorstein/jqp"
source = f"https://github.com/noahgorstein/jqp/archive/v{pkgver}.tar.gz"
sha256 = "0039fe0d17be1931f03dcf236d1b5e280aeffb1070abecfecee3323eb2423d4c"
# upstream provides no tests
options = ["!check"]

def post_install(self):
     self.install_license("LICENSE")
