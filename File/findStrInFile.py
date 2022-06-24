import os

def eachFile(filepath):
  pathDir = os.listdir(filepath)    #遍历文件夹中的text
  return pathDir

def readfile(name):
  fopen=open(name,'r')
  # fopen=open(name,mode='r',encoding='utf-8')
  a =['120128342678']
  for lines in fopen.readlines():     #按行读取text中的内容
    lines = lines.replace("\n", "").split(",")
    for str1 in a:
      if str1 in str(lines):
      #筛选出含有''中内容的每一行
        print(lines)
        print(name)
  fopen.close()



filePath = r"C:\Users\linjie-033\Documents\日志\1"
 # 文件路径
pathDir=eachFile(filePath)
for allDir in pathDir:
  # child = os.path.join('%s%s' % (filepath, allDir))
  child = filePath + '\\' + allDir
  readfile(child)
