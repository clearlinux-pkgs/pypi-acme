#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-acme
Version  : 2.7.0
Release  : 34
URL      : https://files.pythonhosted.org/packages/53/fe/d25df0985f17d48fbe5ae2aa7281152693bf6f70727a0f5031d2656fd616/acme-2.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/53/fe/d25df0985f17d48fbe5ae2aa7281152693bf6f70727a0f5031d2656fd616/acme-2.7.0.tar.gz
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
BuildRequires : pypi(setuptools)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-acme package.


%prep
%setup -q -n acme-2.7.0
cd %{_builddir}/acme-2.7.0
pushd ..
cp -a acme-2.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1696430046
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-acme
cp %{_builddir}/acme-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-acme/d095fa0d394cc9417a65aecd0d28e7d10e762f98 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
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
