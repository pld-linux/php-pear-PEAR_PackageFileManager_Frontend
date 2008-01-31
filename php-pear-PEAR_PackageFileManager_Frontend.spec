%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	PackageFileManager_Frontend
%define		_status		alpha
%define		_pearname	PEAR_PackageFileManager_Frontend

Summary:	%{_pearname} - the singleton-based frontend for user input/output
Summary(pl.UTF-8):	%{_pearname} - oparty na singletonach frontend do obsługi wejścia/wyjścia
Name:		php-pear-%{_pearname}
Version:	0.7.0
Release:	3
License:	PHP License 3.01
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	61dabde9fd2506d70177afa581a92cde
URL:		http://pear.php.net/package/PEAR_PackageFileManager_Frontend/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Config >= 1.10.6
Requires:	php-pear-PEAR_PackageFileManager >= 1.6.0-0.b4.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Log.*)' 'pear(Var/Dump.*)'

%description
PEAR_PackageFileManager_Frontend is designed to act as a backend with
all features required by frontend such as Web or Gtk2.

Features:
- keep and manage all errors/warnings through a PEAR ErrorStack
- allow to import/export users preferences
- logs all frontend activities
- retrieve user package informations on import with common API
  getDefaults()
- provides also basic methods to get list of maintainers, files with
  roles and replacements, list of dependencies (packages, extensions),
  and specific files roles.
- provides a common Decorator pattern class for any frontend (Web,
  Gtk2, ...)
- works with PHP 4 and PHP 5.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
PEAR_PackageFileManager_Frontend został zaprojektowany aby działać
jako backend ze wszystkimi cechami wymaganym przez frontend taki jak
Web czy Gtk2.

Możliwości:
- zachowywanie i zarządzanie wszystkimi błędami/ostrzeżeniami poprzez
  PEAR-owy ErrorStack
- możliwość importu/eksportu ustawień użytkownika
- logowanie całej aktywności frontendu
- odczytywanie informacji o pakiecie użytkownika przy imporcie przy
  użyciu ogólnego API getDefaults()
- udostępnia także podstawowe metody do pobierania listy maintainerów,
  plików z rolami i zamiennikami, listy zależności (pakietów,
  rozszerzeń) i określonych ról plików
- udostępnia ogólną klasę wzorców Decorator dla dowolnego frontendu
  (Web, Gtk2...)
- działa z PHP 4 i PHP 5.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt docs/%{_pearname}/{examples,ChangeLog,NEWS}
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/PEAR/PackageFileManager/Frontend
%{php_pear_dir}/PEAR/PackageFileManager/Frontend/Decorator.php
%{php_pear_dir}/PEAR/PackageFileManager/Frontend.php
