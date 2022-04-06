#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-acme
Version  : 1.26.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/34/39/de2b128948d82accbc83d8407ef68f538853246c4bf874f55420e18c8900/acme-1.26.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/34/39/de2b128948d82accbc83d8407ef68f538853246c4bf874f55420e18c8900/acme-1.26.0.tar.gz
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
%setup -q -n acme-1.26.0
cd %{_builddir}/acme-1.26.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649258458
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-acme
cp %{_builddir}/acme-1.26.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-acme/d095fa0d394cc9417a65aecd0d28e7d10e762f98
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

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
