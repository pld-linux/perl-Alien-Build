#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Alien
%define		pnam	Build
Summary:	Alien::Build - build external dependencies for use in CPAN
Summary(pl.UTF-8):	Alien::Build - budowanie zewnętrznych zależności do wykorzystania w CPAN
Name:		perl-Alien-Build
Version:	2.83
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Alien/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fbec7ad3281181db0cd3e2219710815e
URL:		https://metacpan.org/dist/Alien-Build
BuildRequires:	perl-devel >= 1:5.8.4
BuildRequires:	perl-ExtUtils-CBuilder
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.64
BuildRequires:	perl-ExtUtils-ParseXS >= 3.30
BuildRequires:	perl-File-Which >= 1.10
BuildRequires:	perl-PkgConfig >= 0.14026
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Test2::API) >= 1.302096
BuildRequires:	perl(Text::ParseWords) >= 3.26
BuildRequires:	perl-Capture-Tiny >= 0.17
BuildRequires:	perl-Digest-SHA
BuildRequires:	perl-FFI-CheckLib >= 0.11
BuildRequires:	perl-File-Which >= 1.10
BuildRequires:	perl-File-chdir
BuildRequires:	perl-JSON-PP
BuildRequires:	perl-Path-Tiny >= 0.077
BuildRequires:	perl-Scalar-List-Utils >= 1.33
BuildRequires:	perl-Test2-Suite >= 0.000121
%endif
Requires:	perl(Text::ParseWords) >= 3.26
Requires:	perl-File-Which >= 1.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides tools for building external (non-CPAN)
dependencies for CPAN. It is mainly designed to be used at install
time of a CPAN client, and work closely with Alien::Base which is used
at runtime.

%description -l pl.UTF-8
Ten moduł dostarcza narzędzia do budowania zewnętrznych zależności
(spoza CPAN) dla CPAN. Powstał głównie do wykorzystania w czasie
instalacji klienta CPAN, do współpracy z Alien::Base, który jest
wykorzystywany w czasie działania.

%package -n perl-Alien-Base
Summary:	Alien::Base - Base classes for Alien:: modules
Summary(pl.UTF-8):	Alien::Base - klasy bazowe dla modułów Alien::
Group:		Development/Languages/Perl
Requires:	perl(Text::ParseWords) >= 3.26
Requires:	perl-Path-Tiny >= 0.077
Requires:	perl-Scalar-List-Utils >= 1.33

%description -n perl-Alien-Base
Alien::Base comprises base classes to help in the construction of
Alien:: modules. Modules in the Alien namespace are used to locate and
install (if necessary) external libraries needed by other Perl
modules.

%description -n perl-Alien-Base -l pl.UTF-8
Alien::Base obejmuje klasy bazowe pomagające w konstrukcji modułów
Alien::. Moduły w przestrzeni nazw Alien służą do lokalizacji i
instalowania (w razie potrzeby) zewnętrznych bibliotek wymaganych
przez inne moduły Perla.

%package -n perl-Test-Alien
Summary:	Test::Alien - testing tools for Alien modules
Summary(pl.UTF-8):	Test::Alien - narzędzia testowe dla modułów Alien
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	perl(Test2::API) >= 1.302096

%description -n perl-Test-Alien
This module provides tools for testing Alien modules. It has hooks to
work easily with Alien::Base based modules, but can also be used via
the synthetic interface to test non Alien::Base based Alien modules.
It has very modest prerequisites.

