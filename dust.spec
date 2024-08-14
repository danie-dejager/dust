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
mkdir -p %{buildroot}/etc/bash_completion.d/

# Copy the binary to /bin in the buildroot
install -m 755 target/release/%{name} %{buildroot}/bin/

# Copy Bash completion
install -m 755 completions/%{name}.bash %{buildroot}/etc/bash_completion.d/

%files
# List all the files to be included in the package
/bin/%{name}
/etc/bash_completion.d/%{name}.bash

%changelog
* Wed Aug 14 2024 Danie de Jager - 1.1.1-1
- Built using rustc 1.80.1
