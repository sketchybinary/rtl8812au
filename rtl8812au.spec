Name:           rtl8812au
Version:        v5.3.4
Release:        1%{?dist}
Summary:        Modified rtl8812au driver that enables features like monitor mode, 802.11w, and net_ns

License:        GPLv2
URL:            https://github.com/sketchybinary/rtl8812au
Source0:        https://github.com/sketchybinary/rtl8812au

BuildRequires:  
Requires:       

%description


%prep
%autosetup


%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Tue May 28 2019 will.kline <will.kline@wkline.darkwolf.io>
- 
