var cluster = require('cluster').isMaster;

if (cluster) {
	let i = 0;
	cluster = require('cluster');
	require('fs').readFileSync('token_x.txt', 'utf-8').split(/\r?\n/).forEach(function(line){
	  let worker = cluster.fork();
		worker.send({
			"token": line,
			"channel": '841450484678262798',
			"guild": '841450484678262794'
		});
		i++;
		console.log('start thread : ' + i);
	})
} else {
    process.on('message', function(message) {
        const WebSocket = require("ws");
        const pack = (d) => JSON.stringify(d);
		const ws = new WebSocket('wss://gateway.discord.gg/?v=8&encoding=json');
		ws.on('open', () => {
			ws.send(pack({
				"op": 2,
				"d": {
					"token": message.token,
					"properties": {
						"$os": "windows",
						"$browser": "Discord",
						"$device": "desktop"
					}
				}
			}));
		});
		
		ws.on("message", (msg) => {
			msg = JSON.parse(msg);
			if (msg.op == 10) {
				ws.send(pack({"op": 4,"d": {"guild_id": message.guild,"channel_id": message.channel,"self_mute": true,"self_deaf": true}}));
				ws.send(pack({"op": 18,"d": {"type": "guild","guild_id": message.guild,"channel_id": message.channel,"preferred_region": "singapore"}}));
				setInterval(() => {
					ws.send(pack({
						"op": 1,
						"d": null
					}));
				}, msg.d.heartbeat_interval);
			}
		});
    });
}