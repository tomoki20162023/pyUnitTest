# memo

## pandocでテンプレートを使った、markdownからhtmlへの変換
>> pandoc --toc --template=template.html -f markdown -t html -s -o testrm.html testrm.md

## test reportの出力方法をどうするか
- 画面ごとにHTMLを分ける
- 可能であればExcel出力する
- テストケースの要約を上に出力する
- スクリーンショットなど各テストケースの情報は下の方にまとめて出力する
- 要約にリンクを付けて、詳細情報へ跳べるようにする

### 要約の情報
- 出力用のメソッドを作って、テストメソッド毎に足していく

### 詳細の情報
- 出力用のメソッドを作って、一時ファイルにバッファしておく
- テストが終わったら、HTMLへ結合


