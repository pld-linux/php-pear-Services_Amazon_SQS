%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Amazon_SQS
%define		_status		alpha
%define		_pearname	Services_Amazon_SQS
Summary:	PHP API and tools for Amazon SQS
Summary(pl.UTF-8):	API PHP oraz narzędzia do obsługi Amazon SQS
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	Apache v2.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	56adf2ee5af123d1a0f9a3c6f74093a5
URL:		http://pear.php.net/package/Services_Amazon_SQS/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Console_Getopt
Requires:	php-pear-Crypt_HMAC2 >= 0.2.1
Requires:	php-pear-HTTP_Request2 >= 0.1.0
Requires:	php-pear-PEAR >= 1.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
%pear_package_install
install {./,$RPM_BUILD_ROOT}%{_bindir}/sqs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%attr(755,root,root) %{_bindir}/sqs
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/cfg/Services_Amazon_SQS/sqs.ini
%{php_pear_dir}/Services/Amazon/SQS
%{php_pear_dir}/Services/Amazon/SQS.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Services_Amazon_SQS
