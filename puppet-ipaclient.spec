%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-ipaclient
%global commit b086731d5f1c0129db3cd8e3ebdc1acd649ebfce
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-ipaclient
Version:        2.5.2
Release:        1%{?dist}
Summary:        IPA Client Puppet Module
License:        MIT

URL:            https://github.com/joshuabaird/puppet-ipaclient

Source0:        http://github.com/joshuabaird/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
IPA client puppet module for integration with IPA servers.

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/ipaclient/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/ipaclient/



%files
%{_datadir}/openstack-puppet/modules/ipaclient/


%changelog
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 2.5.2-1
- Update to 2.5.2



