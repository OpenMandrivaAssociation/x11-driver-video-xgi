Name: x11-driver-video-xgi
Version: 1.6.0
Release: %mkrel 2
Summary: X.org driver for XGI Cards
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-xgi-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-util-macros		>= 1.1.5
BuildRequires: libdrm-devel		>= 2.3.0
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: x11-server-devel		>= 1.4
BuildRequires: libmesagl-devel		>= 7.0.2
BuildRequires: dos2unix
Conflicts: xorg-x11-server < 7.0

Patch1: 0001-Ensure-XGI-DriverRec-and-xgiModuleData-XF86ModuleDat.patch
Patch2: string-format-error.patch

%description
x11-driver-video-xgi is the X.org driver for Generic XGI Cards.

%prep
%setup -q -n xf86-video-xgi-%{version}
# This will make patch maintaining easier:
dos2unix src/xgi_driver.c
%apply_patches

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/xgi_drv.la
%{_libdir}/xorg/modules/drivers/xgi_drv.so
%{_mandir}/man4/xgi.*
