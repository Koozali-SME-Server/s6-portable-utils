%global debug_package %{nil}
%define name s6-portable-utils
%define version 2.3.0.4
%define release 2
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
* Fri Sep 25 2026 Jean-Philippe Pialasse <jpp@koozali.org> 2.3.0.4-2.sme
- allow build for both x86_64 and aarch64

* Wed Nov 13 2024 Jean-Philippe Pialasse <jpp@koozali.org> 2.3.0.4-1.sme
- Initial code - create RPM 

%prep

%setup -q

%build
# Strip out custom target naming formatting for Skarnet's custom engine
%ifarch x86_64
%define skarnet_target x86_64-redhat-linux
%else
%ifarch aarch64
%define skarnet_target aarch64-redhat-linux
%else
%define skarnet_target %{_target_cpu}-redhat-linux
%endif
%endif

sed -e 's/(cat \$sysdeps\/target)/target/' -i configure
./configure --with-sysdeps=%{_libdir}/skalibs/sysdeps --target=%{skarnet_target}
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
