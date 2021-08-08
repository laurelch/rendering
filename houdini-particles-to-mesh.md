# Houdini Particles to Mesh

## Procedures to Convert Particles to Mesh
_Connect following nodes in sequence_
### Option 1
- **File** geometry node
  - reads **OBJ file** with particles coordinates as vertices
- **VDB from Particles** geometry node
- **VDB Smooth SDF** geometry node
- **Convert VDB** geometry node
  - converts VDB to OBJ file with vertices and faces
- **File** geometry node
  - writes file

### Option 2
- **File** geometry node
  - reads **OBJ file** with particles coordinates as vertices
- **Particle Fluid Surface** geometry node
- **File** geometry node
  - writes file

## Naming of Files in Houdini
When saving or reading files, use $F to represent frame numbers, and $F4 to represent frame numbers in 4 digits.

For example:
  
    frame_$F.obj
    
    => frame_0.obj, frame_10.obj, frame_100.obj
or

    frame_$F4.obj
    
    => frame_0000.obj, frame_0010.obj, frame_0100.obj

## Resources
- [Use SideFX Houdini to turn point clouds into optimized 3D models](https://docs.microsoft.com/en-us/dynamics365/mixed-reality/product-visualize/houdini-point-cloud) (Aug, 2020)
