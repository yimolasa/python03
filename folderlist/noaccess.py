import re                                               # 2020/03/09 22:50:20 ERROR 5 (0x00000005) Copying File \\nzwhkvmfs003\d$\System Volume Information\SRM\a\quota.xml
log = 'no.txt'
folderlist = 'foldrlist.txt'

folders = list()
with open(log, 'rb') as f:
    nplist = f.readlines()
for each in nplist:
    each = each.decode('UTF-8')                         # decode
    result = re.split(r'\\', each)                      # split by \ 
    
    newline = r'\\' + '\\'.join(result[2:-1]) + '\n'    # combine to a path
    
    if not newline in folders:                          # deduplicate
        folders.append(newline)

folders.sort()

for folder in folders[:-2]:
    nextfolder = folders[folders.index(folder)+1]
    # print(nextfolder)
    while nextfolder.find(folder): 
        folders.remove(nextfolder)
        nextfolder = folders[folders.index(folder)]
    print(folder)    
# print(folders)

# with open(folderlist, 'w') as f:
#     f.writelines(folders)


