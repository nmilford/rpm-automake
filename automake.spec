# To Build:
#
# sudo yum -y install rpmdevtools autoconf && rpmdev-setuptree
# wget https://raw.github.com/nmilford/rpm-automake/master/automake.spec -O ~/rpmbuild/SPECS/automake.spec
# wget http://ftp.gnu.org/gnu/automake/automake-1.14.tar.gz -O  ~/rpmbuild/SOURCES/automake-1.14.tar.gz
# rpmbuild -bb ~/rpmbuild/SPECS/automake.spec

Name:       automake
Version:    1.14
Release:    1
Summary:    Automatically generate Makefiles
Group:      Development/Tools
License:    GNU GPL
URL:        http://www.gnu.org/software/automake/
Source0:    http://ftp.gnu.org/gnu/automake/automake-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch
BuildRequires:  autoconf
Requires:   autoconf
Requires(post):  /sbin/install-info
Requires(preun): /sbin/install-info

%description
Automake is a tool for automatically generating Makefiles compliant with the 
GNU Coding Standards.

%prep
%setup -q

%build
%configure --prefix=/usr --docdir=/usr/share/doc/automake-1.11
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_infodir}/dir

%clean
rm -rf %{buildroot}

%post
/sbin/install-info %{_infodir}/automake.info.gz %{_infodir}/dir || :

%preun
if [ $1 = 0 ]; then
/sbin/install-info --delete %{_infodir}/automake.info.gz %{_infodir}/dir || :
fi 

%files
%defattr(-,root,root,-)
%doc AUTHORS README THANKS NEWS
%{_bindir}/*
%{_infodir}/*.info*
%{_datadir}/automake-%{version}
%{_datadir}/aclocal-%{version}
%{_datadir}/aclocal/README
%{_mandir}/man1/*
%{_docdir}/*/*

%changelog
* Mon Sep 02 2013 Nathan Milford <nathan@milford.io> 1.14-1
- First shot.