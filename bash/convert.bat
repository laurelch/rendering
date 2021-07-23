:: (Windows) convert all EXR files to PNG with Image Magick
FOR /R %%a IN (*.exr) DO "C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe" convert "%%~a" "%%~dpna.png"
