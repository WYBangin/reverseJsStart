var CryptoJS = require('crypto-js');


window = global;
key_e = "4tBlCLWFZ3eD93CvDE2lpw==";
key_d = "5opkytHOggKj5utjZOgszg==";

function encryptStr(t, a) {
    var n = CryptoJS.enc.Base64.parse(key_e);
    let c = JSON.stringify({
        id: t.substring(0, t.length - 1),
        sum: a
    });
    console.log(c)
    var i = CryptoJS.enc.Utf8.parse(c)
        , s = CryptoJS.AES.encrypt(i, n, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return s.toString();
}

function decryptStr(e) {
    var t = CryptoJS.enc.Base64.parse(key_d)
        , a = CryptoJS.AES.decrypt(e, t, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return CryptoJS.enc.Utf8.stringify(a).toString()
}

window.deciphering = function (e, t) {
    t = t || 32;
    var a = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678"
        , n = a.length;
    for (let c = 0; c < t; c++)
        a.charAt(Math.floor(Math.random() * n));
    return e;
};

function get_sig(encypt_txt) {
    var content = decryptStr(encypt_txt);
    const a = content.split(",")[0].substring(4);
    const id = content.split(",")[1].split("=")[1];
    const result = eval(a);
    console.log(id, result)
    sig = encryptStr(id, result);
    return sig;
}


// var encypt_txt = "truiLeKm7AKyuie+33QCYQNFwHprzqgdcYqa5NLouvPQSDseJB0UlCSD+ccmBNIlChroi7XTf/+2deEyFX3pnu0wlzp08aP8xHeaxH0Ny3OChgka338HNRNIiVGFn8P+NOsrefRVPPr/OQav5clS8EtJWjIvAoeMfhW4xYTOw7bm1W7GsmE60fr9ko8CFjIWvnXoDGmd5mf7ppPnRoTycw=="
// console.log(get_sig(encypt_txt));
