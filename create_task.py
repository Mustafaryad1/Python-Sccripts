import os 
import sys
PATH = os.getcwd()

#  create HTml page 
def create_html(name):
  with open(f"index.html","w") as f:
    f.write(f"""<!DOCTYPE html>
<html lang="en">
  <head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>{name}</title>
  </head>
  <body>
  <!-- created by python script -->
  <script src="script.js"></script>
  </body>
</html>""")

#  create js file 
def create_js():
  with open("script.js",'w') as f:
    f.write("// created by python scripte ")
# create Task 
def create_task(name):
  if name in os.listdir(os.getcwd()):
    name = name + "-Copy"
  os.mkdir(name)
  os.chdir(PATH+f'\\{name}')
  create_html(name)
  create_js()


if __name__ == '__main__':
  folder_name = sys.argv[1]
  create_task(sys.argv[1])
  os.chdir(PATH)
  os.system(f'cmd /k "code \"{folder_name}\" "')