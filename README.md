# Summary

这是一个简单的脚本，用来将typora中的图片上传到华为云的对象存储中。

# Usage

你可以单独的使用这个脚本，或是将其配置到Typora的自定义命令中。

本程序需要使用到python的requests库，请自行安装。

## 配置内容

本程序需要使用部分配置：

* AccessKeyId：你的私钥ID，你可以在华为云，"我的凭证/访问密钥"中创建或查询
* AccessKeySecret: 你的私钥，同AccessKeyId获取
* BucketName：需要上传的桶名称
* UploadPath：上传路径
* Endpoint：接入点，可以在控制台查询

例如：

```
AccessKeyId = "4dwOWKTDANIOpaILBXVP"
AccessKeySecret = "r3x3NOxo76dbtLAhx8746adL4Z0kPOI0iJayEEg"
BucketName = "mybucket" 
UploadPath = "/image"
Endpoint = "obs.cn-east-3.myhuaweicloud.com"
```

## 单独使用

```
python uploader.py file1 file2 file3
```

上传文件的路径需要时绝对路径，或者文件和脚本在同一个目录下。

## Typora配置

在偏好设置中，选择图像。

上传服务选择自定义命令：

```
"python" "脚本路径"
```

如果你需要使用特定的python解释器，请自行修改。

例如：

```
"python" "E:\TyporaImageUploader4Hwyun\uploader.py"
```

设置完成后点击验证图片上传选项即可验证。随后在上方的"插入图片时"选择上传图片，即可将插入在typora的图片上传至OBS。

