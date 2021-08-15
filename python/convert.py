# given a dataset with particle positions
# convert from TXT file sequence to OBJ or RIB format 
import sys
import os.path

def txtToRib(x,y,z,camera,shader_string):
    """
    a particle in RIB example:
    AttributeBegin
        Bxdf "PxrSurface" "particles" "string __materialid" ["snowSG"]
        Translate 0.116228 0.115198 0.667355
        Sphere 0.004 -0.004 0.004 360
    AttributeEnd
    color=(0,200,255*rgb)
    """
    sphere_radius=0.008
    line_1='AttributeBegin\n'
    line_2='    Bxdf "PxrSurface" "particles" "string __materialid" ["%s"]\n'%shader_string
    line_3='    Translate %s %s %s\n'%(x-camera[0],y-camera[1],z-camera[2])
    line_4='    Sphere %f -%f %f 360\n'%(sphere_radius,sphere_radius,sphere_radius)
    line_5='AttributeEnd\n'
    return line_1+line_2+line_3+line_4+line_5

def txtToObj(x,y,z):
    return "v %f %f %f\n"%(x,y,z)

def write(input_file,output_file,camera):
    shader_string="defaultSG"
    f_in=open(input_file,'r')
    f_out=open(output_file,'w')
    last_char_index=output_file.rfind(".")
    extension=output_file[last_char_index+1:]
    lines=f_in.readlines()
    if extension=="rib":
        for i in range(len(lines)):
            line=lines[i].split()
            if(len(line) > 0):
                x=float(line[0])
                y=float(line[1])
                z=float(line[2])
                rib=txtToRib(x,y,z,camera,shader_string)
            f_out.write(rib)
    elif extension=="obj":
        for i in range(len(lines)):
            line=lines[i].split()
            if(len(line) > 0):
                x=float(line[0])
                y=float(line[1])
                z=float(line[2])
                obj=txtToObj(x,y,z)
            f_out.write(obj)
    f_out.close()

def input_format(filename):
    return print("Usage: %s <directory> <rib or obj> <start frame> <end frame>"%filename)

def main():
    camera=[1,1,1] #camera position

    if len(sys.argv)!=5:
        input_format(sys.argv[0])
        sys.exit()
    directory=sys.argv[1]
    output_type=sys.argv[2] #rib, obj
    if output_type!="rib" and output_type!="obj":
        input_format(sys.argv[0])
        print("invalid output format: rib or obj only")
        sys.exit()
    start=int(sys.argv[3])
    end=int(sys.argv[4])

    for i in range(start,end+1):
        print(i)
        file_format=str(i)+'.txt' #specific file format for input dataset
        input_file=os.path.join(directory,file_format)
        output_file=os.path.join(directory,'frame_%04d.%s')%(i,output_type)
        write(input_file,output_file,camera)

if __name__ == "__main__":
    main()