jdbc驱动：https://repo1.maven.org/maven2/com/oceanbase/oceanbase-client/2.4.18/

#### 1. 在 DBeaver 中创建新驱动

下载好 JAR 文件后，就可以在 DBeaver 里动手配置了。

1. 打开 DBeaver，点击菜单栏的 **数据库 → 驱动管理器**-[-1](https://open.oceanbase.com/blog/27407905136)。
2. 在弹出的窗口中，点击 **新建** 按钮，创建一个自定义驱动-[-1](https://open.oceanbase.com/blog/27407905136)。

#### 2. 填写驱动核心参数

在“新建驱动”窗口中，需要填写以下关键信息：

- **驱动名称**：随意填写，例如 `OceanBase Oracle`，只要自己能识别就好。
- **类名**：填入 `com.alipay.oceanbase.jdbc.Driver`
- **URL 模板**：填入 `jdbc:oceanbase://{host}:{port}`

#### 3. 添加驱动 JAR 包

完成基本信息填写后，切换到 **"库"** 选项卡，点击 **添加文件** 按钮，然后选择你在第一步下载好的 OceanBase JDBC 驱动 JAR 包。


#### 4. 使用新驱动建立连接

填写ip、端口、用户名（包含租户和集群，如eds@BQD_EDS#bqd_obcluster_07）、密码


#### 5. 设置“连接初始化 SQL”
查询当前会话的默认 Schema

```
SELECT SYS_CONTEXT('USERENV', 'CURRENT_SCHEMA') FROM DUAL;
```


1. 编辑连接 -> 切换到 **“初始化”** 选项卡（Driver properties 旁边）。

2. 勾选 **“连接后执行SQL脚本”**（或类似选项，英文是 `After connection`）。

3. 在文本框中输入：

   ```
   ALTER SESSION SET CURRENT_SCHEMA = EDSPURE;
   ```



查看哪些表：

```javascript
SELECT * FROM ALL_TABLES WHERE OWNER = 'EDSPURE';
```

