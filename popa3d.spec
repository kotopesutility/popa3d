Name: popa3d
Version: 0.5.9
Release: alt2

Summary: Tiny secure POP3 daemon
License: LGPL
Group: System/Servers
Url: http://www.openwall.com/%name/

%define real_version 0.5.9
%define srcname %name-%real_version
Source: ftp://ftp.openwall.com/pub/projects/%name/%srcname.tar.bz2
Source1: %name-params.h
Source2: %name.pamd
Source3: %name.xinetd
Source4: %name.eps

#Patch0: %name-%real_version-%version.patch
Patch1: %name-0.5-alt-params.patch
Patch2: %name-0.5-alt-libpam_userpass.patch

PreReq: shadow-utils, /var/empty

# Automatically added by buildreq on Fri May 31 2002
BuildRequires: libpam-devel pam_userpass-devel

%description
This is a tiny Post Office Protocol version 3 (POP3) server with
security as its primary design goal.

%prep
%setup -q -n %srcname
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%__install -p -m644 $RPM_SOURCE_DIR/%name.eps .

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
%doc %name.eps

%changelog
* Thu Oct 17 2002 Dmitry V. Levin <ldv@altlinux.org> 0.5.9-alt2
- Added flow control diagram
  (from Owl CanSecWest/core02 / NordU2002 presentation slides).

* Tue Sep 24 2002 Dmitry V. Levin <ldv@altlinux.org> 0.5.9-alt1
- Updated to 0.5.9:
  * Sun Sep 08 2002 Solar Designer <solar@owl.openwall.com>
  - Avoid non-ANSI/ISO C constructs.
  - Deal with file sizes beyond what will fit in unsigned long reasonably.
  * Fri Aug 02 2002 Solar Designer <solar@owl.openwall.com>
  - Use unsigned integer types where integer overflows are possible and
  post-checked for; ISO C 99 leaves the behavior on integer overflow for
  signed integer types undefined.
  - Use unsigned long for file and message sizes and file offsets.
  * Sun Jun 30 2002 Solar Designer <solar@owl.openwall.com>
  - Mention "POP3" in ".SH NAME" in the man page such that "apropos POP3"
  will catch it, as suggested by Phil Pennock.
  * Sat Jun 22 2002 Solar Designer <solar@owl.openwall.com>
  - Style change with plural form of abbreviations (ID's -> IDs) in the
  documentation and source code comments.

* Fri May 31 2002 Dmitry V. Levin <ldv@altlinux.org> 0.5.1.2-alt1
- Updated to 0.5.1.2:
  * Mon May 27 2002 Solar Designer <solar@owl.openwall.com>
  - Workaround a bug in certain versions of Microsoft Outlook Express
  (reported) where the client would abort on body-less messages which are
  lacking a blank line after the headers (valid per RFC 822, 2822).
  * Sat May 25 2002 Solar Designer <solar@owl.openwall.com>
  - Relaxed the overflow check with strtol() to what really is needed
  to solve the interoperability problem reported by Yury Trembach on
  fido7.ru.unix.

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
