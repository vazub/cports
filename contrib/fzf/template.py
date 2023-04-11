pkgname = "fzf"
pkgver = "0.39.0"
pkgrel = 0
build_style = "go"
make_check_args = [
    "github.com/junegunn/fzf/src",
    "github.com/junegunn/fzf/src/algo",
    "github.com/junegunn/fzf/src/tui",
    "github.com/junegunn/fzf/src/util",
]
hostmakedepends = ["go"]
makedepends = ["ncurses-devel"]
pkgdesc = "Command-line fuzzy finder"
license = "MIT"
url = "https://github.com/junegunn/fzf"
source = f"https://github.com/junegunn/fzf/archive/{pkgver}.tar.gz"
sha256 = "ac665ac269eca320ca9268227142f01b10ad5d25364ff274658b5a9f709a7259"

def post_install(self):
    self.install_license("LICENSE")
    self.install_bin("bin/fzf-tmux")
    self.install_man("man/man1/fzf.1")
    self.install_dir("usr/share/vim/vimfiles")
    self.install_file("plugin/fzf.vim", "usr/share/vim/vimfiles")
    self.install_file(
        src = "shell/completion.bash",
        dest = "usr/share/bash-completion/completions",
        name = "fzf"
    )
    self.install_file(
        src = "shell/completion.zsh",
        dest = "usr/share/zsh/site-functions",
        name = "fzf"
    )
