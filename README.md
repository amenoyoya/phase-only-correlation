# phase-only-correlation

位相限定相関法による、サイトスクリーンショットの位置ずれ検出

## Environment

- サンプルサイト
    - 行間の少しずれたサイトを2つ用意
    - 言語・フレームワーク
        - Python: `3.7.0`
        - Flask: `1.0.2`
- スクリーンショット撮影
    - サンプルサイトのスクリーンショット撮影
    - 言語・フレームワーク
        - Node.js: `10.16.2`
            - yarn: `1.17.3`
        - Puppeteer

***

## Setup

### Install Puppetter
```bash
# Puppeteer: Headless Chrome Browser API
$ yarn add -D puppeteer
```

### Test run
- サンプルサイト準備
    - **sample-site/server.py**
        ```python
        from flask import Flask, render_template
        from typing import Tuple

        app = Flask(__name__)

        @app.route('/', methods=['GET'])
        def home() -> Tuple[str, int]:
            return render_template('home.jinja')

        if __name__ == "__main__":
            app.run(debug=True, port=5000, host='0.0.0.0')
        ```
    - サーバー起動
        ```bash
        $ cd sample-site/
        $ python server.py
        ```
- Puppeteerでサンプルサイトのスクリーンショット撮影
    - **screenshot.js**
        ```javascript
        const puppeteer = require('puppeteer');
        
        // 同期処理する
        (async () => {
        const browser = await puppeteer.launch({
            headless: false,  // 動作確認するためheadlessモードにしない
            slowMo: 500  // 動作確認しやすいようにpuppeteerの操作を遅延させる
        });
        const page = await browser.newPage();
        
        await page.goto('http://localhost:5000') // サンプルサイト訪問
        await page.screenshot({ path: 'screenshot/sample1.png' }) // スクリーンショット撮影
        
        await browser.close()
        })();
        ```
    - 実行
        ```bash
        $ node screenshot.js
        ```
