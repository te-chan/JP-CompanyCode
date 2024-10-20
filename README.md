# JP-CompanyCode
日本の株式コードをJPXから毎日更新し、CSVで提供します。

## CSVリンク

[株式コードCSVダウンロード](https://te-chan.github.io/JP-CompanyCode/company_list.csv)

### curl

```bash
$ curl -O https://te-chan.github.io/JP-CompanyCode/company_list.csv
```

### python
```python
import requests
import pandas as pd

# CSVデータのURL
url = 'https://te-chan.github.io/JP-CompanyCode/company_list.csv'

# CSVデータをダウンロード
response = requests.get(url)
response.raise_for_status()  # エラーチェック

# 一時ファイルに保存
with open('company_list.csv', 'wb') as file:
    file.write(response.content)

# 保存したCSVファイルをDataFrameとして読み込む
data = pd.read_csv('company_list.csv')

# DataFrameを表示
print(data)
```

## 貢献方法

問題があればIssue,またはPRをお願いします。

## 免責事項

有志で行っています。何か問題が発生した場合、一切の責任を負いません。

## ライセンス

MIT
