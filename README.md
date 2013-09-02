rpm-automake
============

An RPM spec file to build and install automake.

To Build:

`sudo yum -y install rpmdevtools autoconf && rpmdev-setuptree`

`wget https://raw.github.com/nmilford/rpm-automake/master/automake.spec -O ~/rpmbuild/SPECS/automake.spec`

`wget http://ftp.gnu.org/gnu/automake/automake-1.14.tar.gz -O  ~/rpmbuild/SOURCES/automake-1.14.tar.gz`

`rpmbuild -bb ~/rpmbuild/SPECS/automake.spec`