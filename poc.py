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
