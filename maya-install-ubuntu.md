

# Installing Maya 2020 on Ubuntu


Comments: There are several (official) references talking about how to install Maya on Ubuntu, this is the one I use to follow in general

Reference link: [Installing Maya 2020 on Ubuntu](https://knowledge.autodesk.com/support/maya/learn-explore/caas/simplecontent/content/installing-maya-2020-ubuntu.html)

## Issue:

You need to install Maya 2020 on Ubuntu Linux, but the standard installation procedures for Linux do not work.

## Solution:

The installation of Maya 2020 on Ubuntu is non-standard. You need to install additional packages, convert the Maya rpm to a Debian package, and install Maya from the generated Debian package.

	
- Get the packages required for converting the rpm package. 	
```
sudo apt-get install alien dpkg-dev debhelper build-essential zlib1g-dev
```

- Get and install libXp6. 	
```
sudo add-apt-repository ppa:zeehio/libxp
sudo apt-get update
sudo apt-get install libxp6
```

- Extract the contents of the Maya installation package and change directory to its install/Packages directory.
```
Convert the rpm packages in the installation to deb packages. 	
sudo alien -vc *.rpm
```
	
- Install packages for standalone licensing. 	
```
sudo apt install lsb-core
```

- Install the licensing packages: adlmapps, adlmflexnetserveripv6, adlmflexnetclient, and adsklicensing. For example: 	
```
sudo apt-get install ./adlmapps17_17.0.49-1_amd64.deb
sudo apt-get install ./adlmflexnetserveripv6_17.0.50-1_amd64.deb
sudo apt-get install ./adlmflexnetclient-17.0.49-1_amd64.deb
sudo apt-get install ./adsklicensing9.2.1.2399_0-1_amd64.deb
```

- Verify that the licensing service is running. 	
```
sudo systemctl status adsklicensing
```

- If the licensing service is not running:
  - Start it using this command: 
  - 
        /opt/Autodesk/AdskLicensingService --run
  - Verify again that the service is running.
		
- If it is still not running, set up the licensing service manually:
```
sudo getent group adsklic &>/dev/null || sudo groupadd adsklic
sudo id -u adsklic &>/dev/null || sudo useradd -M -r -g adsklic adsklic -d / -s /usr/sbin/nologin  
sudo ln -sf /opt/Autodesk/AdskLicensing/9.2.1.2399/AdskLicensingService/AdskLicensingService /usr/bin/AdskLicensingService
sudo mkdir /usr/lib/systemd/system
sudo cp -f /opt/Autodesk/AdskLicensing/9.2.1.2399/AdskLicensingService/adsklicensing.el7.service /usr/lib/systemd/system/adsklicensing.service
sudo chmod 644 /usr/lib/systemd/system/adsklicensing.service
sudo systemctl daemon-reload
sudo systemctl enable adsklicensing –quiet
sudo systemctl start adsklicensing
```		

- Install Maya. 	
```
sudo apt-get install <Maya2020 deb package>
```

- Verify that Maya has been registered. Maya should appear in the list of products returned by: 	
```
/opt/Autodesk/AdskLicensing/<version_number>/helper/AdskLicensingInstHelper list
```
- If it does not, manually register it using 	
```
sudo /opt/Autodesk/AdskLicensing/<version_number>/helper/AdskLicensingInstHelper register -pk 657L1 -pv 2020.0.0.F -el EN_US -cf /var/opt/Autodesk/Adlm/Maya2020/MayaConfig.pit
```
- Then verify that it is in the list.
	
- Install additional required packages for running Maya. 	
```
sudo apt-get install libfam0 libcurl4 libpcre16-3 libjpeg62 libxm4 xfonts-100dpi xfonts-75dpi
sudo ln -s /usr/lib/x86_64-linux-gnu/libpcre16.so.3 /usr/autodesk/maya2020/lib/libpcre16.so.0
sudo ln -s /usr/lib/x86_64-linux-gnu/libssl.so.1.1 /usr/autodesk/maya2020/lib/libssl.so.10
sudo ln -s /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1 /usr/autodesk/maya2020/lib/libcrypto.so.10
sudo ln -s /usr/lib/x86_64-linux-gnu/libXp.so.6 /usr/autodesk/maya2020/lib/libXp.so.6
xset +fp /usr/share/fonts/X11/100dpi
xset +fp /usr/share/fonts/X11/75dpi
xset fp rehash
```

- You need libpng15.so.15 to run Maya. Because libpng15.so.15 is no longer available as a package, you need to download its source code from Sourceforge and build it locally. 	
```
cd ~/tmp
wget https://sourceforge.net/projects/libpng/files/libpng15/older-releases/1.5.15/libpng-1.5.15.tar.gz
tar -zxvf ./libpng-1.5.15.tar.gz
cd libpng-1.5.15
./configure --prefix=/usr/local/libpng
make check
sudo make install
make check
sudo ln -s /usr/local/libpng/lib/libpng15.so.15 /usr/autodesk/maya2020/lib/libpng15.so.15
```

- Create the /usr/tmp directory. 	
```
sudo mkdir /usr/tmpa
sudo chmod 777 /usr/tmp
```
	
- Set environment variables in the Maya.env file.
	
    - The Maya.env file is located in ~/maya/2020/Maya.env, You can create the file if it does not exist.
	
	- You will need to set MAYA_DISABLE_CIP and LC_ALL.
	
	- MAYA_DISABLE_CIP disables ADP, which can cause a hang on close, while LC_ALL ensures that Maya works with Ubuntu color correction. 
    -	
        ```
        echo "MAYA_DISABLE_CIP=1" >> ~/maya/2020/Maya.env
        echo "LC_ALL=C" >> ~/maya/2020/Maya.env
        ```
        
	
- Start Maya. 	
```
/usr/autodesk/maya2020/bin/maya
```
