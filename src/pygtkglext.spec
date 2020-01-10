# -*- rpm-spec -*-

%define base_version		1.1.0
%define api_version		1.0
%define rel			1

%define gtkglext_req_version	1.0.0

Summary: Python Bindings for GtkGLExt
Name: pygtkglext
Version: %{base_version}
Release: %{rel}
License: LGPL
Group: Development/Languages
URL: http://gtkglext.sourceforge.net/
Source0: ftp://dl.sourceforge.net/pub/sourceforge/gtkglext/pygtkglext-%{version}.tar.gz
BuildRoot: %{_tmppath}/pygtkglext-%{version}-root

Requires: gtkglext >= %{gtkglext_req_version}
Requires: pygtk2
Requires: gtk2
Requires: XFree86-libs
Requires: python >= 2.2

BuildRequires: gtkglext-devel >= %{gtkglext_req_version}
BuildRequires: pygtk2-devel
BuildRequires: gtk2-devel
BuildRequires: XFree86-devel
BuildRequires: python-devel >= 2.2
BuildRequires: pkgconfig

%description
PyGtkGLExt is Python language bindings for GtkGLExt, OpenGL Extension to GTK.
It enables Python programmers to write OpenGL applications with PyGTK2.

%prep
%setup -q -n pygtkglext-%{version}

%build
[ -x /usr/bin/python2.2 ] && export PYTHON=/usr/bin/python2.2
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)

%doc AUTHORS COPYING COPYING.LIB ChangeLog NEWS README
%{_libdir}/python?.?/site-packages/gtk-2.0/gtk/gdkgl
%{_libdir}/python?.?/site-packages/gtk-2.0/gtk/gtkgl
%{_libdir}/pkgconfig/*
%{_datadir}/pygtk/2.0/defs/*

%changelog
* Sun Aug 31 2003 Naofumi Yasufuku <naofumi@users.sourceforge.net>
- Updated source URL.

* Sun May 11 2003 Naofumi Yasufuku <naofumi@users.sourceforge.net>
- Initial build.


