# Installing RenderMan 24.1 and RenderMan for Maya  on Ubuntu 18.04

- Download
  - confirm system and product requirement (e.g Maya, Houdini, Blender) at RenderMan [Installing for Linux](https://rmanwiki.pixar.com/display/REN24/installing+on+Linux) page
  - Download RenderMan at [Try/Buy page](https://renderman.pixar.com/store)
- Install on Ubuntu
  - install RenderMan installer in ```~/Downloads```
    ```
    sudo alien -i RenderMan-InstallerNCR-24.1.0_2180719-linuxRHEL7_gcc63icc190.x86_64.rpm
    ```
  - Run installer
    ```
    sudo /opt/pixar/RenderMan-Installer-ncr-24.1/bin/RenderManInstaller
    ```
  - Note: If you encountered same following **error**, please follow the solution ([reference](https://www.youtube.com/watch?v=zCDQDlRN7eE))
    ```
    /opt/pixar/RenderMan-Installer-ncr-24.1/bin/RenderManInstaller: error while loading shared libraries: libicui18n.so.50: cannot open shared object file: No such file or directory
    ```
    - Visit [libicu-50.2-4.el7_7.x86_64.rpm](https://centos.pkgs.org/7/centos-x86_64/libicu-50.2-4.el7_7.x86_64.rpm.html) package page
    - Download the **Binary Package** with given URL
    - In ```~/Downloads/```, unpack the package with
      ```
      rpm2cpio libicu-50.2-4.el7_7.x86_64.rpm | cpio -idmv
      ```
    - Copy the files into RenderMan installer folder
      ```
      sudo cp ~/Downloads/usr/lib64/* /opt/pixar/RenderMan-Installer-ncr-24.1/lib/3rdparty/Qt-5.12.6/lib/
      ```
    - Run installer again
        ```
        sudo /opt/pixar/RenderMan-Installer-ncr-24.1/bin/RenderManInstaller
        ```
  - Follow GUI installation
    - Select **RenderMan Pro Server** and **RenderMan for xxx**
  - Install RenderMan for Maya
    ```
    sudo alien -i RenderManForMaya-24.1_2180719-linuxRHEL7_gcc63icc190.x86_64.rpm
    ```
- Load RenderMan in Maya
  - Create Renderman for Maya module file
    - Name the file according to the version: ```RenderMan_for_Maya_24.1.module```
    - In the module file, add this line
      ```
      + RenderMan_for_Maya 24.1 /opt/pixar/RenderManForMaya-24.1
      ```
    - Save the module file in the path: ```~/maya/modules/```
    - Check all module finding paths: open Maya, In Script Editor > Add a New MEL Script > Execute the following:
        ```
        getenv MAYA_MODULE_PATH
        ```
  - Load RenderMan in Maya
    - Open Maya with ```/usr/autodesk/maya2020/bin/maya```
    - Windows > Settings/Preferences > Plug-in Magaer, search for ```RenderMan_for_Maya.py``` in folder ```opt/pixar/RenderManForMaya-24.1/plug-ins```
    - Turn on **Loaded** (and Auto load)
    - Delete shelf of old versions of RenderMan if needed
## References

- [Installing for Linux](https://rmanwiki.pixar.com/display/REN24/installing+on+Linux), RenderMan 24 Docs, Pixar Animation Studios

- [Installing of RenderMan for Maya](https://rmanwiki.pixar.com/display/RFM24/Installation+of+RenderMan+for+Maya), RenderMan 24 Docs, Pixar Animation Studios

- [RenderMan 24 Installation Process on Linux for Houdini and Blender](https://www.youtube.com/watch?v=zCDQDlRN7eE), by Alexander Weide, YouTube