Name: x11-driver-video-xgi
Version: 1.5.0
Release: %mkrel 1
Summary: The X.org driver for XGI Cards
Group: Development/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-xgi  xorg/drivers/xf86-video-xgi
# cd xorg/drivers/xf86-video/xgi
# git-archive --format=tar --prefix=xf86-video-xgi-1.5.0/ xf86-video-xgi-1.5.0 | bzip2 -9 > xf86-video-xgi-1.5.0.tar.bz2
########################################################################
Source0: xf86-video-xgi-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
########################################################################
# git-format-patch xf86-video-xgi-1.5.0..origin/mandriva+gpl
Patch1: 0001-Add-to-.gitignore-to-skip-patch-emacs-droppings.patch
Patch2: 0002-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.1.5-4mdk
BuildRequires: x11-util-modular
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for Generic XGI Cards

%package devel
Summary: Development files for %{name}
Group: Development/X11
License: MIT

%description devel
Development files for %{name}

%prep
%setup -q -n xf86-video-xgi-%{version}

%patch1 -p1
%patch2 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
# Create list of dependencies
x-check-deps.pl
for deps in *.deps; do
    install -D -m 644 $deps %{buildroot}/%{_datadir}/X11/mandriva/$deps
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/xgi_drv.so
%{_mandir}/man4/xgi.*

%files devel
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/*.la
%{_datadir}/X11/mandriva/*.deps
