Summary: 	Client module for OpenVAS
Name:		openvas-client
Version:	2.0.3
Release:	%mkrel 1
Source:		http://wald.intevation.org/frs/download.php/561/%name-%version.tar.gz
Patch0:		openvas-client-2.0.3-fix-str-fmt.patch
Group:		System/Configuration/Networking
Url:		http://www.openvas.org
License:	GPLv2+
BuildRoot:	%{_tmppath}/%name-%{version}-root
BuildRequires:	gtk+2-devel
BuildRequires:	openssl-devel
BuildRequires:	openvas-devel >= 2.0

%description
OpenVAS-Client is a successor of NessusClient. The fork happened
with NessusClient CVS HEAD 20070704.

%prep
%setup -q -n %name-%version
%patch0 -p0

%build
%configure2_5x --disable-static --enable-gtk
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
