document.getElementById("uranai-btn").addEventListener("click", function() {
 const results = ["超大吉","大吉","大吉","中吉","中吉","吉","吉","小吉","小吉"];//結果の配列を作る
const images = {
  "超大吉": "uranai_choudaikiti.png",//画像と配列の中身を結びつける辞書のような役割
  "大吉": "uranai_daikiti.png",
  "中吉": "uranai_chuukiti.png",
  "吉": "uranai_kiti.png",
  "小吉": "uranai_syoukiti.png"
  };
const re_number = Math.floor(Math.random()*results.length);
const resultText  = results[re_number]
const resultImage = images[resultText];

 const resultElement = document.getElementById("result");//下記で運勢の文字と画像を、画面に表示するためのもの。（HTMLとCSSと結びつける）

  resultElement.innerHTML = `
    <h2>${resultText}！</h2>
    <img src="images/${resultImage}" alt="${resultText}" class="result-img">
  `;
});