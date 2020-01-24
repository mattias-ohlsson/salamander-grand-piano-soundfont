Name:           salamander-grand-piano-soundfont
Version:        3.20161209
Release:        1%{?dist}
Summary:        Acoustic grand piano sample library in SFZ format

License:        CC-BY
URL:            https://freepats.zenvoid.org/Piano/acoustic-grand-piano.html
Source0:        https://freepats.zenvoid.org/Piano/SalamanderGrandPiano/SalamanderGrandPianoV3+20161209_48khz24bit.tar.xz

BuildArch:      noarch

%description
Acoustic grand piano sample library in SFZ format recorded with two AKG c414
disposed in an AB position 12cm above the strings.

%prep
%autosetup -n SalamanderGrandPianoV3_48khz24bit

%build
mv SalamanderGrandPianoV3.sfz SalamanderGrandPiano.sfz
mv SalamanderGrandPianoV3Retuned.sfz SalamanderGrandPianoRetuned.sfz

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/soundfonts/salamander-grand-piano
install -p -m 644 SalamanderGrandPiano.sfz $RPM_BUILD_ROOT%{_datadir}/soundfonts/salamander-grand-piano
install -p -m 644 SalamanderGrandPianoRetuned.sfz $RPM_BUILD_ROOT%{_datadir}/soundfonts/salamander-grand-piano
cp -a 48khz24bit $RPM_BUILD_ROOT%{_datadir}/soundfonts/salamander-grand-piano/

%files
%doc README
%{_datadir}/soundfonts/salamander-grand-piano

%changelog
* Fri Jan 24 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 3.20161209-1
- Initial build
