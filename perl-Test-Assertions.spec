#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Test-Assertions
Version  : 1.054
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/B/BB/BBC/Test-Assertions-1.054.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BB/BBC/Test-Assertions-1.054.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtest-assertions-perl/libtest-assertions-perl_1.054-3.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-Test-Assertions-license = %{version}-%{release}
Requires: perl-Test-Assertions-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Log::Trace)
BuildRequires : perl(Test::More)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Test::Assertions v1.054
(c) BBC 2004, 2005. This program is free software; you can redistribute it and/or modify it under the GNU GPL.

%package dev
Summary: dev components for the perl-Test-Assertions package.
Group: Development
Provides: perl-Test-Assertions-devel = %{version}-%{release}
Requires: perl-Test-Assertions = %{version}-%{release}

%description dev
dev components for the perl-Test-Assertions package.


%package license
Summary: license components for the perl-Test-Assertions package.
Group: Default

%description license
license components for the perl-Test-Assertions package.


%package perl
Summary: perl components for the perl-Test-Assertions package.
Group: Default
Requires: perl-Test-Assertions = %{version}-%{release}

%description perl
perl components for the perl-Test-Assertions package.


%prep
%setup -q -n Test-Assertions-1.054
cd %{_builddir}
tar xf %{_sourcedir}/libtest-assertions-perl_1.054-3.debian.tar.xz
cd %{_builddir}/Test-Assertions-1.054
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Test-Assertions-1.054/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Assertions
cp %{_builddir}/Test-Assertions-%{version}/COPYING %{buildroot}/usr/share/package-licenses/perl-Test-Assertions/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4 || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Test-Assertions/653140b78590077918e962d5ef3284c7c90b936f || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Assertions.3
/usr/share/man/man3/Test::Assertions::Manual.3
/usr/share/man/man3/Test::Assertions::TestScript.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Assertions/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4
/usr/share/package-licenses/perl-Test-Assertions/653140b78590077918e962d5ef3284c7c90b936f

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
