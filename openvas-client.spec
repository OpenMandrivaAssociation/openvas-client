Summary: 	Client module for OpenVAS
Name:		openvas-client
Version:	3.0.3
Release:	2
Source0:		http://wald.intevation.org/frs/download.php/561/%name-%version.tar.gz
source1:	.abf.yml
Group:		System/Configuration/Networking
Url:		http://www.openvas.org
License:	GPLv2+
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	openvas-devel >= 3.0
Patch0:		openvas-client-3.0.3-devel.patch

%description
OpenVAS-Client is a successor of NessusClient. The fork happened
with NessusClient CVS HEAD 20070704.

%prep
%setup -q -n %name-%version
%patch0 -p0 -b .devel

%build
%configure2_5x --disable-static --enable-gtk
make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%{_sysconfdir}/openvas/openvas-client_log.conf
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Thu Sep 08 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 3.0.3-1mdv2011.0
+ Revision: 698905
- 3.0.3
  P0 to fix some devel .h files

* Sun Nov 28 2010 Funda Wang <fwang@mandriva.org> 3.0.2-1mdv2011.0
+ Revision: 602181
- new version 3.0.2

* Sun Dec 20 2009 Funda Wang <fwang@mandriva.org> 3.0.0-1mdv2010.1
+ Revision: 480337
- drop link against crypto
- openssl is not needed any more
- New version 3.0.0

* Thu Oct 01 2009 Funda Wang <fwang@mandriva.org> 2.0.5-1mdv2010.0
+ Revision: 452250
- New verrsion 2.0.5
- new Group
- import openvas-client


