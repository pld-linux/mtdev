Summary:	Multitouch devices
Name:		mtdev
Version:	1.1.2
Release:	0.1
License:	MIT (X11)
Group:		Applications/System
Source0:	http://bitmath.org/code/mtdev/%{name}-%{version}.tar.bz2
# Source0-md5:	d9c7700918fc392e29da7477ae20c5c2
URL:		http://bitmath.org/code/mtdev/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mtdev is a stand-alone library which transforms all variants of
kernel MT events to the slotted type B protocol. The events put into
mtdev may be from any MT device, specifically type A without contact
tracking, type A with contact tracking, or type B with contact
tracking. See the kernel documentation for further details.

%package devel
Summary:	Header files for mtdev library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
mtdev-devel contains header files for use with mtdev library

%package static
Summary:	Static mtdev libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
mtdev-static contains development static libraries for use
with mtdev library


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

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_libdir}/libmtdev.so.1.0.0
%{_bindir}/mtdev-test

%files devel
%defattr(644,root,root,755)
%{_libdir}/libmtdev.la
%{_includedir}/mtdev*
%{_pkgconfigdir}/mtdev.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmtdev.a
