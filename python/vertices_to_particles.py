"""
Input: OBJ file(s) with vertices only
Output: RIB file(s) to draw spheres while rendered with RenderMan
Usage: vertices_to_particles.py <directory> <start frame> <end frame>
"""
import sys

def txtToRib(x,y,z,camera):
    # Sample RIB sphere assigned with PxrSurface shader: "snowSG"
    """
    AttributeBegin
        Bxdf "PxrSurface" "particles" "string __materialid" ["snowSG"]
        Translate 0.116228 0.115198 0.667355
        Sphere 0.004 -0.004 0.004 360
    AttributeEnd
    """
    
    color=[1,1,1] # rgb values in [0,1]
    sphere_r=0.006
    line_1='AttributeBegin\n'
    line_2='    Bxdf "PxrSurface" "particles" "float diffuseGain" [1] "color diffuseColor" [%s %s %s]\n'%(color[0],color[1],color[2])
    line_3='    Translate %s %s %s\n'%(x-camera[0],y-camera[1],z-camera[2])
    line_4='    Sphere %f -%f %f 360\n'%(sphere_r,sphere_r,sphere_r)
    line_5='AttributeEnd\n'
    return line_1+line_2+line_3+line_4+line_5

def writeRib(f_in_name,f_out_name,camera):
    f_in=open(f_in_name,'r')
    f_out=open(f_out_name,"w")
    lines=f_in.readlines()
    for i in range(len(lines)):
        line=lines[i].split()
        if(len(line) > 0):
            x=float(line[0])
            y=float(line[1])
            z=float(line[2])
            rib=txtToRib(x,y,z,camera)
        f_out.write(rib)
    f_out.close()

def main():
    if(len(sys.argv)!=4):
        print("Usage: %s <directory> <start frame> <end frame>"%sys.argv[0])
        sys.exit()
    directory=sys.argv[1]
    start=int(sys.argv[2])
    end=int(sys.argv[3])
    for i in range(start,end+1):
        print(i)
        input_file=directory+'/t_'+str(i)+'.txt'
        rib_file=directory+'/frame_%04d.rib'%i

        # camera translation (x,y,z)
        camera_1=[1,2,3] 
        writeRib(input_file,rib_file,camera_1)

if __name__ == "__main__":
    main()