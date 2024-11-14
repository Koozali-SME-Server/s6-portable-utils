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
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
BuildRequires: skalibs 
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
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
> %{name}-%{version}-filelist
#echo "%doc COPYING"  >> %{name}-%{version}-filelist
#--dir <dir> 'attr(755,user,grp)' \
#--file <file> 'attr(755,root,root)' \

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
