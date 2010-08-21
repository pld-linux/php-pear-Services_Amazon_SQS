# TODO
# - -cli subpackage for CLI tools (bin+config)?
%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Amazon_SQS
%define		_status		beta
%define		_pearname	Services_Amazon_SQS
Summary:	PHP API and tools for Amazon SQS
Summary(pl.UTF-8):	API PHP oraz narzędzia do obsługi Amazon SQS
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	2
License:	Apache v2.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	12ab27143e5681fc190252d9026cdc2b
URL:		http://pear.php.net/package/Services_Amazon_SQS/
BuildRequires:	php-pear-PEAR >= 1:1.7.2-9
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Console_CommandLine >= 1.1.0
Requires:	php-pear-Console_Getopt
Requires:	php-pear-Crypt_HMAC2 >= 0.2.1
Requires:	php-pear-HTTP_Request2 >= 0.1.0
Requires:	php-pear-Net_URL2 >= 0.2.0
Requires:	php-pear-PEAR-core >= 1:1.7.2-9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir		%(pear config-get cfg_dir 2>/dev/null || ERROR)/%{_pearname}

%description
This package provides an object-oriented interface to the Amazon
Simple Queue Service (SQS). Included are client libraries and a
command-line script for managing queues. You will need a set of
web-service keys from Amazon Web Services that have SQS enabled.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten udostępnia zorientowany obiektowo interfejs do usługi
Simple Queue Service (SQS) serwisu Amazon. Dołączone zostały
biblioteki kliencie oraz uruchamiany z linii poleceń skrypt do
zarządzania kolejkami. Do pełnego wykorzystania potrzebny będzie
zestaw kluczy z Amazon Web Services umożliwiających dostęp do usługi
SQS.

a klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

# pear/tests/pearname/tests -> pear/tests/pearname
mv ./%{php_pear_dir}/tests/%{_pearname}/{tests/*,}
rmdir ./%{php_pear_dir}/tests/%{_pearname}/tests

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir},%{_sysconfdir}}
%pear_package_install
install -p {./,$RPM_BUILD_ROOT}%{_bindir}/sqs
cp -a {./,$RPM_BUILD_ROOT}%{_sysconfdir}/sqs.ini

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/Services/Amazon
%{php_pear_dir}/Services/Amazon/SQS.php
%{php_pear_dir}/Services/Amazon/SQS

# - cli?
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sqs.ini
%attr(755,root,root) %{_bindir}/sqs

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/%{_pearname}
