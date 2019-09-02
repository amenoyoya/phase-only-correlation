const puppeteer = require('puppeteer');

// 同期処理する
(async () => {
  const browser = await puppeteer.launch({
    headless: false,  // 動作確認するためheadlessモードにしない
    slowMo: 500  // 動作確認しやすいようにpuppeteerの操作を遅延させる
  });
  const page = await browser.newPage();
  
  page.setViewport({width: 1200, height: 800})
  await page.goto('http://localhost:5000') // サンプルサイト訪問
  await page.screenshot({ path: 'screenshot/sample1.png' }) // スクリーンショット撮影

  await page.goto('http://localhost:5000/?site=2') // サンプルサイト2
  await page.screenshot({ path: 'screenshot/sample2.png' })

  await browser.close()
})();
