%global debug_package %{nil}
%define name s6-portable-utils
%define version 2.3.0.4
%define release 1
Summary: This is what s6-portable-utils does.
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Source: %{name}-%{version}.tar.gz
License: GNU GPL version 2
Group: SMEserver/addon
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
BuildRequires: e-smith-devtools
BuildRequires: skalibs-devel 
Requires: e-smith-release >= 10.0
AutoReqProv: no

%description
local build of https://github.com/skarnet/s6-portable-utils mainly for seekablepipe 

%changelog
* Wed Nov 13 2024 Jean-Philippe Pialasse <jpp@koozali.org> 2.3.0.4-1.sme
- Initial code - create RPM 

%prep

%setup -q

%build
sed -e 's/(cat \$sysdeps\/target)/target/' -i configure
./configure --with-sysdeps=/usr/lib64/skalibs/sysdeps --target=x86_64-redhat-linux
#x86_64-generic-linux-gnu
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR="$RPM_BUILD_ROOT"
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
> %{name}-%{version}-filelist

%clean
cd ..
rm -rf %{name}-%{version}

%pre

%preun

%post

%postun
#uninstall
%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
