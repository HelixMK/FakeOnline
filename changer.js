const SteamUser = require('steam-user');
const puppeteer = require('puppeteer');

const newpassword="eblanProductions228"

var accs=[
// steam login, steam password, mail password
["zebrahack228","Zebrakrut2210","bMAIUu5noy1("],
];


for(i in accs){
	try{
		var client = new SteamUser();

		client.logOn({
			"accountName": accs[i][0],
			"password": accs[i][1]
		});

		client.on('error', function(e) {
			console.log(accs[i][0]+' '+accs[i][1],e);
		});

		client.on('emailInfo', function(mail, validated) {
			var domain = mail.split("@")[1];
			if(domain == "inbox.ru")
				domain = "mail.ru"
			if(domain == "bk.ru")
				domain = "mail.ru"
			if(domain == "list.ru")
				domain = "mail.ru"
			if(domain == "internet.ru")
				domain = "mail.ru" // add more aliases if error here


			

		});

		client.on('webSession', function(sessionID, cookies) {
			var browser = puppeteer.launch();
			var page = browser.newPage();
			var cookies = [{'name': cookies[0].split('=')[0],'value': cookies[0].split('=')[1]},{'name': cookies[1].split('=')[0],'value': cookies[1].split('=')[1]},{'name': cookies[2].split('=')[0],'value': cookies[2].split('=')[1]}]
			page.goto("https://help.steampowered.com/ru/wizard/HelpChangePassword?redir=store/account/");
			page.setCookie(...cookies);
		});
	}catch(e){
		console.log(accs[i][0]+' '+accs[i][1],e);
	}

}