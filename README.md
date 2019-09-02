# phase-only-correlation

位相限定相関法による、サイトスクリーンショットの位置ずれ検出

## Environment

- サンプルサイト
    - 行間の少しずれたサイトを2つ用意
    - 言語・フレームワーク
        - Python: `3.7.0`
        - Flask: `1.0.2`
        - NumPy: `1.15.1`
        - OpenCV: `4.1.0`
- スクリーンショット撮影
    - サンプルサイトのスクリーンショット撮影
    - 言語・フレームワーク
        - Node.js: `10.16.2`
            - yarn: `1.17.3`
        - Puppeteer

***

## Setup

### Install Puppeteer
```bash
# Puppeteer: Headless Chrome Browser API
$ yarn add -D puppeteer
```


### Install Python packages
```bash
# Flask: Micro web framework
$ pip install flask

# NumPy: Efficient multi-dimensional container of generic data
$ pip install numpy

# OpenCV: Library including several hundreds of computer vision algorithms
$ pip install opencv-python
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
    - **puppeteer/screenshot.js**
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

***

## 位相限定相関

### 単純な計算
- **poc.py**
    ```python
    import numpy as np
    import cv2

    # 画像を読み込み Array{Float32,1} に変換
    def load_img(filename: str) -> np.ndarray:
        # cv2.imread の第2引数を0にするとグレースケールで読み込む
        return np.float32(cv2.imread(filename, 0))

    if __name__ == "__main__":
        # sample1, sample2 画像読み込み
        img1: np.ndarray = load_img('./puppeteer/screenshot/sample1.png')
        img2: np.ndarray = load_img('./puppeteer/screenshot/sample2.png')
        # 位相限定相関を計算
        (dx, dy), etc = cv2.phaseCorrelate(img1, img2)
        print(f'({dx}, {dy}), {etc}')
    ```
- 実行結果:
    ```bash
    $ python poc.py
    (0.010397262925721407, -0.001163075541398939), 0.7413033304850261
    ```
    - 横のズレ: ~0.0104
    - 縦のズレ: ~0.0012
    - 一致率: ~74 %
- 考察:
    - 行ごとのズレがある以上、各行を一つのオブジェクトとして各々のズレを検出しないと意味がない
