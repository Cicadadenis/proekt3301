import os
import json
from time import sleep
from .logo import *
from .system import *

class main:
  def install_tools(self):
    while True:
      tool=tools()
      num=1
      total=len(tool.names)
      os.system("clear")
      logo.install_tools()
      print("\007")
      for tool_name in tool.names:
        print (f"{num} install {tool_name}")
        num+=1
      print("")
      logo.back()
      cmd=input("⏭⏭⏭")
      if cmd=="00" or cmd=="back":
        self.menu()
        break
      else:
        try:
          if int(cmd)>=1 and int(cmd)<=int(total):
            os.system("clear")
            logo.installing()
            print("installing ....")
            tool.install(tool.names[int(cmd)-1])
          else:
            print(f"Сожалею : '{cmd}' Неправильный ввод !!")
            sleep(1)
        except ValueError:
          print(f"Сожалею : '{cmd}' Неправильный ввод !!")
          sleep(1)

  def category(self):
    while True:
      tool=tools()
      total=len(tool.category)
      num=1
      os.system("clear")
      logo.tool_header()
      print("")
      for cat in tool.category:
        print (f"  [ {num} ] {tool.category_data[cat]}")
        num+=1
      print("")
      logo.back()
      cmd=input("⏭⏭⏭")
      if cmd=="00" or cmd=="back":
        self.menu()
        break
      else:
        try:
          if int(cmd) in range(1,int(total)+1):
            while True:
              print(int(cmd)-1)
              print(tool.category[int(cmd)-1])
              cnt=1
              os.system("clear")
              logo.tool_header()
              print("")
              tmp_cat_tool=[]
              for i in tool.names:
                if tool.category[int(cmd)-1] in tool.data[i]["category"]:
                  tmp_cat_tool.append(tool.data[i]['name'])
                  print(f" [ {cnt} ] install {tool.data[i]['name']}")
                  cnt+=1
              print("")
              logo.back()
              tcmd=input("	 ⏭⏭⏭ ")
              if tcmd=="0️⃣0️⃣" or tcmd=="back":
                break
              else:
                try:
                  cat_total=len(tmp_cat_tool)
                  if int(tcmd) in range(1,int(cat_total)+1):
                    os.system("clear")
                    logo.installing()
                    print("installing ....")
                    tool.install(tmp_cat_tool[int(tcmd)-1])
                  else:
                    print(f"Cожалею : '{tcmd}' Некорректный ввод !!")
                    sleep(1)
                except ValueError:
                  print(f"Cожалею : '{tcmd}' Некорректный ввод !!")
                  sleep(1)
          else:
            print(f"Cожалею : '{cmd}' Некорректный ввод !!")
            sleep(1)
        except ValueError:
          print(f"Cожалею : '{cmd}' Некорректный ввод !!")
          sleep(1)

  def update(self):
    while True:
      os.system("clear")
      logo.update()
      cmd=input("⏭⏭⏭")
      if cmd=="1":
        system=sys()
        if system.connection:
          os.system("clear")
          logo.updating()
          if system.sudo != None:
            if os.path.exists(system.home+"/Cicada"):
              pass
            else:
              os.system(system.sudo+" git clone https://github.com/bednakovdenis/Xack-menu.git "+system.home+"/Cicada")
            if os.path.exists(system.home+"/Cicada/install.aex"):
              os.system("cd "+system.home+"/Cicada && "+system.sudo+" sh install.aex")
              if os.path.exists(system.bin+"/Cicada") and os.path.exists(system.conf_dir+"/Cicada"):
                os.system("clear")
                logo.updated()
                cmd=input("⏭⏭⏭")
              else:
                os.system("clear")
                logo.update_error()
                cmd=input("⏭⏭⏭")
            else:
              os.system("clear")
              logo.update_error()
              cmd=input("⏭⏭⏭")
          else:
            if os.path.exists(system.home+"/Cicada"):
              pass
            else:
              os.system("git clone https://github.com/bednakovdenis/Xack-menu.git "+system.home+"/Cicada")
            if os.path.exists(system.home+"/Cicada/install.aex"):
              os.system("cd "+system.home+"/Cicada && sh install.aex")
              if os.path.exists(system.bin+"/Cicada") and os.path.exists(system.conf_dir+"/Cicada"):
                os.system("clear")
                logo.updated()
                cmd=input("⏭⏭⏭")
              else:
                os.system("clear")
                logo.update_error()
                cmd=input("⏭⏭⏭")
            else:
              os.system("clear")
              logo.update_error()
              cmd=input("⏭⏭⏭")
        else:
          os.system("clear")
          logo.nonet()
          tmp=input("⏭⏭⏭")
      elif cmd=="0" or cmd=="back":
        self.menu()
        break
      else:
        print(f"Cожалею : '{cmd}' Некорректный ввод !!")
        sleep(1)

  def about(self):
    while True:
      tool=tools()
      total=len(tool.names)
      os.system("clear")
      logo.about(total)
      cmd=input("⏭⏭⏭")
      self.menu()
      break

  @classmethod
  def menu(self):
    while True:
      tool=tools()
      system=sys()
      total=len(tool.names)
      os.system("clear")
      logo.menu(total)
      cmd=input("⏭⏭⏭")
      if cmd == "1":
        self.install_tools(self)
        break
      elif cmd == "2":
        self.category(self)
        break
      elif cmd == "3":
        self.update(self)
        break
      elif cmd == "4":
        self.about(self)
        break
      elif cmd=="x" or cmd=="X" or cmd=="exit":
        os.system("clear")
        logo.exit()
        break
      elif cmd=="rm -t" or cmd=="rm -T" or cmd=="uninstall Cicada" or cmd=="unistall Cicada":
        if system.sudo:
          os.system(system.sudo+" rm -rf "+system.bin+"/Cicada")
          os.system(system.sudo+" rm -rf "+system.bin+"/cicada")
          os.system(system.sudo+" rm -rf "+system.conf_dir+"/Cicada")
        else:
          os.system("rm -rf "+system.bin+"/Cicada")
          os.system("rm -rf "+system.bin+"/cicada")
          os.system("rm -rf "+system.conf_dir+"/Cicada")
        os.system("clear")
        logo.exit()
        break
      else:
        print(f"Cожалею : '{cmd}' Некорректный ввод !!")
        sleep(1)

