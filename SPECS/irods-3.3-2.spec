%global irodsServerPackageName server-gsi
%global irodsClientPackageName client-gsi
%global irodsServerPackageName server-gsi
%global irodsClientCommands iadmin ibun icd ichksum ichmod icp ienv ierror iexecmd iexit iget igetwild.sh ihelp iinit ils ilsresc imcoll imeta imiscsvrinfo imkdir imv ipasswd iphybun iphymv iput ipwd iqdel iqmod iqstat iquest iquota ireg irepl irm irmtrash irsync irule iscan isysmeta itrim iuserinfo
%global irodsServerCommands irodsAgent irodsReServer irodsServer
%global configFiles server.config.in rda.config HostAccessControl irodsHost
%global perlScripts utils_paths.pl utils_print.pl utils_file.pl utils_platform.pl utils_config.pl irodsctl.pl

Summary:	iRODS - Integrated Rule-Oriented Data System
Name:		irods
Group:		System Environment/Libraries
Version:	3.3
Release:	2%{?dist}
License:	BSD
Source:		irods%{version}.tgz
Source1:	irods
Patch0:		allow-root-configure.patch
Patch1:		irods_script.patch
Patch2:		make-install-target.patch
Patch3:		no-anonymous-exec-cmd.patch

URL:		http://www.irods.org
Packager:	Jerome Pansanel <jerome.pansanel@iphc.cnrs.fr>
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	perl, perl-Archive-Tar, libtool-ltdl-devel, globus-gss-assist-devel, globus-gssapi-gsi-devel, globus-common-devel, globus-gsi-proxy-ssl-devel, globus-gsi-sysconfig-devel, globus-openssl-module-devel, globus-gsi-cert-utils-devel, globus-gsi-callback-devel, globus-gsi-credential-devel, globus-gsi-openssl-error-devel, globus-gssapi-gsi-devel, globus-common-devel, globus-gsi-proxy-ssl-devel, globus-gsi-sysconfig-devel, globus-openssl-module-devel, globus-gsi-cert-utils-devel, globus-gsi-callback-devel, globus-gsi-credential-devel, globus-gsi-openssl-error-devel, globus-gsi-proxy-core-devel, globus-callout-devel, globus-gsi-proxy-core-devel, globus-callout-devel, netcdf-devel, pam-devel

%description
iRODS, the Integrated Rule-Oriented Data System, is a data grid
software system developed by the Data Intensive Cyber Environments
research group (developers of the SRB, the Storage Resource Broker),
and collaborators. The iRODS system is based on expertise gained
through a decade of applying the SRB technology in support of Data
Grids, Digital Libraries, Persistent Archives, and Real-time Data
Systems. iRODS management policies (sets of assertions these
communities make about their digital collections) are characterized in
iRODS Rules and state information. At the iRODS core, a Rule Engine
interprets the Rules to decide how the system is to respond to various
requests and conditions. iRODS is open source under a BSD license.

The %{name} package contains:
iRODS Common Libraries

%package %{irodsClientPackageName}
Summary:	iRODS - Client Programs (GSI-enabled)
Requires:	%{name} = %{version}-%{release}
Group:		Applications/Internet

%description %{irodsClientPackageName}
iRODS, the Integrated Rule-Oriented Data System, is a data grid
software system developed by the Data Intensive Cyber Environments
research group (developers of the SRB, the Storage Resource Broker),
and collaborators. The iRODS system is based on expertise gained
through a decade of applying the SRB technology in support of Data
Grids, Digital Libraries, Persistent Archives, and Real-time Data
Systems. iRODS management policies (sets of assertions these
communities make about their digital collections) are characterized in
iRODS Rules and state information. At the iRODS core, a Rule Engine
interprets the Rules to decide how the system is to respond to various
requests and conditions. iRODS is open source under a BSD license.

The %{irodsClientPackageName} provides the iRODS client command-line
utilities that are used to perform various functions between the iRODS
client and server.

%package %{irodsServerPackageName}
Summary:        iRODS - Server with GSI
Requires:       irods = %{version}-%{release}, unixODBC
Group:          System Environment/Daemons

%description %{irodsServerPackageName}
iRODS, the Integrated Rule-Oriented Data System, is a data grid
software system developed by the Data Intensive Cyber Environments
research group (developers of the SRB, the Storage Resource Broker),
and collaborators. The iRODS system is based on expertise gained
through a decade of applying the SRB technology in support of Data
Grids, Digital Libraries, Persistent Archives, and Real-time Data
Systems. iRODS management policies (sets of assertions these
communities make about their digital collections) are characterized in
iRODS Rules and state information. At the iRODS core, a Rule Engine
interprets the Rules to decide how the system is to respond to various
requests and conditions. iRODS is open source under a BSD license.

The %{irodsServerPackageName} package provides the iRODS server
binaries, and can be used to create both an iRODS catalog service
(ICAT), or to create an iRODS data resource server, or both.

