pom

```xml
<!-- OceanBase 官方 JDBC 驱动（oracle 模式使用） -->
        <dependency>
            <groupId>com.oceanbase</groupId>
            <artifactId>oceanbase-client</artifactId>
            <version>2.4.1</version>
        </dependency>
```

demo

```java
import java.io.FileDescriptor;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Properties;

/**
 * OceanBase (Oracle 模式) 连接查询示例。
 *
 * <p>连接参数硬编码自 obclient 命令，仅执行一次查询并打印全部结果。</p>
 */
public class OceanBaseQueryDemo {

    // ----- 硬编码连接信息（直接取自 obclient 命令）-----
    private static final String HOST = "10.1.95.201";
    private static final String PORT = "2883";
    // 用户名@租户名#集群名
    private static final String USERNAME = "eds@BQD_EDS#bqd_obcluster_07";
    private static final String PASSWORD = "IqlOtY0iwE";

    // JDBC URL（不指定默认 schema，查询时使用全限定名）
    private static final String URL = String.format("jdbc:oceanbase://%s:%s", HOST, PORT);

    // 硬编码的查询 SQL（Oracle 模式下 DATE 字面量的标准写法）
    private static final String SQL =
            "SELECT * FROM edspure.bonddt WHERE entrydate = DATE '2026-09-03'";

    public static void main(String[] args) {
        // 统一以 UTF-8 输出，避免 Windows 默认 GBK 导致中文乱码
        try {
            System.setOut(new PrintStream(new FileOutputStream(FileDescriptor.out), true, "UTF-8"));
        } catch (java.io.UnsupportedEncodingException e) {
            // 理论上 UTF-8 一定存在，这里忽略即可
        }

        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;

        try {
            // 1. 加载驱动（JDBC 4.0 后一般会自动加载，但显式加载更保险）
            Class.forName("com.oceanbase.jdbc.Driver");

            // 2. 建立连接（用户名密码放入 Properties）
            Properties props = new Properties();
            props.setProperty("user", USERNAME);
            props.setProperty("password", PASSWORD);

            conn = DriverManager.getConnection(URL, props);
            System.out.println("连接 OceanBase 成功！");

            // 3. 执行查询
            stmt = conn.createStatement();
            rs = stmt.executeQuery(SQL);

            // 4. 动态打印结果集（列数/列名取自元数据，避免硬编码）
            ResultSetMetaData meta = rs.getMetaData();
            int columnCount = meta.getColumnCount();

            printHeader(meta, columnCount);
            int rowCount = printRows(rs, columnCount);

            System.out.println("查询完成，共返回 " + rowCount + " 行数据。");

        } catch (ClassNotFoundException e) {
            System.err.println("找不到 JDBC 驱动，请检查 oceanbase-client 依赖。");
            e.printStackTrace();
        } catch (SQLException e) {
            System.err.println("数据库连接或查询失败！");
            e.printStackTrace();
        } finally {
            // 5. 逆序关闭资源
            closeQuietly(rs);
            closeQuietly(stmt);
            closeQuietly(conn);
        }
    }

    /** 打印列头，列之间用制表符分隔（便于在终端里阅读）。 */
    private static void printHeader(ResultSetMetaData meta, int columnCount) throws SQLException {
        StringBuilder header = new StringBuilder();
        for (int i = 1; i <= columnCount; i++) {
            if (i > 1) {
                header.append('\t');
            }
            header.append(meta.getColumnName(i));
        }
        System.out.println(header);
    }

    /** 逐行打印数据，返回总行数。 */
    private static int printRows(ResultSet rs, int columnCount) throws SQLException {
        int rowCount = 0;
        while (rs.next()) {
            StringBuilder line = new StringBuilder();
            for (int i = 1; i <= columnCount; i++) {
                if (i > 1) {
                    line.append('\t');
                }
                line.append(rs.getString(i));
            }
            System.out.println(line);
            rowCount++;
        }
        return rowCount;
    }

    /** 忽略异常的关闭工具方法。 */
    private static void closeQuietly(AutoCloseable resource) {
        if (resource != null) {
            try {
                resource.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}

```

