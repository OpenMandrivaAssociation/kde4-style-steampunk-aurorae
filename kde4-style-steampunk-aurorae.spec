Summary:	"SteampunK Powered Linux" Aurorae theme
Name:		kde4-style-steampunk-aurorae
Version:	3.0
Release:	1
License:	Creative Commons Attribution-ShareAlike
Group:		Graphical desktop/KDE
Url:		http://kde-look.org/content/show.php?content=158790
Source0:	http://kde-look.org/CONTENT/content-files/158790-SteampunK.tar.gz
Requires:	kdebase4-workspace >= 2:4.10
BuildRequires:	kde4-macros
BuildArch:	noarch

%description
This package contains the "SteampunK Powered Linux" theme for Aurorae.

%files
%{_kde_appsdir}/aurorae/themes/SteampunK

#----------------------------------------------------------------------------

%prep
%setup -q -c
find . -type f | xargs chmod 0644

%build
# nothing

%install
mkdir -p %{buildroot}%{_kde_appsdir}/aurorae/themes

cp -r SteampunK %{buildroot}%{_kde_appsdir}/aurorae/themes/

