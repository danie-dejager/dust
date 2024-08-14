%define name dust
%define version 1.1.1
%define release 1%{?dist}

Summary:  A more intuitive version of du in rust
Name:     %{name}
Version:  %{version}
Release:  %{release}
License:  MIT License
URL:      https://github.com/bootandy/dust
Source0:  https://github.com/bootandy/dust/archive/refs/tags/v%{version}.tar.gz

%define debug_package %{nil}

BuildRequires: curl
BuildRequires: gcc
BuildRequires: gzip

%description
du + rust = dust. Like du but more intuitive.

%prep
%setup -q

%build
# Install Rust using curl
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
export PATH="$PATH:$HOME/.cargo/bin"
cargo build --release
strip target/release/%{name}

%install
# Create the necessary directory structure in the buildroot
mkdir -p %{buildroot}/bin
mkdir -p %{buildroot}/usr/share/man/man1

# Copy the binary to /bin in the buildroot
install -m 755 target/release/%{name} %{buildroot}/bin/

# Copy the man page to /usr/share/man/man1 in the buildroot
gzip gen/%{name}.1
install -m 644 gen/%{name}.1.gz %{buildroot}/usr/share/man/man1/

%files
# List all the files to be included in the package
/bin/sd
/usr/share/man/man1/%{name}.1.gz

%changelog
* Wed Aug 14 2024 Danie de Jager - 1.1.1-1
- Built using rustc 1.80
