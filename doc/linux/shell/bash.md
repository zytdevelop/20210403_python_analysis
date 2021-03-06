# Bash

## 1. 学习Bash的目的

  -  执行速度快
  -  提高工作效率
  -  保持编码手感

  
## 2. Bash 的功能


### 2.1 记录
  ~/.bash_history会记录上一次登陆以前所执行过的命令，至于当前登陆的指令会被存储到内存中，等到你成功退出之后才会写入该文件。
  这样做的好处是便于查询曾经做过的举动。

### 2.2 命令补全功能[tab]
[tab]键的好处：
  - 1. 少打字
  - 2. 确定输入的内容是正确的


### 2.3 命令别名(alias)
- 给命令设定一个别名。
- 直接使用alias查看别名的记录

### 2.4 工作控制、前后台控制
待完善

### 2.5 程序化脚本(shell scripts)
主要目的是为了实现批量操作

### 2.6 通配符(wildcard)
支持模糊搜索



## 3. 命令

### 3.1 type
判断命令是否为BASH的内建命令:type

透过type这个命令我们可以知道每个命令是否为bash的内建命令。


### 3.2 echo
echo最大的作用就是显示变量，如果不确定一个变量是否存在，可以先echo一下。

  - 用法：
  ```bash
  echo $variable
  echo $PATH
  echo ${PATH}   # 作者推荐的格式

  ```


### 3.3 变量的规则
    - 1. 变量与变量之间以一个等号`=`连接:
    `myname=VBird`

    - 2. 等号两边不能直接连接空格，如下是错误示范：
    `myname = ZytDeveloper` 或`myname=Zyt Developer`

    - 3. 变量名称只能是英文字母和数字，但是开头字符不能是数字，如下是错误示范：
    `2myname=ZytDeveloper`

    - 4. 变量内容若有空格可以使用双引号`""`或者单引号`''`将变量内容结合起来。但存在两种特殊情况：
        - 双引号内的特殊字符如$，可以保留原本的特性：`var="lang is $LANG"`，则`echo $var`结果为`lang is zh_TW.UTF-8`
        - 单引号内的特殊字符就以纯文本存在：`var='lang is $LANG'`,则`echo $var`结果为`lang is $LANG`
    - 5. 用反斜杠转义符`\`将特殊字符变为普通字符存储：`myname=Zyt\ Developer`


    - 6. 需要引用额外的命令得到的结果时，可以用反单引号`指令`(tab键上方的波浪号键)或`$指令`。

    - 7. 变量之间可以相互嵌套，使用`$`或者`${}`：`version=$(uname -r)`再`echo $version`可以得到你的系统内核版本。

    - 8. 如果一个变量需要在其他子程序执行，则需要以`export`来使变量成为系统变量：`export PATH`

    - 9. 大写的字符通常是系统预设变量，自定义变量可以使用小写字符，方便判断（纯粹依照使用者兴趣与习惯）

    - 10. 取消变量：unset



### 3.4 env和export

```bash
    env : 查看预设的环境变量
```

```markdown
常用的env系统预设变量:
    - HOME : 家目录

    - SHELL : 存储当前环境所支持的shell

    - HISTSIZE : 历史命令数量限制

    - MAIL : 邮件相关环境变量

    - PATH : 执行文件搜索的路径

    - LANG : 系统语言

    - RANDOM : 随机变量  
```

```text
export : 自定义变量转为系统变量
PS:每个主机上的export内容都不一致。
```


 
### 3.5 set
```text
  查看所有的变量(包含系统变量和自定义变量)
```


### 3.6 locale
```text
  locale : 查看当前linux环境支持哪些编码格式
```

### 3.7 read, array, declare
```markdown
    read : 读取来自键盘的变量，多用于和user进行交互

    用法：read [-pt] var
    -p ：设置提示字符串
    -t ：设置等待时间
```

```text
    array : 数组
    待完善....
```
```markdown
    declare/typeset : 声明变量类型
    用法 : declare [-aixr] var
    -a : 声明变量类型为数组
    -i : 声明变量类型为整型
    -x : 声明变量类型为环境变量，与export作用一样
    -r : 声明变量为read-only
    不加参数 : 变量类型为字符串
```



### 3.8 ulimit




