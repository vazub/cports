pkgname = "emptty"
pkgver = "0.9.1"
pkgrel = 0
build_style = "go"
make_check_args = [
    "./src",
]
hostmakedepends = ["go", "linux-pam-devel", "libx11-devel"]
pkgdesc = "Dead simple CLI Display Manager on TTY"
maintainer = "vazub <chimera@zubko.cc>"
license = "MIT"
url = "https://github.com/tvrzna/emptty"
source = f"https://github.com/tvrzna/{pkgname}/archive/refs/tags//v{pkgver}.tar.gz"
sha256 = "1b3c940da8d60705306525bf5a7619a7b30d954679e30a978a03ac53357e57d4"
options = ["spdx"]

def post_install(self):
    self.install_man("res/emptty.1")
    self.install_dir("etc/emptty")
    self.install_file("res/conf", "etc/emptty")
    self.install_file("res/motd-gen.sh", "etc/emptty")
    self.install_dir("etc/pam.d")
    self.install_file(
        src = "res/pam",
        dest = "etc/pam.d",
        name = "emptty"
    )
    self.install_service("res/dinit-service", "emptty")