%description -n perl-Test-Alien -l pl.UTF-8
Ten moduł udostępnia narzędzia do testowania modułów Alien. Ma uchwyty
do łatwej pracy z modułami opartymi na Alien::Base, ale może być
używany także przeez sztuczny interfejs do testowania modułów Alien
nie opartych na Alien::Base. Ma bardzo skromne zależności.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Alien/Base/{Authoring,FAQ}.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Alien/Build/Manual.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Alien/Build/Manual/*.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Alien/Build/Plugin/*.pod

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes Changes.Alien-Build-Decode-Mojo SUPPORT
%{perl_vendorlib}/Alien/Build.pm
%dir %{perl_vendorlib}/Alien/Build
%{perl_vendorlib}/Alien/Build/CommandSequence.pm
%{perl_vendorlib}/Alien/Build/Interpolate.pm
%{perl_vendorlib}/Alien/Build/Interpolate
%{perl_vendorlib}/Alien/Build/Log.pm
%{perl_vendorlib}/Alien/Build/Log
%{perl_vendorlib}/Alien/Build/MM.pm
%{perl_vendorlib}/Alien/Build/Plugin.pm
%dir %{perl_vendorlib}/Alien/Build/Plugin
%{perl_vendorlib}/Alien/Build/Plugin/Build
%{perl_vendorlib}/Alien/Build/Plugin/Core
%{perl_vendorlib}/Alien/Build/Plugin/Decode
%{perl_vendorlib}/Alien/Build/Plugin/Digest
%{perl_vendorlib}/Alien/Build/Plugin/Download
%{perl_vendorlib}/Alien/Build/Plugin/Extract
%{perl_vendorlib}/Alien/Build/Plugin/Fetch
%{perl_vendorlib}/Alien/Build/Plugin/Gather
%{perl_vendorlib}/Alien/Build/Plugin/PkgConfig
%{perl_vendorlib}/Alien/Build/Plugin/Prefer
%{perl_vendorlib}/Alien/Build/Plugin/Probe
%{perl_vendorlib}/Alien/Build/Plugin/Test
%{perl_vendorlib}/Alien/Build/Temp.pm
%{perl_vendorlib}/Alien/Build/Util.pm
%{perl_vendorlib}/Alien/Build/Version
%{perl_vendorlib}/Alien/Build/rc.pm
%{perl_vendorlib}/alienfile.pm
%{_mandir}/man3/Alien::Build.3pm*
%{_mandir}/man3/Alien::Build::CommandSequence.3pm*
%{_mandir}/man3/Alien::Build::Interpolate*.3pm*
%{_mandir}/man3/Alien::Build::Log*.3pm*
%{_mandir}/man3/Alien::Build::MM.3pm*
%{_mandir}/man3/Alien::Build::Manual.3pm*
%{_mandir}/man3/Alien::Build::Manual::*.3pm*
%{_mandir}/man3/Alien::Build::Plugin.3pm*
%{_mandir}/man3/Alien::Build::Plugin::Build*.3pm*
%{_mandir}/man3/Alien::Build::Plugin::Core*.3pm*
%{_mandir}/man3/Alien::Build::Plugin::Decode*.3pm*
%{_mandir}/man3/Alien::Build::Plugin::Digest*.3pm*
%{_mandir}/man3/Alien::Build::Plugin::Download*.3pm*
%{_mandir}/man3/Alien::Build::Plugin::Extract*.3pm*
%{_mandir}/man3/Alien::Build::Plugin::Fetch*.3pm*
%{_mandir}/man3/Alien::Build::Plugin::Gather*.3pm*
%{_mandir}/man3/Alien::Build::Plugin::PkgConfig*.3pm*
%{_mandir}/man3/Alien::Build::Plugin::Prefer*.3pm*
%{_mandir}/man3/Alien::Build::Plugin::Probe*.3pm*
%{_mandir}/man3/Alien::Build::Plugin::Test*.3pm*
%{_mandir}/man3/Alien::Build::Temp.3pm*
%{_mandir}/man3/Alien::Build::Util.3pm*
%{_mandir}/man3/Alien::Build::Version::Basic.3pm*
%{_mandir}/man3/Alien::Build::rc.3pm*
%{_mandir}/man3/alienfile.3pm*
%{_examplesdir}/%{name}-%{version}

%files -n perl-Alien-Base
%defattr(644,root,root,755)
%doc Changes Changes.{Alien-Base,Alien-Base-Wrapper}
%{perl_vendorlib}/Alien/Base.pm
%dir %{perl_vendorlib}/Alien/Base
%{perl_vendorlib}/Alien/Base/PkgConfig.pm
%{perl_vendorlib}/Alien/Base/Wrapper.pm
%{perl_vendorlib}/Alien/Role.pm
%{perl_vendorlib}/Alien/Util.pm
%{_mandir}/man3/Alien::Base.3pm*
%{_mandir}/man3/Alien::Base::Authoring.3pm*
%{_mandir}/man3/Alien::Base::FAQ.3pm*
%{_mandir}/man3/Alien::Base::PkgConfig.3pm*
%{_mandir}/man3/Alien::Base::Wrapper.3pm*
%{_mandir}/man3/Alien::Role.3pm*
%{_mandir}/man3/Alien::Util.3pm*

%files -n perl-Test-Alien
%defattr(644,root,root,755)
%doc Changes.Test-Alien
%{perl_vendorlib}/Test
%{_mandir}/man3/Test::Alien*.3pm*
