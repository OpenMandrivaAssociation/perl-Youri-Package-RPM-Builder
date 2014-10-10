%define upstream_name		Youri-Package-RPM-Builder
%define upstream_version	0.3.0

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7
Summary:	Build RPM packages
License:	GPL or Artistic
Group:		Development/Other
Url:		http://youri.zarb.org
Source0:	http://youri.zarb.org/download/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-JSON-PP
BuildRequires:	perl(RPM)
BuildRequires:	perl(Youri::Package::RPM)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(String::ShellQuote)
BuildRequires:	perl(version)
Requires:	perl(version)
BuildArch:	noarch

%description
YOURI stands for "Youri Offers an Upload & Repository Infrastucture". It aims
to build tools making management of a coherent set of packages easier.

This module build rpm packages.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc Changes README
%{perl_vendorlib}/Youri
%{_mandir}/man3/*


%changelog
* Sat Mar 12 2011 Funda Wang <fwang@mandriva.org> 0.3.0-3mdv2011.0
+ Revision: 643944
- rebuild
- rebuild

* Fri Jan 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.0-1
+ Revision: 633678
- new version

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - fix RPM::Problems usage with rpm5
    - fix a part of the code that weren't ported to rpm5 as it weren't covered by the
      regression tests

* Sun Jan 09 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.2.0-3mdv2011.0
+ Revision: 630738
- merge rpm5 branch

* Sun Sep 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-1mdv2010.0
+ Revision: 438984
- new version
- use perl_version macro

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1.2-5mdv2010.0
+ Revision: 430674
- rebuild

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - set TEST_AUTHOR environment variable to enable prereq & perlcritic test

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.1.2-4mdv2009.0
+ Revision: 258923
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.1.2-3mdv2009.0
+ Revision: 246808
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-1mdv2008.1
+ Revision: 109519
- new version
- import perl-Youri-Package-RPM-Builder


