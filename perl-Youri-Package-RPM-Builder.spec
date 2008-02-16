%define module	Youri-Package-RPM-Builder
%define name	perl-%{module}
%define version 0.1.2
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Build RPM packages
License:	GPL or Artistic
Group:		Development/Other
Url:		http://youri.zarb.org
Source:		http://youri.zarb.org/download/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(RPM4)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(String::ShellQuote)
BuildRequires:	perl-version
Requires:	    perl-version
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
YOURI stands for "Youri Offers an Upload & Repository Infrastucture". It aims
to build tools making management of a coherent set of packages easier.

This module build rpm packages.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Youri
%{_mandir}/man3/*
