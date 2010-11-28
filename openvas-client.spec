Summary: 	Client module for OpenVAS
Name:		openvas-client
Version:	3.0.2
Release:	%mkrel 1
Source:		http://wald.intevation.org/frs/download.php/561/%name-%version.tar.gz
Group:		System/Configuration/Networking
Url:		http://www.openvas.org
License:	GPLv2+
BuildRoot:	%{_tmppath}/%name-%{version}-root
BuildRequires:	gtk+2-devel
BuildRequires:	openvas-devel >= 3.0

%description
OpenVAS-Client is a successor of NessusClient. The fork happened
with NessusClient CVS HEAD 20070704.

%prep
%setup -q -n %name-%version

%build
%configure2_5x --disable-static --enable-gtk
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sysconfdir}/openvas/openvas-client_log.conf
%{_bindir}/*
%{_mandir}/man1/*
