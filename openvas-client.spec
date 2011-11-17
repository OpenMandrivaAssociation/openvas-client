Summary: 	Client module for OpenVAS
Name:		openvas-client
Version:	3.0.3
Release:	%mkrel 2
License:	GPLv2+
Group:		System/Configuration/Networking
URL:		http://www.openvas.org
Source0:	http://wald.intevation.org/frs/download.php/561/%name-%version.tar.gz
Source1:	openvas-client.desktop
Patch0:		openvas-client-3.0.3-devel.patch
#Set for the openvas-client the default port of openvas-scanner instead of 
#openvas manager, untill manager is available for Fedora/RedHat
Patch1:		openvas-client-ports4.patch
BuildRequires:	gtk+2-devel
BuildRequires:	desktop-file-utils
BuildRequires:	openvas-devel >= 3.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
OpenVAS-Client is a successor of NessusClient. The fork happened
with NessusClient CVS HEAD 20070704.

%prep

%setup -q -n %name-%version
%patch0 -p0 -b .devel
%patch1 -p1 -b .ports4

%build
%configure2_5x --disable-static --enable-gtk
make

%install
rm -rf %{buildroot}

%makeinstall_std

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

# cleanup
rm -rf %{buildroot}%{_datadir}/openvas

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/openvas/openvas-client_log.conf
%{_bindir}/OpenVAS-Client
%{_mandir}/man1/OpenVAS-Client.1.*
%{_datadir}/applications/*
