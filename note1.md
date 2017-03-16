<head><meta charset="UTF-8"></head>
## Installation
1. Some bots have additional dependencies which are mentioned in their documentation and their own REQUIREMENTS file (in their source directory).
## configuration
1. malware domain list ->   the file output bot writes all data to /opt/intelmq/var/lib/bots/file-output/events.txt.
2. The configuration directory is /opt/intelmq/etc/
   defaults.conf: default values for bots and their behavior, e.g. error handling, log options and pipeline configuration.
   runtime.conf:各种bots的配置，运行时的配置
   pipeline.conf: Defines source and destination queues per bot.
   BOTS:bots配置的提示，runtime.conf的模板
   harmonization.conf: 指定所有消息类型的字段。harmonization library将加载此配置，以便在消息处理期间检查值是否符合协调。通常，此配置不需要任何更改。
  如果要配置新bot，则要用BOTS的模板配置runtime.conf.配置pipeline.conf的源、目的queue。如果不确定，则用IntelMQ Manager生成配置。
3. log: /opt/intelmq/var/log/
4. 当前运行的配置文件在: /opt/intelmq/etc
5. 运用了ElasticSearch (应该是)

6. 不要执行6.1，执行 chmod -R 777 /opt/intelmq  即可。
  6.1  chown -R intelmq.intelmq /opt/intelmq to dr.dr 用户  ;intelmq-mang usermod -a -G intelmq www-data  -> dr
      * 在添加之后若再对该用户添加另外附加组时，使用`usermod -G 附加组名 用户名`会覆盖该用户的之前的附加组。此时，可在usermod 命令中添加一个参数 -a 来实现 `usermod -a -G 附加组名 用户名`.
##
1. fields: A field is a key=value pair.     harmonization
  a event 是多个k-v的结构化日志记录
2. redis列表.
## 使用
1. intelmqctl -h  可以控制intelmq
2. intelmqdump  错误处理，可以检查转储的消息(the message in question)，显示，删除或重新注入
管道。These dumps are saved at /opt/intelmq/var/log/[botid].dump as JSON files.
3.
Pipeline interactions
A can call three methods related to the pipeline:
self.receive_message(): The pipeline handler pops one message from the internal queue if possible. Otherwise one message from the sources list is popped, and added it to an internal queue. In case of errors in process handling, the message can still be found in the internal queue and is not lost. The bot class unravels the message a creates an instance of the Event or Report class.
self.send_message(event): Processed message is sent to destination queues.
self.acknowledge_message(): Message formerly received by receive_message is removed from the internal queue. This should always be done after processing and after the sending of the new message. In case of errors, this function is not called and the message will stay in the internal queue waiting to be processed again.
### 使用要注意的
1. 运行bot前，如果/opt/intelmq/var/run下有对应bot.pid,则应删掉，否则bot运行出错。(命令行运行：run，会结束进程和删掉pid文件；start不会)
2. bot_id命名: 不能出现除了 0-9a-zA-Z(数字、字母)和-  以外的字符


# Developers
1. 所有的目录及文件命名小写，用下划线代替空格。bot目录的名称必须对应于feed名称
2. Class name of the bot (ex: PhishTank Parser) must correspond to the type of the bot (ex: Parser) e.g.  PhishTankParserBot
## 其他
1. IOC（Indicator of Compromise）是MANDIANT在长期的数字取证实践中定义的可以反映主机或网络行为的技术指示器
