Name: x11-driver-video-xgi
Version: 1.6.1
Release: 1
Summary: X.org driver for XGI Cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-xgi-%{version}.tar.bz2
Patch1: 0001-Ensure-XGI-DriverRec-and-xgiModuleData-XF86ModuleDat.patch
Patch2: string-format-error.patch
Patch3: 0002-Remove-xf86-LoaderRe-q-f-Sym-bols-Lists-and-their-sy.patch

BuildRequires: x11-util-macros		>= 1.1.5
BuildRequires: libdrm-devel		>= 2.3.0
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: x11-server-devel		>= 1.4
BuildRequires: pkgconfig(gl)		>= 7.0.2
Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-xgi is the X.org driver for Generic XGI Cards.

%prep
%setup -qn xf86-video-xgi-%{version}
%autopatch -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/xgi_drv.so
%{_mandir}/man4/xgi.*

