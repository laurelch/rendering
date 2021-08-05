# Houdini Particles to Mesh
_Connect following nodes in sequence_
## Option 1
- **File** geometry node
  - reads **OBJ file** with particles coordinates as vertices
- **VDB from Particles** geometry node
- **VDB Smooth SDF** geometry node
- **Convert VDB** geometry node
  - converts VDB to OBJ file with vertices and faces
- **File** geometry node
  - writes file

## Option 2
- **File** geometry node
  - reads **OBJ file** with vertices
- **Particle Fluid Surface** geometry node
- **File** geometry node
  - writes file