class tools:
  data=None
  names=None
  category=None
  category_data=None
  def __init__(self):
    system=sys()
    with open(system.conf_dir+"/Cicada/core/data.json") as data_file:
      self.data=json.load(data_file)
    with open(system.conf_dir+"/Cicada/core/cat.json") as cat_file:
      self.category_data=json.load(cat_file)
    self.names=list(self.data.keys())
    self.category=list(self.category_data.keys())

  def install(self,name):
    package_name=self.data[name]["package_name"]
    package_manager=self.data[name]["package_manager"]
    url=self.data[name]["url"]
    req=list(self.data[name]["dependency"])
    system=sys()

    if system.connection:
      if len(req)!=0 and req[0]!=None:
        for dep in req:
          if os.path.exists(system.bin+"/"+dep):
            pass
          else:
            if system.sudo != None:
              os.system(system.sudo+" "+system.pac+" install "+dep+" -y")
            else:
              os.system(system.pac+" install "+dep+" -y")

      if package_manager=="package_manager":
        if os.path.exists(system.bin+"/"+package_name):
          os.system("clear")
          logo.already_installed(name)
          tmp=input("⏭⏭⏭")
        else:
          if system.sudo != None:
            os.system(system.sudo+" "+system.pac+" install "+package_name+" -y")
          else:
            os.system(system.pac+" install "+package_name+" -y")
          # check tool is installed or not
          if os.path.exists(system.bin+"/"+package_name):
            os.system("clear")
            logo.installed(name)
            tmp=input("⏭⏭⏭")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp=input("⏭⏭⏭")

      elif package_manager=="git":
        if os.path.exists(system.home+"/"+package_name):
          os.system("clear")
          logo.already_installed(name)
          tmp=input("⏭⏭⏭")
        else:
          if system.sudo != None:
            os.system(system.sudo+" git clone "+url+" "+system.home+"/"+package_name)
          else:
            os.system("git clone "+url+" "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            os.system("clear")
            logo.installed(name)
            tmp=input("⏭⏭⏭")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp=input("⏭⏭⏭")

      elif package_manager=="wget":
        if os.path.exists(system.home+"/"+package_name):
          os.system("clear")
          logo.already_installed(name)
          tmp=input("⏭⏭⏭")
        else:
          if system.sudo != None:
            os.system(system.sudo+" wget "+url+" -o "+system.home+"/"+package_name)
          else:
            os.system("wget "+url+" -o "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            os.system("clear")
            logo.installed(name)
            tmp=input("⏭⏭⏭")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp=input("⏭⏭⏭")

      elif package_manager=="curl":
        if os.path.exists(system.home+"/"+package_name):
          os.system("clear")
          logo.already_installed(name)
          tmp=input("⏭⏭⏭")
        else:
          if system.sudo != None:
            os.system(system.sudo+" curl "+url+" -o "+system.home+"/"+package_name)
          else:
            os.system("curl "+url+" -o "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            os.system("clear")
            logo.installed(name)
            tmp=input("⏭⏭⏭")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp=input("⏭⏭⏭")
    else:
      os.system("clear")
      logo.nonet()
      tmp=input("⏭⏭⏭")
