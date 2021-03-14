import os
import time

def increase ():
        size = int(input("\tEnter Size to Increase : "))
        os.system(f"lvextend --size +{size}M /dev/myvg1/mylv1")
        os.system(f"resize2fs /dev/myvg1/mylv1")
        os.system("jps")
        print(f"Size Increased Successfully by {size}MB")

def decrease ():
        present = int(input("\tEnter Present Size (Before Reduce) of Disk : "))
        want = int(input("\tEnter Size After Reducing the Disk : "))
        os.system("hadoop-daemon.sh stop datanode")
        os.system("umount /task7")
        os.system("e2fsck -f /dev/myvg1/mylv1")
        os.system(f"resize2fs /dev/myvg1/mylv1 {want}")
        os.system(f"lvreduce --size -{present - want} /dev/myvg1/mylv1 -f")
        os.system("mount /dev/myvg1/mylv1 /task7")
        os.system("hadoop-daemon.sh start datanode")
        os.system("jps")
        print(f"Size Decreased Successfully by {present - want}")


def config ():
        disk = input("\tEnter Disk Name : ")
        os.system("hadoop-daemon.sh stop datanode")
        os.system(f"pvcreate /dev/{disk}")
        time.sleep(3)
        os.system(f"vgcreate hadoop /dev/{disk}")
        size = input("\tEnter Size of the Namenode : ")
        os.system(f"lvcreate --size {size}G --name hadoop-dn hadoop ")
        os.system("umount /task7")
        os.system("rm -rf /data7")
        os.system("mkdir /data7")
        os.system(f"mkfs.ext4 /dev/hadoop/hadoop-dn")
        os.system(f"mount /dev/hadoop/hadoop-dn  /task7")
        os.system("hadoop-daemon.sh start datanode")
        os.system("jps")
        print("Datanode Successfully Configured")

while (True):

        print('\t1. Configure the  Datanode')
        print('\t2. Increase the Size of Datanode')
        print('\t3. Decrease the Size of Datanode')
        print('\t4. Exit')
        ch = input('\tEnter Your choice : ')

        if ch == '1':
		config()
	elif ch == '2':
		increase()
	elif ch == '3':
		decrease()      
	elif ch == '4':
		exit()
	else:
		print('Invalid Choice. Try Again !!!')
