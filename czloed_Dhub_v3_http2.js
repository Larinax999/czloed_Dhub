const fs = require('fs');
const proxy = [];
["http_1_03_09_21.txt","http_2_03_09_21.txt","http_3_03_09_21.txt","http_4_03_09_21.txt"].forEach((filename)=>{
	fs.readFileSync(filename, 'utf-8').split(/\r?\n/).forEach(function(p){proxy.push(p)});
});
const http = require('http');
const tls = require('tls');
const http2 = require('http2');
const axios = require('axios');
const i = process.argv[2];
const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));
const key = "91b4e564d4ef5b7d58a240d2058d0692";
const username = "0x99a " + makeid(3)
let payload = {};
// to avoid errors
process.on('uncaughtException',(err)=>{console.log(err);a()});
process.on('unhandledRejection',(err)=>{console.log(err);a()});

const post = (body,i,proxy,port) => new Promise((resolve) => {

	const req1 = http.request({
	  method: 'CONNECT',
	  host: proxy,
	  port: port,
	  path: 'discord.com'
	})
	req1.end();
	
	req1.on('socket', function (socket) {
		socket.setTimeout(3100);  
		socket.on('timeout', function() {
			req1.abort();
		});
	});
	
	req1.on('connect', (res, socket) => {
		console.log("connect localhost to proxy");
		const client = http2.connect("https://discord.com",{
			createConnection: () => tls.connect({
				socket: socket,
				rejectUnauthorized: false,
				ALPNProtocols: ['h2']
			})
		});
		console.log("connect proxy to discord");
		const buffer = Buffer.from(JSON.stringify(body));
		const req = client.request({
			":scheme": "https",
			":method": "POST",
			":path":"/api/v9/auth/register",
			"Content-Type": "application/json",
			"Content-Length": buffer.length,
			"cookie": "OptanonConsent=version=6.17.0; locale=en",
			"referrer": "https://discord.com/invite/" + i,
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84",
			"x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkyLjAuNDUxNS4xMzEgU2FmYXJpLzUzNy4zNiBFZGcvOTIuMC45MDIuNzMiLCJicm93c2VyX3ZlcnNpb24iOiI5Mi4wLjQ1MTUuMTMxIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTQyOTQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
		});
		req.setEncoding('utf8');
		let data = [];
		req.on('data', (chunk) => {
			data.push(chunk);
		});
		req.write(buffer);
		req.end();
		req.on('end', () => {
			console.log(data.join(""))
			resolve(JSON.parse(data.join("")));
		});
	});
});
function makeid(length) {
	var result = '';
	var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
	var charactersLength = characters.length;
	for ( var i = 0; i < length; i++ ) {
	  result += characters.charAt(Math.floor(Math.random() * charactersLength));
   }
   return result;
}

async function a(){
	while (true) {
		let p = proxy[Math.floor(Math.random()*proxy.length)];
		p = p.split(":")
		console.log("try")
		const res = await post(payload,i,p[0],parseInt(p[1]));
		if (res.token) {
			console.log(res)
			//axios.post("http://185.117.3.23:4378/?token={token}&guild={gi}&chid={ci}")
			console.log(`[*] username : ${username}`);
			process.exit(0);
		}
	}
}


(async ()=>{
	const taskid = await axios.post("http://api.capmonster.cloud/createTask",JSON.stringify({"clientKey":key,"task":{"type":"HCaptchaTaskProxyless","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73","websiteURL":"https://discord.com/invite/" + i,"websiteKey":"f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"}})).then(res=>{return res.data.taskId});
	while (true) {
		let d = await axios.post('http://api.capmonster.cloud/getTaskResult', JSON.stringify({"clientKey":key, 'taskId': taskid})).then(res=>{return res.data});
		if (d.status == "ready") {
			console.log("[captcha] ok")
			payload = {
				"captcha_key": d.solution.gRecaptchaResponse,
				"consent": true,
				"fingerprint": "",
				"gift_code_sku_id": null,
				"invite": i,
				"username": username
			}
			break
		}
		await delay(1500)
	}
	await a()
})();
/*
89.163.220.14:443
194.233.73.103:443
194.233.73.109:443
194.233.73.105:443
*/