#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x447BF683AA3B26C3 (certbot-team@eff.org)
#
Name     : pypi-acme
Version  : 1.29.0
Release  : 15
URL      : https://files.pythonhosted.org/packages/da/17/3ee4578e992cf68d57114bdb50b310f6f91c2db9a1cf006ce959f6715b4a/acme-1.29.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/da/17/3ee4578e992cf68d57114bdb50b310f6f91c2db9a1cf006ce959f6715b4a/acme-1.29.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/da/17/3ee4578e992cf68d57114bdb50b310f6f91c2db9a1cf006ce959f6715b4a/acme-1.29.0.tar.gz.asc
Summary  : ACME protocol implementation in Python
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-acme-license = %{version}-%{release}
Requires: pypi-acme-python = %{version}-%{release}
Requires: pypi-acme-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cryptography)
BuildRequires : pypi(josepy)
BuildRequires : pypi(pyopenssl)
BuildRequires : pypi(pyrfc3339)
BuildRequires : pypi(pytz)
BuildRequires : pypi(requests)
BuildRequires : pypi(requests_toolbelt)
BuildRequires : pypi(setuptools)

%description
ACME protocol implementation in Python

%package license
Summary: license components for the pypi-acme package.
Group: Default

%description license
license components for the pypi-acme package.


%package python
Summary: python components for the pypi-acme package.
Group: Default
Requires: pypi-acme-python3 = %{version}-%{release}

%description python
python components for the pypi-acme package.


%package python3
Summary: python3 components for the pypi-acme package.
Group: Default
Requires: python3-core
Provides: pypi(acme)
Requires: pypi(cryptography)
Requires: pypi(josepy)
Requires: pypi(pyopenssl)
Requires: pypi(pyrfc3339)
Requires: pypi(pytz)
Requires: pypi(requests)
Requires: pypi(requests_toolbelt)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-acme package.


%prep
%setup -q -n acme-1.29.0
cd %{_builddir}/acme-1.29.0
pushd ..
cp -a acme-1.29.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657149944
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-acme
cp %{_builddir}/acme-1.29.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-acme/d095fa0d394cc9417a65aecd0d28e7d10e762f98
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-acme/d095fa0d394cc9417a65aecd0d28e7d10e762f98

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
