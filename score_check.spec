Name:           Score-check-oom
Version:        1
Release:        1
Summary:        oom_score process
Group:          Applications/File
License:        BSD
BuildRequires:  git


%description
scripts designed to asses the systems processes and their oom_score.

%prep
%setup -c -T
curl -fL https://api.github.com/repos/LukeShirnia/OOM-Killer-score/tarball/master |
tar -xzvf - --strip 1


%install
mkdir -p %{buildroot}/usr/bin/
%{__install} -D -m0755 score_check.sh ${RPM_BUILD_ROOT}/usr/bin/score_check

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/score_check

%changelog
* Thu Mar 26 2021 LukeShirnia <LukeShirnia@gmail.com>
- Initial release