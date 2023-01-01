%global _debugsource_packages  %{nil}
%global build_no ~136~ubuntu16.04.1
%global __brp_check_rpaths %{nil}

Summary:	A simple GUI for managing Conky config files
Name:		conky-manager
Version:	2.4
Release:	1
Group:		Monitoring
License:	GPLv3+
Url:		https://launchpad.net/conky-manager
Source0:	https://launchpad.net/~teejee2008/+archive/ppa/+files/%{name}_%{version}%{build_no}.tar.xz
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	vala
Requires:	conky
Requires:	lm_sensors
Requires:	hddtemp
Requires:	p7zip

%description
A simple GUI for managing Conky config files. Options for changing themes and
running Conky at startup.

%files -f %name.lang
%doc README AUTHORS TODO
%{_bindir}/conky-manager*
%{_datadir}/applications/conky-manager.desktop
%{_datadir}/appdata/conky-manager.appdata.xml
%{_datadir}/conky-manager/
%{_datadir}/pixmaps/conky-manager.png

#---------------------------------------------------------------------------

%prep
%autosetup -n %{name}-%{version}%{build_no}

# Enable debugging information:
sed -i 's/valac/valac -g/g' src/makefile

%build
%before_configure
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

# locales
%find_lang %name

