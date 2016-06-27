#!/bin/sh -eux

# download the ruby source code
ruby_semver=`grep "%define \+ruby_ver" $HOME/rpmbuild/SPECS/ruby.spec | awk '{print $3}'`
cd $HOME/rpmbuild/SOURCES && curl -O ftp://ftp.ruby-lang.org/pub/ruby/ruby-$ruby_semver.tar.gz

# build the ruby rpms
rpmbuild -ba $HOME/rpmbuild/SPECS/ruby.spec

# copy the rpms back to the shared mount
cp $HOME/rpmbuild/RPMS/x86_64/* /shared
cp $HOME/rpmbuild/SRPMS/* /shared
