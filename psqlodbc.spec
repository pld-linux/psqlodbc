#
# --with-iodbc build with iodbc support

%bcond_with iodbc    # use iodbc instead of unix-odbc

Summary:	ODBC interface to PostgreSQL
Summary(es):	Driver ODBC para acceder un servidor PostgreSQL
Summary(pl):	Interfejs ODBC do PostgreSQL
Summary(pt_BR):	Driver ODBC necess醨io para acessar um servidor PostgreSQL
Summary(zh_CN):	用 ODBC 访问 一个 PostgreSQL 数据库的 ODBC 驱动
Name:		psqlodbc
Version:	7.2.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.us.postgresql.org/odbc/versions/src/%{name}-%{version}.tar.gz
# Source0-md5:	701c7c55831652d35937c2efaeaab26d
URL:		http://gborg.postgresql.org/project/psqlodbc/projdisplay.php
BuildRequires:	postgresql-devel
%{?!with_iodbc:BuildRequires:  unixODBC-devel}
%{?with_iodbc:BuildRequires:  libiodbc-devel}
%{?with_iodbc:Requires:	libiodbc}

Obsoletes:	postgresql-odbc
Obsoletes:	postgresql-odbc-devel
Obsoletes:	postgresql-odbc-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes library for interface ODBC.
%{?with_iodbc:This rpm uses libiODBC}

%description -l es
Driver para acceder un servidor PostgreSQL, a trav閟 de ODBC.
%{?with_iodbc:This rpm uses libiODBC}

%description -l pl
Pakiet ten zawiera biblioteki dla interfejsu ODBC.
%{?with_iodbc:Ta paczka rpm u縴wa libiODBC}

%description -l pt_BR
Driver ODBC necess醨io para acessar um servidor PostgreSQL.
%{?with_iodbc:This rpm uses libiODBC}

%prep
%setup -q

%build
%configure \
%{?with_iodbc:	--with-iodbc}
#	--with-unixodbc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.unix notice.txt
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_datadir}/%{name}
