# XXX testing status: gmake rebuilds binary
pkgname = "gitea"
pkgver = "1.19.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
makedepends = ["sqlite-devel", "linux-pam-devel"]
depends = ["git"]
checkdepends = ["gmake", "openssh", "git"]
go_build_tags = ["bindata", "sqlite", "pam", "tidb"]
go_ldflags = ["-X", f"main.Version={pkgver}"]
pkgdesc = "Git with a cup of Tea"
license = "MIT"
url = "https://gitea.io"
source = f"https://github.com/go-gitea/gitea/releases/download/v{pkgver}/gitea-src-{pkgver}.tar.gz"
sha256 = "f670f35d2198c58c37e3f1249a3e3855d18b56146c18bd9ee607f2a323d4a864"
# required for crossbuild support
env = { "CGO_ENABLED": "1" }
# some tests fails, some require network access
options = ["!check"]

# testing is overcomplicated, let's use upstream's Makefile
def do_check(self):
    self.do("gmake", "test-backend")

system_users = [
    {
        "name" : "_gitea",
        "id"   : None,
        "home" : "/var/lib/gitea",
        "shell": "/usr/bin/sh",  # proper shell is needed for ssh support
    }
]

def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "gitea.dinit", name = "gitea")
    self.install_file(self.files_path / "app.ini", "etc/gitea/conf", 0o0640)
    self.install_file(
        src = self.files_path / "app.ini",
        dest = "usr/share/gitea/conf",
        name = "app.ini.chimera"
    )
    self.install_file(
        src = "custom/conf/app.example.ini",
        dest = "usr/share/gitea/conf",
        name = "app.ini.upstream"
    )
