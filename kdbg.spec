%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg kdbg
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Epoch:			%{tde_epoch}
Version:		2.2.2
Release:		%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:		Graphical debugger interface [Trinity]
Group:			Applications/Utilities
URL:			http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/development/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DCONFIG_INSTALL_DIR=%{_sysconfdir}/trinity
BuildOption:    -DWITH_ALL_OPTIONS=ON -DBUILD_ALL=ON -DBUILD_DOC=ON
BuildOption:    -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}


BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires: libtool m4

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

%description
KDbg is a graphical user interface to gdb, the GNU debugger.  It provides
an intuitive interface for setting breakpoints, inspecting variables,
stepping through code and much more.  KDbg requires TDE but you can of
course debug any program.

KDbg can also debug XSLT (XML stylesheet translation) scripts by
interfacing with xsldbg.  For this the package kxsldbg must be installed.

Features include the following:
* Inspection of variable values in a tree structure.
* Direct member: For certain compound data types the most important
  member values are displayed next to the variable name, so that it is
  not necessary to expand the subtree of that variable in order to see
  the member value.  KDbg can also display Qt's QString values, which
  are Unicode strings.
* Debugger at your finger tips: The basic debugger functions (step,
  next, run, finish, until, set/clear/enable/disable breakpoint) are
  bound to function keys F5 through F10.  Quick and easy.
* View source code, search text, set program arguments and environment
  variables, display arbitrary expressions.
* Debugging of core dumps, attaching to running processes is possible.
* Conditional breakpoints.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_prefix}/bin/kdbg
%{tde_prefix}/share/applications/tde/kdbg.desktop
%{tde_prefix}/share/apps/kdbg/
%config(noreplace) %{_sysconfdir}/trinity/kdbgrc
%lang(de) %{tde_prefix}/share/doc/tde/HTML/de/kdbg/
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/kdbg/
%lang(ru) %{tde_prefix}/share/doc/tde/HTML/ru/kdbg/
%{tde_prefix}/share/icons/hicolor/*/apps/kdbg.png
%{tde_prefix}/share/icons/locolor/*/apps/kdbg.png
%{tde_prefix}/share/man/man1/kdbg.*

