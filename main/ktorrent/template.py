pkgname = "ktorrent"
pkgver = "24.12.3"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "kcmutils-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdnssd-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kitemviews-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "kparts-devel",
    "kplotting-devel",
    "kstatusnotifieritem-devel",
    "ktextwidgets-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "libktorrent-devel",
    "phonon-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "solid-devel",
    "syndication-devel",
    "taglib-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE torrent client"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/ktorrent"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/ktorrent-{pkgver}.tar.xz"
sha256 = "a6eb8be915d48aed5dd745d3bec1a0f4462f078448a13242dc94d0cfb94f8f9c"

if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
    makedepends += ["qt6-qtwebengine-devel"]
