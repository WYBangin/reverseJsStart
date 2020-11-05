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

// 以下是aes部分
function base64_aes_encrypt(data, key, iv) {
    var aes_key = CryptoJS.enc.Utf8.parse(key);
    const option = {
        iv: CryptoJS.enc.Utf8.parse(iv),
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7,
    };
    var encrypt = CryptoJS.AES.encrypt(JSON.stringify(data), aes_key, option);
    var encrypt_data = encrypt.toString();
    return encrypt_data
}

function base64_aes_decrypt(data, key, iv) {
    var aes_key = CryptoJS.enc.Utf8.parse(key);
    const option = {
        iv: CryptoJS.enc.Utf8.parse(iv),
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7,
    };
    var decrypt = CryptoJS.AES.decrypt(data, aes_key, option);
    var decrypt_data = JSON.parse(decrypt.toString(CryptoJS.enc.Utf8)); //解密后的数据
    return decrypt_data
}

function hex_aes_encrypt(data, key, iv) {
    var aes_key = CryptoJS.enc.Utf8.parse(key);
    const option = {
        iv: CryptoJS.enc.Utf8.parse(iv),
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7,
    };
    var encrypt = CryptoJS.AES.encrypt(JSON.stringify(data), aes_key, option);
    var encrypt_data = encrypt.ciphertext.toString();
    return encrypt_data
}

function hex_aes_decrypt(data, key, iv) {
    var hex_str = CryptoJS.enc.Hex.parse(data);
    var aes_key = CryptoJS.enc.Utf8.parse(key);
    const option = {
        iv: CryptoJS.enc.Utf8.parse(iv),
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7,
    };
    var encrypt = CryptoJS.AES.decrypt({
        ciphertext: hex_str
    }, aes_key, option);
    var decrypt_data = encrypt.toString(CryptoJS.enc.Utf8);
    return decrypt_data

}

// var kk = "20171109124536982017110912453698";
// var vv = "2017110912453698";
// var aa = hex_aes_encrypt("你好", kk, vv);
// console.log(aa);    // 265d267f11e8786094a6ef8bf0d9320f
// console.log(hex_aes_decrypt(aa, kk, vv));
