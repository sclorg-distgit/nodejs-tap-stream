%{?scl:%scl_package nodejs-tap-stream}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-tap-stream

%global npm_name tap-stream
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-tap-stream
Version:	0.2.0
Release:	4%{?dist}
Summary:	Taps a nodejs stream and logs the data that's coming through.
Url:		http://registry.npmjs.org/tap-stream/-/tap-stream-0.2.0.tgz
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:    https://raw.githubusercontent.com/kasicka/tap-stream/090861dcbca70089b5272a7c3dab285f25c3f1bf/LICENSE
# https://github.com/thlorenz/tap-stream/pull/1
License:	BSD

BuildArch:	noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(tap)
%endif

%description
Taps a nodejs stream and logs the data that's coming through.

%prep
%setup -q -n package
cp -p %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%doc README.md LICENSE
%{nodejs_sitelib}/tap-stream

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.2.0-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.2.0-2
- Rebuilt with updated metapackage

* Fri Jan 08 2016 Tomas Hrcka <thrcka@redhat.com> - 0.2.0-1
- Initial build
