Summary:	XML-RPC library for Erlang
Name:		erlang-xmlrpc
Version:	1.13
Release:	1
License:	BSD
Group:		Development/Languages
Source0:	http://ejabberd.jabber.ru/files/contributions/xmlrpc-%{version}-ipr2.tgz
# Source0-md5:	c1905556e01d8970681b93dcba892442
URL:		http://sourceforge.net/projects/sowap/
BuildRequires:	erlang
BuildRequires:	erlang-xmerl
Requires:	erlang
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an HTTP 1.1 compliant XML-RPC library for Erlang. It is
designed to make it easy to write XML-RPC Erlang clients and/or
servers. The library is compliant with the XML-RPC specification
published by http://www.xmlrpc.org/.

%prep
%setup -q -n xmlrpc-%{version}

%build
xmerldir=$(ls -1d %{_libdir}/erlang/lib/xmerl-* | head -n1)

%{__make} -C src \
	XMERL_PATH=$xmerldir

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/erlang/lib/xmlrpc-%{version}
cp -a ebin src $RPM_BUILD_ROOT%{_libdir}/erlang/lib/xmlrpc-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO doc/*.txt
%{_libdir}/erlang/lib/xmlrpc-*
