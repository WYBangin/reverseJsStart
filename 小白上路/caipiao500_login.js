// http://wwww-caipiao500.com/login

var CryptoJS = require("crypto-js");


function s(c) {
    return CryptoJS.MD5(c).toString()
}
function base64_encrypt(t) {
    return CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(t))
}

function c(e, t) {
    return s(e.toLowerCase() + s(t))
}

function get_enrypt_pwd(e) {
    var t = "dafacloud_" + Math.random()
      , a = {
        random: base64_encrypt(t)
    }
      , i = c(e.userName, e.password);
    e.password = s(i + t);
    e.random = a.random;
    return e
}



var aa = {"userName": "AA123", "password": "123456"}
console.log(get_enrypt_pwd(aa));
