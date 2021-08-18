%define upstream_name    Net-INET6Glue
%define upstream_version 0.604

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Make L<IO::Socket::INET> behave like
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    https://cpan.metacpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::Socket::IP) >= 0.250.0
BuildRequires: perl(Net::FTP) >= 2.750.0
BuildRequires: perl-devel
BuildRequires: perl
BuildArch:  noarch

%description
the Net::INET6Glue manpage is a collection of modules to make common
modules IPv6 ready by hotpatching them.

Unfortunatly the current state of IPv6 support in perl is that no IPv6
support is in the core and that a lot of important modules (like the
Net::FTP manpage, the Net::SMTP manpage, the LWP manpage,...) do not
support IPv6 even if the modules for IPv6 sockets like the Socket6 manpage,
the IO::Socket::IP manpage or the IO::Socket::INET6 manpage are available.

This module tries to mitigate this by hotpatching. Currently the following
submodules are available:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
env PERL_MM_USE_DEFAULT=1 %{__perl} Makefile.PL INSTALLDIRS=vendor

%make_build

%check
%make_build test

%install
%make_install

%files
%doc COPYRIGHT Changes META.json META.yml MYMETA.yml README
%{_mandir}/man3/*
%perl_vendorlib/*
