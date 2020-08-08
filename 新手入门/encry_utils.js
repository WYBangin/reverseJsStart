var CryptoJS = require("crypto-js");


function md5(c) {
    return CryptoJS.MD5(c).toString()
}

function bs64_encode(t) {
    return CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(t))
}

function base64_decode(t) {
    return CryptoJS.enc.Base64.parse(t).toString(CryptoJS.enc.Utf8)
}

function hmac_sha256(encry_str, key) {
    return CryptoJS.HmacSHA256(encry_str, key).toString()
}

// var aa = "d77f7fcff637bc61bfb82fcbcd767bfa"   // 密钥
// var bb = "YXBwS2V5PWM5NzgyM2UyODFjMDcxYzM5ZSZkb21haW49d3d3LnlhYm8yNTkuY29tJm5hbWU9YWRtaW4mbm9uY2Vfc3RyPWUzOGkyN3ZvYmQmcGFzc3dvcmQ9MTIzNDU2JnRpbWVzdGFtcD0xNTk2ODY4OTE2JnV1aWQ9d2ViLVdpbmRvd3MtYzJiYmRlZmY0ODQ1NWM3NDU5OWVlNmNiMDJiZTJkOTEmYXBwU2VjdXJpdD1kNzdmN2ZjZmY2MzdiYzYxYmZiODJmY2JjZDc2N2JmYQ=="
// console.log(hmac_sha256(bb, aa))
