from pathlib import Path
import numpy as np
import os
abspath2file = os.path.abspath(__file__)
print("abspath2file : ", abspath2file)
abspath2file_path = Path(abspath2file)
print('abspath2file_path : ',abspath2file_path)
print("abspath2file_path.name : ", abspath2file_path.name)
print("abspath2file_path.suffix : ", abspath2file_path.suffix)
print('abspath2file_path.parent : ',abspath2file_path.parent)

abspath2dir = os.path.dirname(os.path.abspath(__file__))
print("abspath2dir : ", abspath2dir)

#現在実行しているファイルのディレクトリに移動する。
os.chdir(os.path.dirname(os.path.abspath(__file__)))

dirpath = os.getcwd()
print("dirpath : ",dirpath )

filename = Path("source_data/text_files/raw_data.txt")

print(filename.name)
# prints "raw_data.txt"

print(filename.suffix)
# prints "txt"

print(filename.stem)
# prints "raw_data"

if not filename.exists():
    print("Oops, file doesn't exist!")
else:
    print("Yay, the file exists!")

pathfile=os.path.dirname(dirpath)
basename=os.path.basename(dirpath)
print("pathfile : ", pathfile)
print("basename : ", basename)
print(os.path.join(pathfile,"output","log.txt"))
print(abspath2file_path.parent / 'newDirectory')
Path(abspath2file_path.parent / 'newDirectory').mkdir(parents=True, exist_ok=True)

print('-----------------------------------------------------------------------------')

#**の場合、**はディレクトリにのみマッチする。ファイルにもマッチさせたい場合は**/*とする。
p = Path(abspath2file_path.parent).glob('**/*.py')

array_test = np.array([])
for var_file_name in p:
    print(var_file_name)
    new_array_test = np.append(array_test,var_file_name,1)
print(new_array_test)

print('-----------------------------------------------------------------------------')
#**の場合、**はディレクトリにのみマッチする。ファイルにもマッチさせたい場合は**/*とする。
p = Path(abspath2file_path.parent).glob('**/*.py')
arr_files = [x for x in p if x.is_file()]
print(arr_files)
print(*arr_files, sep ="\n")

# ListからArrayに変換
myarray = np.asarray(arr_files)

print(myarray)


