import fitz

doc = fitz.open("C:/Users/10x/OneDrive/デスクトップ/Shinjo Tobatsu/1.Reference/English/Advanced English/3rd/2022_busjigyo.pdf") # ドキュメントを開く
out = open("output.txt", "wb") # テキスト出力を作成する
for page in doc: # ドキュメントのページを反復処理する
    text = page.get_text().encode("utf8") # プレーンテキストを取得する（UTF-8形式）
    out.write(text) # ページのテキストを書き込む
    out.write(bytes((12,))) # ページ区切り（フォームフィード0x0C）を書き込む
out.close()