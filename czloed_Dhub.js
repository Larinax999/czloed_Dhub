// ==UserScript==
// @name         CZLOED Dhub
// @namespace    https://czloed.dev
// @version      0.1
// @description  Discord token generator
// @author       larinax999
// @run-at       document-start
// @match        *://discord.com/czloed_Dhub
// @grant        GM_xmlhttpRequest
// ==/UserScript==

setTimeout(()=>{
    window.stop();
},1);
window.location.reload(true);
const html = `
<style type="text/css">
.btn6{
  padding: 15px 100px;
  margin:10px 4px;
  color: #fff;
  font-family: sans-serif;
  text-transform: uppercase;
  text-align: center;
  position: relative;
  text-decoration: none;
  display:inline-block;

}
.btn6{
  border:1px solid transparent;
   -webkit-transition: all 0.4s cubic-bezier(.5, .24, 0, 1);
  transition: all 0.4s cubic-bezier(.5, .24, 0, 1);
}

.btn6::before {
  content: '';
  position: absolute;
  left: 0px;
  bottom:0px;
  z-index:-1;
  width: 0%;
  height:1px;
  background: #6098FF;
  box-shadow: inset 0px 0px 0px #6098FF;
  display: block;
  -webkit-transition: all 0.4s cubic-bezier(.5, .24, 0, 1);
  transition: all 0.4s cubic-bezier(.5, .24, 0, 1)
}

.btn6:hover::before {
  width:100%;
}

.btn6::after {
  content: '';
  position: absolute;
  right: 0px;
  top:0px;
  z-index:-1;
  width: 0%;
  height:1px;
  background: #6098FF;
  -webkit-transition: all 0.4s cubic-bezier(.5, .24, 0, 1);
  transition: all 0.4s cubic-bezier(.5, .24, 0, 1)
}
.btn6:hover::after {
  width:100%;
}
.btn6:hover{
  border-left:1px solid #6098FF;
  border-right:1px solid #6098FF;
}
</style>
<center>
<h1 style="color: #7289DA;">CZLOED Dhub v2</h1>
<h3 style="color: #7289DA;">by larina</h3>
<input id="ip" type="text" value="127.0.0.1">
<br>
<div>
<a id="loadcap" href="#" class="btn6">load hcaptcha</a>
<a id="reloadcap" href="#" class="btn6">reset hcaptcha</a>
<a id="gencap" href="#" class="btn6">send captcha</a>
</div>
<br>
<div style="margin-top: 20px;" class="h-captcha" data-sitekey="f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34" data-theme="dark"></div>
</center>
`;
/* load my html and clear discord header*/
document.body = document.createElement("body");
document.head.innerHTML = `<meta http-equiv="Content-Security-Policy" content="connect-src 'self' http://* 'unsafe-inline' 'unsafe-eval';">
<title>czloed Dhub</title>`;
document.body.innerHTML = html;

/* load hcaptcha */
function load_cap_api() {
    var btn = document.createElement("script");
    btn.setAttribute("src", "https://hcaptcha.com/1/api.js?hl=en");
    btn.async = true;
    btn.defer = true;
    document.body.appendChild(btn);
}
/* send captcha reponse */
function gen_hcaptcha() {
    var rescap = document.getElementsByTagName("iframe")[0].getAttribute("data-hcaptcha-response");
    var ip = document.getElementById("ip").value;
    fetch(`http://${ip}/?recapkey=${rescap}`, {method:"POST"}).then((res)=>{
        console.log(res.text());
    }).catch(()=> {
        console.log("cannot connect host or error");
    });
}
function reload_hcaptcha() {
    hcaptcha.reset();
}
/* set btn event */
document.getElementById("loadcap").addEventListener("click", load_cap_api);
document.getElementById("gencap").addEventListener("click", gen_hcaptcha);
document.getElementById("reloadcap").addEventListener("click", reload_hcaptcha);

/* set css body */
document.body.style = "background-color: #23272A; font-family: 'Roboto Mono', monospace;";