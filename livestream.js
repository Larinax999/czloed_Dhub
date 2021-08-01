var cluster = require('cluster');

if (cluster.isMaster) {
	/*
	var port = 8080;
	var express = require('express');
	var app = express()
	app.post('/', function (req, res) {
		res.send('online')
	})
	app.post('/', function (req, res) {
		let worker = cluster.fork();
		worker.send({
			"token": req.query.token,
			"channel": req.query.ch,
			"guild": req.query.guild
		});
		res.send('Done')
	})
	cluster.on('online', function(worker) {
		console.log('Worker ' + worker.process.pid + ' is online');
	});
	app.listen(port, () => {
	  console.log(`Example app listening at http://localhost:${port}`)
	})
	*/
	let i = 0;
	require('fs').readFileSync('token_rice.txt', 'utf-8').split(/\r?\n/).forEach(function(line){
	  let worker = cluster.fork();
		worker.send({
			"token": line,
			"channel": '848332089324601344',
			"guild": '844612239969484800'
		});
		i++;
		console.log('start thread : ' + i);
	})
	/*
	let worker = cluster.fork();
	worker.send({
		"token" : "ODU2OTc0Mjk4NjA2ODYyMzc4.YNI1hA.1CHD4yq4ALN9X7RySV9H87kfPno",
		"channel": '841450484678262798',
		"guild": '841450484678262794'
	})
	*/
} else {
    process.on('message', function(message) {
        const WebSocket = require("ws")
        const EventEmitter = require('events');
        const pack = (d) => JSON.stringify(d);
        const unpack = (d) => JSON.parse(d);
        class Client extends EventEmitter {
            constructor() {
                super();
                this.ws = null;
                this.token = null;
                //this.mediaStream = null;
                //this.mediaRecorder = null;
                this.user = {}
                this.on("READY", (data) => {
                    this.user = data.user
                })
            }
            login(token) {
                this.token = token
                this.ws = new WebSocket('wss://gateway.discord.gg/?v=8&encoding=json');
                this.ws.on('open', () => {
                    //ws.send('something');
                    this.send({
                        "op": 2,
                        "d": {
                            "token": this.token,
                            "properties": {
                                "$os": "windows",
                                "$browser": "Discord",
                                "$device": "desktop"
                            }
                        }
                    })
                })

                this.ws.on("message", (msg) => {

                    msg = unpack(msg)

                    switch (msg.op) {
                        case 10:

                            setInterval(() => {
                                this.send({
                                    "op": 1,
                                    "d": null
                                })

                            }, msg.d.heartbeat_interval);
                            break;

                        case 0: //event lisner

                            this.emit(msg.t, msg.d)
                            break;

                        default:

                            console.log(msg)
                            break;
                    }
                })

                this.ws.on("close", (e) => {
                    console.log('WebSocket Close', e);
                })
            }
            send(msg) {
                this.ws.send(pack(msg))
            }
        }
        const bot = new Client();

        bot.on("READY", () => {
            bot.send({
                "op": 4,
                "d": {
                    "guild_id": message.guild,
                    "channel_id": message.channel,
                    "self_mute": true,
                    "self_deaf": true
                }
            })
        })

        bot.on("VOICE_STATE_UPDATE", (state) => {
            if (state.user_id == bot.user.id) {
                bot.user.voice = state
            }
        })

        bot.on("VOICE_SERVER_UPDATE", (server) => {
            bot.send({
                "op": 18,
                "d": {
                    "type": "guild",
                    "guild_id": bot.user.voice.guild_id,
                    "channel_id": bot.user.voice.channel_id,
                    "preferred_region": "singapore"
                }
            }) //Start Live stream
        })
        bot.login(message.token)
    });
}