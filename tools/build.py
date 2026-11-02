"""把 src/page.html 與 assets 內的圖片內嵌成單一檔案 index.html（雙擊即可離線開啟）。"""
import base64, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
b64 = lambda p: base64.b64encode((root/p).read_bytes()).decode()
html = (root/'src/page.html').read_text(encoding='utf-8')
html = html.replace('__BASE__', 'data:image/jpeg;base64,' + b64('assets/xsr700-white.jpg'))
html = html.replace('__MASK__', 'data:image/png;base64,' + b64('assets/xsr700-mask.png'))
(root/'index.html').write_text(html, encoding='utf-8')
print('built index.html', len(html)//1024, 'KB')
