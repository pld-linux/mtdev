Summary:	Multitouch devices
Summary(pl.UTF-8):	Urządzenia multitouch
Name:		mtdev
Version:	1.1.2
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://bitmath.org/code/mtdev/%{name}-%{version}.tar.bz2
# Source0-md5:	d9c7700918fc392e29da7477ae20c5c2
URL:		http://bitmath.org/code/mtdev/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mtdev is a stand-alone library which transforms all variants of
kernel MT events to the slotted type B protocol. The events put into
mtdev may be from any MT device, specifically type A without contact
tracking, type A with contact tracking, or type B with contact
tracking. See the kernel documentation for further details.

%description -l pl.UTF-8
mtdev to samodzielna biblioteka tłumacząca wszystkie warianty zdarzeń
MT z jądra na protokół slotowy typu B. Zdarzenia umieszczane w mtdev
mogą pochodzić z dowolnego urządzenia MT, w szczególności typu A bez
śledzenia kontaktu, typu A ze śledzeniem kontaktu lub typu B ze
śledzeniem kontaktu. Więcej szczegółów w dokumentacji jądra.

%package devel
Summary:	Header files for mtdev library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki mtdev
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for use with mtdev library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do biblioteki mtdev.

%package static
Summary:	Static mtdev library
Summary(pl.UTF-8):	Statyczna biblioteka mtdev
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains mtdev static library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę mtdev.

%package tools
Summary:	Tools for mtdev library
Summary(pl.UTF-8):	Narzędzia do biblioteki mtdev
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description tools
mtdev test tool.

%description tools -l pl.UTF-8
Narzędzie testowe mtdev.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libmtdev.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libmtdev.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmtdev.so
%{_libdir}/libmtdev.la
%{_includedir}/mtdev*.h
%{_pkgconfigdir}/mtdev.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmtdev.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mtdev-test
