var CryptoJS = require("crypto-js");    // 导入加密包
var f = CryptoJS.enc.Utf8.parse("jo8j9wGw%6HbxfFn");
var m = CryptoJS.enc.Utf8.parse("0123456789ABCDEF");

function decrypt_str(t) {
    var e = CryptoJS.enc.Hex.parse(t)
        , n = CryptoJS.enc.Base64.stringify(e)
        , a = CryptoJS.AES.decrypt(n, f, {
        iv: m,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    })
        , r = a.toString(CryptoJS.enc.Utf8);
    return r.toString()
}

// var e = "95780ba0943730051dccb5fe3918f9fe4c6612ab8a332ee7d1067088471faa62ac26eaae3bb1029f6df01972a054b69bd1251185b999f427e1602cca196ce79ba3d15b3008a91cf22e7be9b09cd00c55d5812b89d7c8120f191c97b8037d80619ce834673dc2dac681cabe2c241df066ecb224548bdcaae5eef9c42e93e7141a627eaed26dcc92bfec7daf5621302ccd4e52cfce042574ec9fd4cdec2487df2abf8c784e6786489caacbf0a65cf921d1ee309d3099fec4d895ae36698b411fc6bea7219c7865ace97fc5b0ab003d42efacd19002ff2cae935467a7e82d2a5a3067e36bd41970e17baa44f68415f89029500e63a23a16993d90e36ec5e70a0da875cf9466db984e206101a2fca5c5de8889baa08976c8cb882839f15224697df7f5fb88d4154a07d93e081135e19efd6bb05a712ec6b837e3818a93aa07a6ffface5f33abfb8770f1bff5a8e00fdd8535f6aae5c3354fa574a546ce7a677d1da43eda9b60d195c888939c1e4df97ccff10f8c6c70fd7d5f3fc7193de012a31d7cd60e51db795fdf6f6dd8aa61edabb428"
// console.log(h(e));

// http://jzsc.mohurd.gov.cn/home