// as cp生成
function ti(e, t) {
    var n = (65535 & e) + (65535 & t)
      , r = (e >> 16) + (t >> 16) + (n >> 16);
    return r << 16 | 65535 & n
}
function n(e, t) {
    return e << t | e >>> 32 - t
}
function r(e, r, o, i, u, a) {
    return ti(n(ti(ti(r, e), ti(i, a)), u), o)
}
function o(e, t, n, o, i, u, a) {
    return r(t & n | ~t & o, e, t, i, u, a)
}
function i(e, t, n, o, i, u, a) {
    return r(t & o | n & ~o, e, t, i, u, a)
}
function u(e, t, n, o, i, u, a) {
    return r(t ^ n ^ o, e, t, i, u, a)
}
function a(e, t, n, o, i, u, a) {
    return r(n ^ (t | ~o), e, t, i, u, a)
}
function s(e, n) {
    e[n >> 5] |= 128 << n % 32,
    e[(n + 64 >>> 9 << 4) + 14] = n;
    var r, s, c, l, f, p = 1732584193, d = -271733879, h = -1732584194, m = 271733878;
    for (r = 0; r < e.length; r += 16)
        s = p,
        c = d,
        l = h,
        f = m,
        p = o(p, d, h, m, e[r], 7, -680876936),
        m = o(m, p, d, h, e[r + 1], 12, -389564586),
        h = o(h, m, p, d, e[r + 2], 17, 606105819),
        d = o(d, h, m, p, e[r + 3], 22, -1044525330),
        p = o(p, d, h, m, e[r + 4], 7, -176418897),
        m = o(m, p, d, h, e[r + 5], 12, 1200080426),
        h = o(h, m, p, d, e[r + 6], 17, -1473231341),
        d = o(d, h, m, p, e[r + 7], 22, -45705983),
        p = o(p, d, h, m, e[r + 8], 7, 1770035416),
        m = o(m, p, d, h, e[r + 9], 12, -1958414417),
        h = o(h, m, p, d, e[r + 10], 17, -42063),
        d = o(d, h, m, p, e[r + 11], 22, -1990404162),
        p = o(p, d, h, m, e[r + 12], 7, 1804603682),
        m = o(m, p, d, h, e[r + 13], 12, -40341101),
        h = o(h, m, p, d, e[r + 14], 17, -1502002290),
        d = o(d, h, m, p, e[r + 15], 22, 1236535329),
        p = i(p, d, h, m, e[r + 1], 5, -165796510),
        m = i(m, p, d, h, e[r + 6], 9, -1069501632),
        h = i(h, m, p, d, e[r + 11], 14, 643717713),
        d = i(d, h, m, p, e[r], 20, -373897302),
        p = i(p, d, h, m, e[r + 5], 5, -701558691),
        m = i(m, p, d, h, e[r + 10], 9, 38016083),
        h = i(h, m, p, d, e[r + 15], 14, -660478335),
        d = i(d, h, m, p, e[r + 4], 20, -405537848),
        p = i(p, d, h, m, e[r + 9], 5, 568446438),
        m = i(m, p, d, h, e[r + 14], 9, -1019803690),
        h = i(h, m, p, d, e[r + 3], 14, -187363961),
        d = i(d, h, m, p, e[r + 8], 20, 1163531501),
        p = i(p, d, h, m, e[r + 13], 5, -1444681467),
        m = i(m, p, d, h, e[r + 2], 9, -51403784),
        h = i(h, m, p, d, e[r + 7], 14, 1735328473),
        d = i(d, h, m, p, e[r + 12], 20, -1926607734),
        p = u(p, d, h, m, e[r + 5], 4, -378558),
        m = u(m, p, d, h, e[r + 8], 11, -2022574463),
        h = u(h, m, p, d, e[r + 11], 16, 1839030562),
        d = u(d, h, m, p, e[r + 14], 23, -35309556),
        p = u(p, d, h, m, e[r + 1], 4, -1530992060),
        m = u(m, p, d, h, e[r + 4], 11, 1272893353),
        h = u(h, m, p, d, e[r + 7], 16, -155497632),
        d = u(d, h, m, p, e[r + 10], 23, -1094730640),
        p = u(p, d, h, m, e[r + 13], 4, 681279174),
        m = u(m, p, d, h, e[r], 11, -358537222),
        h = u(h, m, p, d, e[r + 3], 16, -722521979),
        d = u(d, h, m, p, e[r + 6], 23, 76029189),
        p = u(p, d, h, m, e[r + 9], 4, -640364487),
        m = u(m, p, d, h, e[r + 12], 11, -421815835),
        h = u(h, m, p, d, e[r + 15], 16, 530742520),
        d = u(d, h, m, p, e[r + 2], 23, -995338651),
        p = a(p, d, h, m, e[r], 6, -198630844),
        m = a(m, p, d, h, e[r + 7], 10, 1126891415),
        h = a(h, m, p, d, e[r + 14], 15, -1416354905),
        d = a(d, h, m, p, e[r + 5], 21, -57434055),
        p = a(p, d, h, m, e[r + 12], 6, 1700485571),
        m = a(m, p, d, h, e[r + 3], 10, -1894986606),
        h = a(h, m, p, d, e[r + 10], 15, -1051523),
        d = a(d, h, m, p, e[r + 1], 21, -2054922799),
        p = a(p, d, h, m, e[r + 8], 6, 1873313359),
        m = a(m, p, d, h, e[r + 15], 10, -30611744),
        h = a(h, m, p, d, e[r + 6], 15, -1560198380),
        d = a(d, h, m, p, e[r + 13], 21, 1309151649),
        p = a(p, d, h, m, e[r + 4], 6, -145523070),
        m = a(m, p, d, h, e[r + 11], 10, -1120210379),
        h = a(h, m, p, d, e[r + 2], 15, 718787259),
        d = a(d, h, m, p, e[r + 9], 21, -343485551),
        p = ti(p, s),
        d = ti(d, c),
        h = ti(h, l),
        m = ti(m, f);
    return [p, d, h, m]
}
function c(e) {
    var t, n = "";
    for (t = 0; t < 32 * e.length; t += 8)
        n += String.fromCharCode(e[t >> 5] >>> t % 32 & 255);
    return n
}
function l(e) {
    var t, n = [];
    for (n[(e.length >> 2) - 1] = void 0,
    t = 0; t < n.length; t += 1)
        n[t] = 0;
    for (t = 0; t < 8 * e.length; t += 8)
        n[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
    return n
}
function f(e) {
    return c(s(l(e), 8 * e.length))
}
function p(e, t) {
    var n, r, o = l(e), i = [], u = [];
    for (i[15] = u[15] = void 0,
    o.length > 16 && (o = s(o, 8 * e.length)),
    n = 0; 16 > n; n += 1)
        i[n] = 909522486 ^ o[n],
        u[n] = 1549556828 ^ o[n];
    return r = s(i.concat(l(t)), 512 + 8 * t.length),
    c(s(u.concat(r), 640))
}
function d(e) {
    var t, n, r = "0123456789abcdef", o = "";
    for (n = 0; n < e.length; n += 1)
        t = e.charCodeAt(n),
        o += r.charAt(t >>> 4 & 15) + r.charAt(15 & t);
    return o
}
function h(e) {
    return unescape(encodeURIComponent(e))
}
function m(e) {
    return f(h(e))
}
function g(e) {
    return d(m(e))
}
function v(e, t) {
    return p(h(e), h(t))
}
function y(e, t) {
    return d(v(e, t))
}
function md5(e, t, n) {
    return t ? n ? v(t, e) : y(t, e) : n ? m(e) : g(e)
}
function create_as_cp() {
    var t = Math.floor((new Date).getTime() / 1e3)
      , e = t.toString(16).toUpperCase()
      , i = md5(t).toString().toUpperCase();
    if (8 != e.length)
        return {
            as: "479BB4B7254C150",
            cp: "7E0AC8874BB0985"
        };
    for (var n = i.slice(0, 5), a = i.slice(-5), s = "", o = 0; 5 > o; o++)
        s += n[o] + e[o];
    for (var r = "", c = 0; 5 > c; c++)
        r += e[c + 3] + a[c];
    return {
        as: "A1" + s + e.slice(-3),
        cp: e.slice(0, 3) + r + "E1"
    }
}
// 26位signature生成，toutiao_signature.js是31位生成方式
function tac_sign(userid){
    Function(function(e) {
        global.navigator={};	//声明一个浏览器得navigator
        global.navigator.userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36";	//给navigator添加一个userAgent，让下面混淆能够正常读取userAgent信息，此userAgent必须和python代码中的headers里的userAgent一模一样。
        return 'e(e,a,r){(b[e]||(b[e]=t("x,y","x "+e+" y")(r,a)}a(e,a,r){(k[r]||(k[r]=t("x,y","new x[y]("+Array(r+1).join(",x[y]")(1)+")")(e,a)}r(e,a,r){n,t,s={},b=s.d=r?r.d+1:0;for(s["$"+b]=s,t=0;t<b;t)s[n="$"+t]=r[n];for(t=0,b=s=a;t<b;t)s[t]=a[t];c(e,0,s)}c(t,b,k){u(e){v[x]=e}f{g=,ting(bg)}l{try{y=c(t,b,k)}catch(e){h=e,y=l}}for(h,y,d,g,v=[],x=0;;)switch(g=){case 1:u(!)4:f5:u((e){a=0,r=e;{c=a<r;c&&u(e[a]),c}}(6:y=,u((y8:if(g=,lg,g=,y===c)b+=g;else if(y!==l)y9:c10:u(s(11:y=,u(+y)12:for(y=f,d=[],g=0;g<y;g)d[g]=y.charCodeAt(g)^g+y;u(String.fromCharCode.apply(null,d13:y=,h=delete [y]14:59:u((g=)?(y=x,v.slice(x-=g,y:[])61:u([])62:g=,k[0]=65599*k[0]+k[1].charCodeAt(g)>>>065:h=,y=,[y]=h66:u(e(t[b],,67:y=,d=,u((g=).x===c?r(g.y,y,k):g.apply(d,y68:u(e((g=t[b])<"<"?(b--,f):g+g,,70:u(!1)71:n72:+f73:u(parseInt(f,3675:if(){bcase 74:g=<<16>>16g76:u(k[])77:y=,u([y])78:g=,u(a(v,x-=g+1,g79:g=,u(k["$"+g])81:h=,[f]=h82:u([f])83:h=,k[]=h84:!085:void 086:u(v[x-1])88:h=,y=,h,y89:u({e{r(e.y,arguments,k)}e.y=f,e.x=c,e})90:null91:h93:h=0:;default:u((g<<16>>16)-16)}}n=this,t=n.Function,s=Object.keys||(e){a={},r=0;for(c in e)a[r]=c;a=r,a},b={},k={};r'.replace(/[-]/g, function(i) {
            return e[15 & i.charCodeAt(0)]
        })
    }("v[x++]=v[--x]t.charCodeAt(b++)-32function return ))++.substrvar .length(),b+=;break;case ;break}".split("")))()('gr$Daten Иb/s!l y͒yĹg,(lfi~ah`{mv,-n|jqewVxp{rvmmx,&effkx[!cs"l".Pq%widthl"@q&heightl"vr*getContextx$"2d[!cs#l#,*;?|u.|uc{uq$fontl#vr(fillTextx$$龘ฑภ경2<[#c}l#2q*shadowBlurl#1q-shadowOffsetXl#$$limeq+shadowColorl#vr#arcx88802[%c}l#vr&strokex[ c}l"v,)}eOmyoZB]mx[ cs!0s$l$Pb<k7l l!r&lengthb%^l$1+s$jl  s#i$1ek1s$gr#tack4)zgr#tac$! +0o![#cj?o ]!l$b%s"o ]!l"l$b*b^0d#>>>s!0s%yA0s"l"l!r&lengthb<k+l"^l"1+s"jl  s&l&z0l!$ +["cs\'(0l#i\'1ps9wxb&s() &{s)/s(gr&Stringr,fromCharCodes)0s*yWl ._b&s o!])l l Jb<k$.aj;l .Tb<k$.gj/l .^b<k&i"-4j!+& s+yPo!]+s!l!l Hd>&l!l Bd>&+l!l <d>&+l!l 6d>&+l!l &+ s,y=o!o!]/q"13o!l q"10o!],l 2d>& s.{s-yMo!o!]0q"13o!]*Ld<l 4d#>>>b|s!o!l q"10o!],l!& s/yIo!o!].q"13o!],o!]*Jd<l 6d#>>>b|&o!]+l &+ s0l-l!&l-l!i\'1z141z4b/@d<l"b|&+l-l(l!b^&+l-l&zl\'g,)gk}ejo{cm,)|yn~Lij~em["cl$b%@d<l&zl\'l $ +["cl$b%b|&+l-l%8d<@b|l!b^&+ q$sign ', [TAC = {}]);
    var signs = TAC.sign(userid);
    return signs
}


// var e = "https://www.toutiao.com/toutiao/stream/widget/local_weather/data/?city=%E5%8C%97%E4%BA%AC";
// var t = {"city": "北京"};

// console.log(tac_sign("3410443345"));
// console.log(create_as_cp())  // 测试as, cp 生成


