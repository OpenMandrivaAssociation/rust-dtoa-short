# Generated by rust2rpm
%bcond_with check
%global debug_package %{nil}

%global crate dtoa-short

Name:           rust-%{crate}
Version:        0.3.2
Release:        7%{?dist}
Summary:        Serialize float number and truncate to certain precision

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            https://crates.io/crates/dtoa-short
Source:         %{crates_source}
# Initial patched metadata
# * Bump float-cmp to 0.4, https://github.com/upsuper/dtoa-short/pull/6
Patch0:         dtoa-short-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(dtoa/default) >= 0.4.1 with crate(dtoa/default) < 0.5.0)
%if %{with check}
BuildRequires:  (crate(float-cmp/default) >= 0.4.0 with crate(float-cmp/default) < 0.5.0)
%endif

%global _description \
Serialize float number and truncate to certain precision.

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-5
- Adapt to new packaging

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-2
- Bump float-cmp to 0.4

* Thu Mar 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Tue Feb 27 2018 Josh Stone <jistone@redhat.com> - 0.3.1-3
- Bump float-cmp to 0.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-1
- Initial package
