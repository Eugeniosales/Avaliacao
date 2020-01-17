import os
import shutil
import tarfile

def create_file(file_name):
    #Create file SQL
    my_file = open(file_name, "w+")
    my_file.close()

def compact_folder(dir_name, file_name):
    try:
        os.makedirs(dir_name)
        print("Tar.gz", dir_name, " Created")
    except FileExistsError:
        print("Tar.gz", dir_name, "Already exists")  

    #Move Sql file to the desired directory
    shutil.move(file_name, dir_name)

    #Compact file to tar.gz
    tar = tarfile.open("opt.tar.gz", "w")
    tar.add(dir_name)
    tar.close()
    shutil.rmtree("opt")

def main():
    create_file("dump.sql")
    compact_folder("opt/bancobackup", "dump.sql")

if __name__ == '__main__':
    main()