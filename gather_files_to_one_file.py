
import os
import time



git_claim_repository_path= "/git/APIntIO_Claim"
git_merge_file_path = "/git/APIntIO_Claim/Claims"
bool_use_git_fetch = True
if bool_use_git_fetch:
    
    print("-------------------")
    print (f"Process to fetch the repository: {git_claim_repository_path}")
    print("git remote -v")
    os.system("cd " + git_claim_repository_path + " && git remote -v")
    # check if something to fetch
    print("git pull")
    os.system("cd " + git_claim_repository_path + " && git pull")
    


print("-------------------")
print("Create the merge file")
if not os.path.exists(git_claim_repository_path):
    print("The path does not exist: ", git_claim_repository_path)
    # create the folder then the file in it
    os.makedirs(git_claim_repository_path)
    with open(git_merge_file_path, 'w') as f:
        f.write("")
else:
    # if the path exists, then create the file in it
    with open(git_merge_file_path, 'w') as f:
        f.write("")
    
time_start=  time.time()
print("Start to gather files from the repository: ", git_claim_repository_path)
# Get all the folders in the repository
folders = [f.path for f in os.scandir(git_claim_repository_path) if f.is_dir()]

for folder in folders:
    # Get all the files in the folder
    folder_name = folder.split("/")[-1]
    bool_is_integer = False
    integer_index = 0
    try:
        integer_index= int(folder_name)
        bool_is_integer = True
    except:
        pass 
    if bool_is_integer:
        # get all files in the folder
        files = [f.path for f in os.scandir(folder) if f
                    .is_file()]
        if len(files) > 0:
            file_name = files[0].split("/")[-1]
            print ("File name: ", file_name)
            # append file name in the merge file as {index}:{file_name}
            with open(git_merge_file_path, 'a') as f:
                f.write(str(integer_index) + ":" + file_name + "\n")

            

time_end = time.time()
time_to_merge= time_end - time_start
print("Time to merge files: ", time_to_merge)
print(f"Open the file: sudo nano {git_merge_file_path}")


