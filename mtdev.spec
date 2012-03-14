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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/ciptool
%attr(755,root,root) %{_bindir}/dfutool
%attr(755,root,root) %{_bindir}/dund
%attr(755,root,root) %{_bindir}/gatttool
%attr(755,root,root) %{_bindir}/hcitool
%attr(755,root,root) %{_bindir}/hidd
%attr(755,root,root) %{_bindir}/l2ping
%attr(755,root,root) %{_bindir}/pand
%attr(755,root,root) %{_bindir}/rfcomm
%attr(755,root,root) %{_bindir}/sdptool
%attr(755,root,root) %{_sbindir}/bccmd
%attr(755,root,root) %{_sbindir}/bluetoothd
%attr(755,root,root) %{_sbindir}/hciattach
%attr(755,root,root) %{_sbindir}/hciconfig
%dir %{_libdir}/bluetooth
%dir %{_libdir}/bluetooth/plugins
%dir %{_sysconfdir}/bluetooth
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bluetooth/*.conf
%attr(754,root,root) /etc/rc.d/init.d/bluetooth
%attr(754,root,root) /etc/rc.d/init.d/dund
%attr(754,root,root) /etc/rc.d/init.d/pand
%attr(754,root,root) /etc/rc.d/init.d/rfcomm
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/bluetooth
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/bluetooth.conf
%{systemdunitdir}/bluetooth.service
%{_datadir}/dbus-1/system-services/org.bluez.service
%attr(755,root,root) %{udevdir}/bluetooth_serial
%attr(755,root,root) %{udevdir}/hid2hci
%{udevdir}/rules.d/97-bluetooth.rules
%{udevdir}/rules.d/97-bluetooth-hid2hci.rules
%{udevdir}/rules.d/97-bluetooth-serial.rules
%{_mandir}/man1/ciptool.1*
%{_mandir}/man1/dfutool.1*
%{_mandir}/man1/dund.1*
%{_mandir}/man1/hcitool.1*
%{_mandir}/man1/hidd.1*
%{_mandir}/man1/pand.1*
%{_mandir}/man1/rfcomm.1*
%{_mandir}/man1/sdptool.1*
%{_mandir}/man8/bccmd.8*
%{_mandir}/man8/bluetoothd.8*
%{_mandir}/man8/hciattach.8*
%{_mandir}/man8/hciconfig.8*
%{_mandir}/man8/hid2hci.8*
%{_mandir}/man8/l2ping.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbluetooth.so
%{_includedir}/bluetooth
%{_pkgconfigdir}/bluez.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libbluetooth.a
