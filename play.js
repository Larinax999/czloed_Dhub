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
	require('fs').readFileSync('token.txt', 'utf-8').split(/\r?\n/).forEach(function(line){
	  let worker = cluster.fork();
		worker.send({
			"token": line,
			"channel": '844612239969484804',
			"guild": '844612239969484800'
		});
		i++
		console.log('start thread : ' + i)
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
        const Discord = require('discord.js');
		const ytdl = require('ytdl-core');
		const client = new Discord.Client(
			{intents: ["GUILD_MESSAGES", "GUILD_VOICE_STATES", "GUILDS"]}
		);
		client.on('ready', () => {
			console.log(`\nONLINE\n`);
			const voiceChannel = client.channels.get(message.channel);
			voiceChannel.join().then(connection => {
					console.log("connected")
					const stream = ytdl('https://www.youtube.com/watch?v=COigUXDYJcM', { filter : 'audioonly' });
					connection.playStream(stream, { seek: 0, volume: 100 });
				}).catch(err => { throw err; });
		});
		client.login(message.token);
    });
}