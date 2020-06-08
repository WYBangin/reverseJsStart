const Koa = require('koa');
const app = new Koa();
const Router = require("koa-router");
const router = new Router();

var CryptoJS = require("crypto-js");

function encrypt(word) {
    var key = CryptoJS.enc.Utf8.parse("xiamenair1234567");
    var srcs = CryptoJS.enc.Utf8.parse(word);
    var encrypted = CryptoJS.AES.encrypt(srcs, key, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return encrypted.toString();
}

// 访问形式http://127.0.0.1:3000/encry/123456
router.get('/encry/:id', ctx => {
    let a = ctx.params.id;
    console.log("/encry/接收的参数是:" + a)
    var i = encrypt(a);
    ctx.body = i;
    console.log(i);
})

router.get("/encry/", ctx => {
    let a = ctx.query.id;
    console.log("/encry/?id=接收的参数是:" + a)
    var i = encrypt(a);
    ctx.body = i;
    console.log(i);
});

app.use(router.routes()).use(router.allowedMethods());
app.listen(3000);
