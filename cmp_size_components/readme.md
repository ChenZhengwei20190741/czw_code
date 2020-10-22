# 比较size components 大小

## 1、保存esp32 的 size components

```sh

idf.py size-components > file1.txt

idf.py size-components > file2.txt

```

## 2、比较2个文件的szie components

```sh

python components.py file1.txt file2.txt

```
