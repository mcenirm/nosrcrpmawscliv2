Summary: AWS CLI version 2
License: Apache License 2.0
# Group: ???
Name: awscliv2
URL: https://docs.aws.amazon.com/cli/
Version: 2.0.41
Release: 2%{?dist}
Source0: https://awscli.amazonaws.com/awscli-exe-linux-%{_arch}.zip
NoSource: 0

# skip debuginfo
%define debug_package %{nil}

%description
The AWS Command Line Interface (AWS CLI) is an open
source tool that enables you to interact with AWS
services using commands in your command-line shell.

%prep
%setup -q -n aws

%build

%install
sh -x ./install --install-dir "$RPM_BUILD_ROOT"/usr/libexec/awscliv2 --bin-dir "$RPM_BUILD_ROOT"/usr/bin
# redo symlinks to avoid complaint about them containing $RPM_BUILD_ROOT
ln -sf ../libexec/awscliv2/v2/current/bin/aws "$RPM_BUILD_ROOT"/usr/bin/aws
ln -sf ../libexec/awscliv2/v2/current/bin/aws_completer "$RPM_BUILD_ROOT"/usr/bin/aws_completer
rm -f "$RPM_BUILD_ROOT"/usr/libexec/awscliv2/v2/current
ln -sf 2.0.41 "$RPM_BUILD_ROOT"/usr/libexec/awscliv2/v2/current

%check
"$RPM_BUILD_ROOT"/usr/bin/aws --version

%files
/usr/bin/aws
/usr/bin/aws_completer
/usr/libexec/awscliv2
