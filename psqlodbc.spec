#
# Conditional build:
%bcond_with	iodbc		# use iodbc instead of unix-odbc
#
Summary:	ODBC interface to PostgreSQL
Summary(es.UTF-8):	Driver ODBC para acceder un servidor PostgreSQL
Summary(pl.UTF-8):	Interfejs ODBC do PostgreSQL
Summary(pt_BR.UTF-8):	Driver ODBC necessário para acessar um servidor PostgreSQL
Summary(zh_CN.UTF-8):	用 ODBC 访问 一个 PostgreSQL 数据库的 ODBC 驱动
Name:		psqlodbc
Version:	09.03.0210
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	ftp://ftp.postgresql.org/pub/odbc/versions/src/%{name}-%{version}.tar.gz
# Source0-md5:	108bc27c0cfd5cbc5c5f9bd7bb4f7739
URL:		http://psqlodbc.projects.pgfoundry.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.8
%{?with_iodbc:BuildRequires:	libiodbc-devel}
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	postgresql-devel
%{!?with_iodbc:BuildRequires:	unixODBC-devel}
%{?with_iodbc:Requires:	libiodbc}
Obsoletes:	postgresql-odbc
Obsoletes:	postgresql-odbc-devel
Obsoletes:	postgresql-odbc-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes library for interface ODBC.
%{?with_iodbc:This rpm uses libiODBC.}

%description -l es.UTF-8
Driver para acceder un servidor PostgreSQL, a través de ODBC.
%{?with_iodbc:This rpm uses libiODBC.}

%description -l pl.UTF-8
Pakiet ten zawiera biblioteki dla interfejsu ODBC.
%{?with_iodbc:Ten pakiet rpm używa libiODBC.}

%description -l pt_BR.UTF-8
Driver ODBC necessário para acessar um servidor PostgreSQL.
%{?with_iodbc:This rpm uses libiODBC.}

%prep
%setup -q

%build
# Note: --enable-gss and --enable-krb5 require private symbols from libpq;
# GSS and KRB5 auth are available anyway through libpq mechanisms
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_iodbc:--with-iodbc} \
	%{!?with_iodbc:--with-unixodbc}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/psqlodbcw.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme.txt docs/*
%attr(755,root,root) %{_libdir}/psqlodbcw.so
