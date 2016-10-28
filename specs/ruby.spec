%define ruby_ver	2.3.1
%define ruby_abi	2.3

Name:		ruby
Version:	%{ruby_ver}
Release:	1%{?dist}
License:	Ruby License/GPL - see COPYING



Summary:	A dynamic, open source programming language with a focus on simplicity and productivity.

Group:		Development/Languages
URL:		https://www.ruby-lang.org/
Source0:	ftp://ftp.ruby-lang.org/pub/ruby/ruby-%{ruby_ver}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXX)

Requires:	readline ncurses gdbm glibc openssl libyaml libffi zlib
BuildRequires:	readline-devel ncurses-devel gdbm-devel glibc-devel gcc openssl-devel make libyaml-devel libffi-devel zlib-devel

Provides: ruby(abi) = %{ruby_abi}
Provides: ruby-irb
Provides: ruby-rdoc
Provides: ruby-libs
Provides: ruby-devel
Provides: rubygems

%description
A dynamic, open source programming language with a focus on simplicity and productivity. 
It has an elegant syntax that is natural to read and easy to write.


%prep
%setup -n ruby-%{ruby_ver}


%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

%configure \
  --enable-shared \
  --disable-rpath \
  --without-X11 \
  --without-tk \
  --includedir=%{_includedir}/ruby \
  --libdir=%{_libdir}

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/usr/src


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_includedir}/*
%{_datadir}/*
%{_libdir}/*
%doc



%changelog
* Fri Oct 28 2016 Eric Rumble <ericwrumble@gmail.com> - 2.3.1
- Update ruby version to 2.3.1

* Fri Oct 28 2016 Eric Rumble <ericwrumble@gmail.com> - 2.2.5
- Update ruby version to 2.2.5

* Fri Oct 28 2016 Eric Rumble <ericwrumble@gmail.com> - 2.1.10
- Set ruby version to 2.1.10
- Remove obsolete tags so older versions can still be installed
