#!/usr/bin/env python
import argparse
import sys

# torchlight
import torchlight
from torchlight import import_class

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Processor collection')  #添加一个解析器对象

    # region register processor yapf: disable
    processors = dict()
    processors['recognition'] = import_class('processor.recognition.REC_Processor')
    processors['demo'] = import_class('processor.demo.Demo')
    #endregion yapf: enable

    # add sub-parser
    subparsers = parser.add_subparsers(dest='processor')  #启动命名空间为processor的添加子命令，dest=‘’将存储子命令名称的属性的名称为processor
    for k, p in processors.items():  #将字典中的每一对变成元组的形式（[name,zhang],[age,20]）
        subparsers.add_parser(k, parents=[p.get_parser()]) #添加子命令K,  这个子命令K继承了p.get_paeser()中定义的所有的命令参数

    # read arguments
    arg = parser.parse_args() #开始读取命令行的数值并保存

    # start
    Processor = processors[arg.processor]  #读取arg的processor属性,取出processors字典中的key代表的元素
    p = Processor(sys.argv[2:])   #sys.argv[0]指.py程序本身,argv[2:]指从命令行获取的第二个参数

    p.start()