%prep
%setup -n iRODS
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
       cp irodsctl irodsctl.orig
        scripts/configure
        sed -i \
          -e 's|#RODS_CAT=|RODS_CAT=1|' \
          -e 's|#PSQICAT=|PSQICAT=1|' \
          -e 's|#POSTGRES_HOME=|POSTGRES_HOME=/usr|' \
          -e 's|#NEW_ODBC=|NEW_ODBC=1|' \
          -e 's|# IRODS_FS = 1|IRODS_FS = 1|' \
          -e 's|^fuseHomeDir=.*|fuseHomeDir=/usr|' \
          -e 's|# GSI_AUTH = 1|GSI_AUTH = 1|' \
          -e 's|^GLOBUS_LOCATION=.*|GLOBUS_LOCATION=/usr|' \
          -e 's|^GSI_INSTALL_TYPE=.*|GSI_INSTALL_TYPE=|' \
          -e 's|^GSI_SSL=.*|GSI_SSL=ssl|' \
          -e 's|^GSI_CRYPTO=.*|GSI_CRYPTO=crypto|' \
          -e 's|# PAM_AUTH = 1|PAM_AUTH = 1|' \
          -e 's|# USE_SSL = 1|USE_SSL = 1|' \
          -e 's|# OS_AUTH = 1|OS_AUTH = 1|' \
          -e 's|#OS_AUTH_CMD =.*|OS_AUTH_CMD=%{_libdir}/irods/genOSAuth|' \
          -e 's|#DEF_CONFIG_DIR=.*|DEF_CONFIG_DIR=/etc/irods|' \
          -e 's|#DEF_STATE_DIR=.*|DEF_STATE_DIR=/var/lib/irods|' \
          -e 's|#DEF_LOG_DIR=.*|DEF_LOG_DIR=/var/log/irods|' \
          -e 's|#CMD_DIR=.*|CMD_DIR=%{_libdir}/irods/cmd|' \
          -e 's|#PAM_AUTH_CHECK_PROG=.*|PAM_AUTH_CHECK_PROG=%{_libdir}/irods/PamAuthCheck|' \
          -e 's|# STORAGE_ADMIN_ROLE = 1|STORAGE_ADMIN_ROLE = 1|' \
          -e 's|#UNI_CODE=|UNI_CODE=1|' \
          -e 's|# RUN_SERVER_AS_ROOT = 1|RUN_SERVER_AS_ROOT = 1|' \
          -e 's|# FILESYSTEM_META = 1|FILESYSTEM_META = 1|' \
          -e 's|# DIRECT_ACCESS_VAULT = 1|DIRECT_ACCESS_VAULT = 1|' \
          -e 's|# NETCDF4_API=1|NETCDF4_API=1|' \
          config/config.mk
          make
          make fuse

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} LIBDIR=%{_libdir} install
# Temporary fix to remove fuse support 
rm %{buildroot}/%{_bindir}/irodsFs

mkdir -p %{buildroot}/usr/share/doc/irods
cp -p %{_builddir}/iRODS/COPYRIGHT/Copyright.txt %{buildroot}/usr/share/doc/irods
cp -p %{_builddir}/iRODS/COPYRIGHT/Copyright_Addendum.txt %{buildroot}/usr/share/doc/irods
cp -p %{_builddir}/iRODS/LICENSE.txt %{buildroot}/usr/share/doc/irods
cp -p %{_builddir}/iRODS/README.txt %{buildroot}/usr/share/doc/irods
cp -p %{_builddir}/iRODS/config/irods.config.template %{buildroot}/usr/share/doc/irods

%clean
rm -rf %{buildroot}
rm -rf %{_tmppath}/%{name}.filelist
rm -rf %{_tmppath}/%{name}-client.filelist

%files
%defattr(-,root,root,-)
%doc /usr/share/doc/irods

%files %{irodsClientPackageName} 
%defattr(-,root,root,-)
%{_bindir}/iadmin
%{_bindir}/ibun
%{_bindir}/icd
%{_bindir}/ichksum
%{_bindir}/ichmod
%{_bindir}/icp
%{_bindir}/idbo
%{_bindir}/idbug
%{_bindir}/ienv
%{_bindir}/ierror
%{_bindir}/iexecmd
%{_bindir}/iexit
%{_bindir}/ifsck
%{_bindir}/iget
%{_bindir}/igetbyticket.pl
%{_bindir}/igetwild.sh
%{_bindir}/igroupadmin
%{_bindir}/ihelp
%{_bindir}/iinit
%{_bindir}/ilocate
%{_bindir}/ils
%{_bindir}/ilsresc
%{_bindir}/imcoll
%{_bindir}/imeta
%{_bindir}/imiscsvrinfo
%{_bindir}/imkdir
%{_bindir}/imv
%{_bindir}/ipasswd
%{_bindir}/iphybun
%{_bindir}/iphymv
%{_bindir}/ips
%{_bindir}/iput
%{_bindir}/ipwd
%{_bindir}/iqdel
%{_bindir}/iqmod
%{_bindir}/iqstat
%{_bindir}/iquest
%{_bindir}/iquota
%{_bindir}/ireg
%{_bindir}/irepl
%{_bindir}/irm
%{_bindir}/irmtrash
%{_bindir}/irsync
%{_bindir}/irule
%{_bindir}/iscan
%{_bindir}/isysmeta
%{_bindir}/iticket
%{_bindir}/itrim
%{_bindir}/iuserinfo
%{_bindir}/ixmsg
%{_libdir}/irods/genOSAuth
%{_libdir}/irods/rules
# NETCDF binaries
%{_bindir}/inc
%{_bindir}/incarch
%{_bindir}/incattr

%files %{irodsServerPackageName} 
%{_sbindir}/
%{_libdir}/irods/cmd
%{_libdir}/irods/schema
%{_libdir}/irods/PamAuthCheck
/etc/irods

%changelog
* Mon Jan 01 2014 Jerome Pansanel <jerome.pansanel@iphc.cnrs.fr> 3.3-2
- Install directory is now /usr
- Use globus packages provided by EPEL
* Thu Dec 12 2012 Jerome Pansanel <jerome.pansanel@iphc.cnrs.fr> 3.3-1
* Fri Apr 13 2012 Jerome Pansanel <jerome.pansanel@iphc.cnrs.fr> 3.0-2
- Add Server and Server packages
* Fri Jun 10 2011 Jerome Pansanel <jerome.pansanel@iphc.cnrs.fr> 3.0-1
- First RPM release

