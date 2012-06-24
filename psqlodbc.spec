Summary:	ODBC interface to PostgreSQL
Summary(es):	Driver ODBC para acceder un servidor PostgreSQL
Summary(pl):	Interfejs ODBC do PostgreSQL
Summary(pt_BR):	Driver ODBC necess�rio para acessar um servidor PostgreSQL
Summary(zh_CN):	�� ODBC ���� һ�� PostgreSQL ���ݿ�� ODBC ����
Name:		psqlodbc
Version:	7.2.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.us.postgresql.org/odbc/versions/src/%{name}-%{version}.tar.gz
URL:		http://gborg.postgresql.org/project/%{name}/projdisplay.php
BuildRequires:	postgresql-devel
BuildRequires:	unixODBC-devel
Obsoletes:	postgresql-odbc
Obsoletes:	postgresql-odbc-devel
Obsoletes:	postgresql-odbc-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes library for interface ODBC.

%description -l es
Driver para acceder un servidor PostgreSQL, a trav�s de ODBC.

%description -l pl
Pakiet ten zawiera biblioteki dla interfejsu ODBC.

%description -l pt_BR
Driver ODBC necess�rio para acessar um servidor PostgreSQL.

%prep
%setup -q

%build
%configure \
	--with-unixodbc
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
