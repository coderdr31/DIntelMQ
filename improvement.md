<head><meta charset="UTF-8"></head>
1.待定： 每次运行前，自动删掉/opt/intelmq/var/run下，所有的***.pid文件


##
1. 本体、关联关系
2. 开发文档中goals：Provide an easy way to create your own black-lists
3. 使用ZMQ正在开发中，可以考虑使用。

## 开发过程需要解决的
1. 命名，文件夹、文件、Bot等等
2. intelmq-manager实现原理，新添parserbot代码，web中无法启动
3. log 怎么写
4. expert bot 是怎么实现的
5. collect parserbot 不同文件类型怎么实现的，实现半自动化, csv第一行key处理(替换)
6. google python相关expert的库、模块、工具
7. parser error、logger没写

### 0405组会小结
1. other-ParserBot 配置的容错性以后再考虑。
2. 不往harmonization.conf增加field

TODO：
1. other-ParserBot 增加可选字段(new field)，raw不要删除内容
2. ExpertBot——IPMarker
3. web界面

Q:
1. 开源的intelmq更新怎么办？ 是否要保证intelmq更新后能直接使用？
