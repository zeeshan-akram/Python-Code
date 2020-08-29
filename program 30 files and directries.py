from pathlib import Path


path = Path("ecommerce")
print(path.exists())


path1 = Path("email")
print(path1.exists())


path3 = Path("number")
print(path3.rmdir())      #remove directory


path2 = Path("number")
print(path2.mkdir())      #make directory again



files = Path()
for file in files.glob("*.py"):     #for all files use only *
    print(file)                  #use can search only extensions too e.g *.py