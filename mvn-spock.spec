#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-spock
Version  : 1.0
Release  : 4
URL      : https://github.com/spockframework/spock/archive/spock-1.0.tar.gz
Source0  : https://github.com/spockframework/spock/archive/spock-1.0.tar.gz
Source1  : https://repo1.maven.org/maven2/org/spockframework/spock-core/1.0-groovy-2.4/spock-core-1.0-groovy-2.4.jar
Source2  : https://repo1.maven.org/maven2/org/spockframework/spock-core/1.0-groovy-2.4/spock-core-1.0-groovy-2.4.pom
Source3  : https://repo1.maven.org/maven2/org/spockframework/spock-core/1.3-groovy-2.5/spock-core-1.3-groovy-2.5.jar
Source4  : https://repo1.maven.org/maven2/org/spockframework/spock-core/1.3-groovy-2.5/spock-core-1.3-groovy-2.5.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-spock-data = %{version}-%{release}
Requires: mvn-spock-license = %{version}-%{release}
BuildRequires : buildreq-mvn
BuildRequires : gradle

%description
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/spockframework/spock/blob/master/LICENSE)
[![Maven Central](https://img.shields.io/maven-central/v/org.spockframework/spock-core.svg?label=Maven Central)](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22org.spockframework%22%20AND%20a%3A%22spock-core%22)
[![Linux Build Status](https://img.shields.io/travis/spockframework/spock/master.svg?label=Linux Build)](https://travis-ci.org/spockframework/spock)
[![Windows Build Status](https://img.shields.io/appveyor/ci/spockframework/spock/master.svg?label=Windows Build)](https://ci.appveyor.com/project/spockframework/spock/branch/master)

%package data
Summary: data components for the mvn-spock package.
Group: Data

%description data
data components for the mvn-spock package.


%package license
Summary: license components for the mvn-spock package.
Group: Default

%description license
license components for the mvn-spock package.


%prep
%setup -q -n spock-spock-1.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-spock
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-spock/LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spockframework/spock-core/1.0-groovy-2.4
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/spockframework/spock-core/1.0-groovy-2.4/spock-core-1.0-groovy-2.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spockframework/spock-core/1.0-groovy-2.4
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/spockframework/spock-core/1.0-groovy-2.4/spock-core-1.0-groovy-2.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spockframework/spock-core/1.3-groovy-2.5
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/spockframework/spock-core/1.3-groovy-2.5/spock-core-1.3-groovy-2.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spockframework/spock-core/1.3-groovy-2.5
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/spockframework/spock-core/1.3-groovy-2.5/spock-core-1.3-groovy-2.5.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/spockframework/spock-core/1.0-groovy-2.4/spock-core-1.0-groovy-2.4.jar
/usr/share/java/.m2/repository/org/spockframework/spock-core/1.0-groovy-2.4/spock-core-1.0-groovy-2.4.pom
/usr/share/java/.m2/repository/org/spockframework/spock-core/1.3-groovy-2.5/spock-core-1.3-groovy-2.5.jar
/usr/share/java/.m2/repository/org/spockframework/spock-core/1.3-groovy-2.5/spock-core-1.3-groovy-2.5.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-spock/LICENSE
