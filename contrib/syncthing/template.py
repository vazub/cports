# nb: github tarball doesn't provides vendor/, contrary to the "official" tarball
# XXX runtime status
# XXX packaging status
# XXX subpackages
# XXX testing : via "go run build.go test" ?
# XXX reuse void files/
# XXX cleanup void stuff

pkgname = "syncthing"
pkgver = "1.23.4"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
go_build_tags = ["notupgrade"]
go_ldflags = [ "-X",  f"github.com/syncthing/syncthing/lib/build.Version=v{pkgver}"]
make_build_args = [
    "github.com/syncthing/syncthing/cmd/syncthing",
    "github.com/syncthing/syncthing/cmd/stdiscosrv",
    "github.com/syncthing/syncthing/cmd/strelaysrv",
]
pkgdesc = "Open Source Continuous File Synchronization"
license = "MPL-2.0"
url = "https://syncthing.net"
source = f"https://github.com/syncthing/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "4b68cee85b63fbb197a4e5401b3983a2a2358e1098ff91755f47925a1ee17f58"
# crossbuild unchecked yet
# testing unchecked yet
options = ["!cross", "!check"]

def pre_build(self):
    from cbuild.util import golang
    self.do(
        "go", "generate",
        "github.com/syncthing/syncthing/lib/api/auto",
        "github.com/syncthing/syncthing/cmd/strelaypoolsrv/auto",
        env = golang.get_go_env(self)
    )

#void# post_install() {
#void# 	vinstall etc/firewall-ufw/syncthing 644 etc/ufw/applications.d
#void# 	vinstall etc/linux-desktop/syncthing-start.desktop 664 usr/share/applications
#void# 	vinstall etc/linux-desktop/syncthing-ui.desktop 644 usr/share/applications
#void# 	vlicense LICENSE
#void# 	vdoc README.md
#void# 	for f in man/syncthing*; do vman $f; done
#void# 	for x in 32 64 128 256 512; do
#void# 		vinstall assets/logo-${x}.png 644 "usr/share/icons/hicolor/${x}x${x}/apps" syncthing.png
#void# 	done
#void# 	vinstall assets/logo-only.svg 644 usr/share/icons/hicolor/scalable/apps syncthing.svg
#void# }

def post_install(self):
    self.install_license("LICENSE")

#void# syncthing-relaysrv_package() {
#void# 	short_desc+=" - relay server"
#void# 	license="MIT"
#void# 	replaces="relaysrv>=0.12.18_2"
#void# 	provides="relaysrv-${version}_${revision}"
#void# 	system_accounts="relaysrv"
#void# 	relaysrv_homedir="/var/lib/relaysrv"
#void#
#void# 	make_dirs="
#void# 	 /var/log/relaysrv 700 root root
#void# 	 /var/lib/relaysrv 700 relaysrv relaysrv"
#void#
#void# 	pkg_install() {
#void# 		vmove usr/bin/strelaysrv
#void# 		vlicense cmd/strelaysrv/LICENSE
#void# 		vsv relaysrv
#void# 		vman man/strelaysrv.1
#void# 	}
#void# }

@subpackage("syncthing-relaysrv")
def _relaysrv(self):
    self.pkgdesc = f"{pkgdesc} - relay server"
    self.license = "MIT"
    def install():
        # XXX add license file since distinct from main package
        # XXX add license file ... install_license() forbidden in subpackage
        # XXX system account
        # XXX service file
        # XXX man page
        #ko# self.install_license("cmd/strelaysrv/LICENSE")
        self.take("usr/bin/strelaysrv")
    return install

#void# syncthing-discosrv_package() {
#void# 	short_desc+=" - discovery server"
#void# 	system_accounts="_discosrv"
#void# 	_discosrv_homedir="/var/lib/discosrv"
#void#
#void# 	make_dirs="
#void# 	 /var/log/discosrv 700 root root
#void# 	 /var/lib/discosrv 700 _discosrv _discosrv"
#void#
#void# 	pkg_install() {
#void# 		vmove usr/bin/stdiscosrv
#void# 		vlicense LICENSE
#void# 		vsv discosrv
#void# 		vman man/stdiscosrv.1
#void# 	}
#void# }

@subpackage("syncthing-discosrv")
def _relaysrv(self):
    self.pkgdesc = f"{pkgdesc} - discovery server"
    def install():
        # XXX add license file ... install_license() forbidden in subpackage
        # XXX system account
        # XXX service file
        # XXX man page
        #ko# self.install_license("LICENSE")
        self.take("usr/bin/stdiscosrv")
    return install
