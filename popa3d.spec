Name: popa3d
Version: 0.5.1
Release: alt1

Summary: tiny secure POP3 daemon
License: LGPL
Group: System/Servers
Url: http://www.openwall.com/%name/

Source: ftp://ftp.openwall.com/pub/projects/%name/%name-%version.tar.bz2
Source1: %name-params.h
Source2: %name.pamd
Source3: %name.xinetd

Patch1: %name-0.5-alt-params.patch
Patch2: %name-0.5-alt-libpam_userpass.patch

PreReq: shadow-utils, /var/empty

# Automatically added by buildreq on Wed Dec 26 2001
BuildRequires: libpam-devel pam_userpass-devel

%description
This is a tiny Post Office Protocol version 3 (POP3) server with
security as its primary design goal.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
make clean
%make_build \
	CFLAGS="-c $RPM_OPT_FLAGS %optflags_notraceback -DHAVE_PROGNAME" \
	LIBS="-lpam -lpam_userpass"

%install
install -pD -m750 %name $RPM_BUILD_ROOT%_sbindir/%name
install -pD -m600 %SOURCE2 $RPM_BUILD_ROOT%_sysconfdir/pam.d/%name
install -pD -m640 %SOURCE3 $RPM_BUILD_ROOT%_sysconfdir/xinetd.d/%name

%post
/usr/sbin/groupadd -r -f %name >/dev/null 2>&1
/usr/sbin/useradd -r -g %name -d /dev/null -s /dev/null -n %name >/dev/null 2>&1 ||:

%files
%_sbindir/%name
%config(noreplace) %_sysconfdir/pam.d/%name
%config(noreplace) %_sysconfdir/xinetd.d/*
%doc DESIGN DESIGN VIRTUAL

%changelog
* Wed Apr 17 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.5.1-alt1
- Updated to 0.5.1:
  * Tue Apr 02 2002 Solar Designer <solar@owl.openwall.com>
  - Let the local delivery agent help generate unique ID's by setting
    the X-Delivery-ID: header.

* Mon Mar 25 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.5.0.3-alt1
- Updated to 0.5.0.3:
  * Fri Mar 22 2002 Solar Designer <solar@owl.openwall.com>
  - Re-worked all of the UIDL calculation, adding support for
    multi-line headers and re-considering which headers to use.

* Tue Jan 08 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.5-alt2
- Fixed my typo in pamd file made in previous package revision.

* Wed Dec 26 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.5-alt1
- 0.5.
- Added libpam_userpass support.

* Fri Oct 13 2000 Dmitry V. Levin <ldv@fandra.org> 0.4-ipl2
- Updated:
  + pam configuration;
  + rewritten xinet support, dropped inet support.

* Fri Feb 25 2000 Dmitry V. Levin <ldv@fandra.org>
- 0.4
- Added PAM authentication.

* Tue Sep 23 1999 Dmitry V. Levin <ldv@fandra.org>
- Initial revision.
