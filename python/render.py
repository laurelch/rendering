import sys,subprocess

frames=[] # render specific frames
resetOutputImage=False # modify output image file name or file path
version=1 # version of output image
take=1 # take of output image
readOtherRIB=False # read other RIB files, eg. particles RIB file

# check input: 
# dataset, the path to directory that holds RIB file sequence
# file prefix, the prefix of RIB files, e.g. particles.0001.rib has a file prefix of particles
# start frame, the frame to start render
# end frame, the frame to end render, inclusive
if len(sys.argv)!=5:
    print("Usage: %s <dataset> <file prefix> <start frame> <end frame>"%sys.argv[0])
    sys.exit()
dataset=sys.argv[1]
prefix=sys.argv[2]
start_frame=int(sys.argv[3])
end_frame=int(sys.argv[4])
print("dataset: %s"%dataset)
print("Frame: %s to %s"%(start_frame,end_frame))

for f in range(start_frame,end_frame+1):
    if len(frames)>0 and f not in frames:
        continue
    print(f)
    frame_4="%04d"%f
    rib_file="%s/%s.%s.rib"%(dataset,prefix,frame_4)

    if readOtherRIB or resetOutputImage:
        f_in=open(rib_file,'r')
        output_rib_file="frame_%s.rib"%frame_4
        f_out=open(output_rib_file,'w')
        for line in f_in.readlines():
            if resetOutputImage and line.find('Display ')>=0:
                    newline='Display "path/to/maya/workspace/images/project-name_v%03d_t%02d/%s.exr"\n'%(version,frame_4)
                    f_out.writelines(newline)
            if readOtherRIB and line.find('WorldEnd')>=0:
                    newline='        ReadArchive "%s/frame_%s.rib"\nWorldEnd\n'%(dataset,frame_4)
                    f_out.writelines(newline)
            else:
                f_out.writelines(line)
        f_in.close()
        f_out.close()
        command='prman -progress -t %s'%output_rib_file
        subprocess.Popen(command,shell=True,stdout=subprocess.PIPE).communicate()
        command='rm %s'%output_rib_file
        subprocess.Popen(command,shell=True,stdout=subprocess.PIPE).communicate()
    else:
        command='prman -progress -t %s'%rib_file
        subprocess.Popen(command,shell=True,stdout=subprocess.PIPE).communicate()