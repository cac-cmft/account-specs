# 查询用户的账户余额

假设有如下用户在系统中拥不同币种的账户，并且账户中有如下余额（"N/A"表示帐户不支持对应币种）

   |user     |account|balance_in_cny|balance_in_eur|
   |---------|-------|--------------|--------------|
   |qinyu    |1001   |1000.00       |N/A           |
   |qinyu    |1002   |N/A           |300.00        |
   |qinyu    |1003   |5000.00       |100.00        |
   |zhongjing|2001   |2000.00       |200.00        |

## 查询所有账户

* 用户"qinyu"查询所有账户的余额
* 他应该看到如下结果：

   |account|balance_in_cny|balance_in_eur|
   |-------|--------------|--------------|
   |1001   |1000.00       |N/A           |
   |1002   |N/A           |300.00        |
   |1003   |5000.00       |100.00        |

## 查询所有账户

* 用户"qinyu"查询所有账户的余额
* 他应该看到如下结果：

   |account|balance_in_cny|balance_in_eur|
   |-------|--------------|--------------|
   |1001   |1000.00       |N/A           |
   |1002   |N/A           |300.00        |
   |1003   |5000.00       |100.00        |

## 查询某一个账户

* 用户"qinyu"查询账户"1003"的余额
* 他应该看到如下结果：

   |account|balance_in_cny|balance_in_eur|
   |-------|--------------|--------------|
   |1003   |5000.00       |100.00        |

## 查询出错

   |account|error_message                 |
   |-------|------------------------------|
   |9999   |账户9999不存在，请核对账户    |
   |2001   |您无权查询账户2001，请核对账户|

* 用户"qinyu"查询账户<account>余额时，应该提示<error_message>
