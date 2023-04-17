# no man page: need to run "hugo gen man"
# no shell completion: need to run "hugo completion [bash|zsh|fish]"
pkgname = "hugo"
pkgver = "0.111.3"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
go_build_tags = ["extended"]
pkgdesc = "Fast & Modern Static Website Engine"
license = "Apache-2.0"
url = "https://gohugo.io"
source = f"https://github.com/gohugoio/hugo/archive/v{pkgver}.tar.gz"
sha256 = "b6eeb13d9ed2e5d5c6895bae56480bf0fec24a564ad9d17c90ede14a7b240999"
# required for sacss support (along with "extended" tag), especially on crossbuild
env = { "CGO_ENABLED": "1" }
# testing unchecked yet (see upstream's makefile.go)
options = ["!check"]
