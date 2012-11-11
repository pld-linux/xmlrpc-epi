# TODO:
# - fix group for -progs subpackage
Summary:	XML-RPC EPI library - an implementation of the xmlrpc protocol
Summary(pl.UTF-8):	Biblioteka XML-RPC EPI - implementacja protokołu xmlrpc
Name:		xmlrpc-epi
Version:	0.54.1
Release:	3
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/xmlrpc-epi/%{name}-%{version}.tar.gz
# Source0-md5:	546ce341e7d79691371344449cb9e484
URL:		http://xmlrpc-epi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	%{_prefix}/include/%{name}

%description
xmlrpc-epi is an implementation of the xmlrpc protocol in C. It
provides an easy to use API for developers to serialize RPC requests
to and from XML. It doesn't include a transport layer, such as HTTP.
The API is primarily based upon proprietary code written for internal
usage at Epinions.com, and was later modified to incorporate concepts
from the xmlrpc protocol. It passed the xmlrpc validation test suite
in December 2000.

%description -l pl.UTF-8
xmlrpc-epi to implementacja protokołu xmlrpc napisana w C. Daje proste
w użyciu API dla programistów do serializacji żądań RPC do i z XML-a.
Nie zawiera warstwy transportowej typu HTTP. API bazuje głównie na
własnościowym kodzie napisanym do użytku wewnętrznego na Epinions.com
i zostało później zmodyfikowane, aby włączyć idee protokołu xmlrpc.
API to przeszło test sprawdzający poprawność implementacji w grudniu
2000.

%package devel
Summary:	Header files etc to develop XML-RPC applications
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia aplikacji XML-RPC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	expat-devel

%description devel
Header files etc needed to develop XML-RPC applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do tworzenia aplikacji używających XML-RPC.

%package static
Summary:	Static XML-RPC EPI libraries
Summary(pl.UTF-8):	Biblioteki statyczne XML-RPC EPI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XML-RPC EPI libraries.

%description static -l pl.UTF-8
Biblioteki statyczne XML-RPC EPI.

%package progs
Summary:	XML-RPC sample programs
Summary(pl.UTF-8):	Programy przykładowe XML-RPC
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description progs
Sample programs for XML-RPC EPI library.

%description progs -l pl.UTF-8
Programy przykładowe do biblioteki XML-RPC EPI.

%prep
%setup -q -n xmlrpc

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--program-prefix=xmlrpc-epi-
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmlrpc-epi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlrpc-epi.so.0

%files devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libxmlrpc-epi.so
%{_libdir}/libxmlrpc-epi.la
%{_includedir}

%files static
%defattr(644,root,root,755)
%{_libdir}/libxmlrpc-epi.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmlrpc-epi-*
