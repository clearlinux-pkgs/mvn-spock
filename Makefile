PKG_NAME := mvn-spock
URL = https://github.com/spockframework/spock/archive/spock-1.0.tar.gz
ARCHIVES = https://repo1.maven.org/maven2/org/spockframework/spock-core/1.0-groovy-2.4/spock-core-1.0-groovy-2.4.jar : https://repo1.maven.org/maven2/org/spockframework/spock-core/1.0-groovy-2.4/spock-core-1.0-groovy-2.4.pom : https://repo1.maven.org/maven2/org/spockframework/spock-core/1.3-groovy-2.5/spock-core-1.3-groovy-2.5.jar : https://repo1.maven.org/maven2/org/spockframework/spock-core/1.3-groovy-2.5/spock-core-1.3-groovy-2.5.pom : 

include ../common/Makefile.common
