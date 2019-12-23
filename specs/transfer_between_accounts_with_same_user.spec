# 在不同用户的账户之间转账

汇率服务使用的是：[fixer.io](https://fixer.io/documentation)  
浮点数舍入使用：[Round_half_to_even](https://simple.wikipedia.org/wiki/Rounding#Round_half_to_even)

假设有如下用户在系统中拥不同币种的账户，并且账户中有如下余额（"N/A"表示帐户不支持对应币种）

   |user     |account|balance_in_cny|balance_in_eur|
   |---------|-------|--------------|--------------|
   |qinyu    |1001   |1000.00       |N/A           |
   |qinyu    |1002   |N/A           |300.00        |
   |zhongjing|2001   |2000.00       |200.00        |

## 在同一币种账户之间转账

* 用户"qinyu"从账户"1001"向用户"zhongjing"的账户"2001"转账"100.00 CNY"
* 转账应该成功完成
* 并且"qinyu"和"zhongjing"的账户余额应该如下： 

   |user     |account|balance_in_cny|balance_in_eur|
   |---------|-------|--------------|--------------|
   |qinyu    |1001   |900.00        |N/A           |
   |zhongjing|2001   |2100.00       |200.00        |

* 用户"qinyu"从账户"1002"向用户"zhongjing"的账户"2001"转账"100.00 EUR"
* 转账应该成功完成
* 并且"qinyu"和"zhongjing"的账户余额应该如下： 

   |user     |account|balance_in_cny|balance_in_eur|
   |---------|-------|--------------|--------------|
   |qinyu    |1002   |N/A           |200.00        |
   |zhongjing|2001   |2000.00       |300.00        |

* 用户"qinyu"从账户"1001"向用户"zhongjing"的账户"2001"转账"1001.00 CNY"
* 转账无法完成，提示错误消息"1001 余额不足"
* 并且"qinyu"和"zhongjing"的账户余额应该如下： 

   |user     |account|balance_in_cny|balance_in_eur|
   |---------|-------|--------------|--------------|
   |qinyu    |1001   |1000.00       |N/A          |
   |zhongjing|1002   |2000.00       |200.00        |

## 在不同币种账户之间转账

假设当时"EUR"对"CNY"的汇率是"7.771705"

* 用户"zhongjing"从账户"2001"向用户"qinyu"的账户"1002"转账"100.00 CNY"
* 转账应该成功完成
* 并且"qinyu"和"zhongjing"的账户余额应该如下： 

   |user     |account|balance_in_cny|balance_in_eur|
   |---------|-------|--------------|--------------|
   |qinyu    |1002   |N/A           |312.87        |
   |zhongjing|1002   |1900          |200.00        |

* 用户"zhongjing"从账户"2001"向用户"qinyu"的账户"1001"转账"0.50 EUR"
* 转账应该成功完成
* 并且"qinyu"和"zhongjing"的账户余额应该如下： 

   |user     |account|balance_in_cny|balance_in_eur|
   |---------|-------|--------------|--------------|
   |qinyu    |1001   |1003.89       |N/A           |
   |zhongjing|2001   |2000          |199.50        |
