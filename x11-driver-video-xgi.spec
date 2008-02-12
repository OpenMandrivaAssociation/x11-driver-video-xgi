Name: x11-driver-video-xgi
Version: 1.5.0
Release: %mkrel 3
Summary: The X.org driver for XGI Cards
Group: Development/X11
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
Conflicts: xorg-x11-server < 7.0

Patch1: 0001-Ensure-XGI-DriverRec-and-xgiModuleData-XF86ModuleDat.patch

%description
The X.org driver for Generic XGI Cards

%prep
%setup -q -n xf86-video-xgi-%{version}

%patch1 -p1

%build
%configure
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
